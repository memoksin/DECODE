"""Actual hours per Linear issue (DEC time tracking).
Counts the time an issue sits in "In Progress", from Linear status history.
Works even when people forget the rules:
- forgot Paused at night: timer stops at 23:00 of the day it started
- two issues In Progress at once: that time is split between them
- a "⏱ Xh" comment on the issue overrides the timer (manual fix)
- Done but never In Progress and no comment: estimate is used, marked "estimate"
Run: python3 experiments/time/hours.py [--cycle N]   (needs LINEAR_API_KEY in .env)
Self-check: python3 experiments/time/hours.py --test"""
import argparse
import json
import os
import re
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Istanbul")
ACTIVE = "In Progress"
DAY_START, DAY_END = 8, 23  # time outside this window is not counted
DAY_CAP = timedelta(hours=8)  # max counted per issue per day
LOG_RE = re.compile(r"⏱\s*(\d+(?:[.,]\d+)?)\s*h")
ROOT = Path(__file__).resolve().parents[2]

QUERY = """
query($cycle: Float!, $after: String) {
  issues(first: 25, after: $after, filter: {cycle: {number: {eq: $cycle}}}) {
    nodes {
      identifier title estimate createdAt assignee { name } state { name type }
      history(first: 100) { nodes { createdAt fromState { name } toState { name } } }
      comments(first: 50) { nodes { body createdAt } }
    }
    pageInfo { hasNextPage endCursor }
  }
}"""


def load_env():
    path = ROOT / ".env"
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        key, sep, value = line.partition("=")
        if sep and not line.lstrip().startswith("#"):
            os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def gql(key, variables):
    req = urllib.request.Request(
        "https://api.linear.app/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": key, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        body = json.load(resp)
    if "errors" in body:
        sys.exit(f"Linear API error: {body['errors']}")
    return body["data"]["issues"]


def fetch_issues(key, cycle):
    issues, after = [], None
    while True:
        page = gql(key, {"cycle": cycle, "after": after})
        issues += page["nodes"]
        if not page["pageInfo"]["hasNextPage"]:
            return issues
        after = page["pageInfo"]["endCursor"]


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def intervals(issue, now):
    """(start, end, still_open) spans spent in ACTIVE, from status-change events."""
    events = sorted(
        ((ts(h["createdAt"]), h) for h in issue["history"]["nodes"] if h["toState"]),
        key=lambda e: e[0],
    )
    spans, start = [], None
    # created directly in In Progress: the first change leaves it, or there is no change yet
    first_from = (events[0][1].get("fromState") or {}).get("name") if events else issue["state"]["name"]
    if first_from == ACTIVE:
        start = ts(issue["createdAt"])
    for at, h in events:
        state = h["toState"]["name"]
        if state == ACTIVE and start is None:
            start = at
        elif state != ACTIVE and start is not None:
            spans.append((start, at, False))
            start = None
    if start is not None:
        spans.append((start, now, True))
    return spans


def day_bounds(day):
    return (datetime(day.year, day.month, day.day, DAY_START, tzinfo=TZ),
            datetime(day.year, day.month, day.day, DAY_END, tzinfo=TZ))


def cut_at_night(start, end):
    """Stop at DAY_END of the start day. Returns (end, forgot) where forgot = ran into the next workday."""
    day = start.astimezone(TZ).date()
    stop = day_bounds(day)[1]
    next_start = day_bounds(day + timedelta(days=1))[0]
    return min(end, stop), end > next_start


def split_shared(spans):
    """spans: {issue_id: [(start, end)]} of one person -> ({issue_id: [(start, end, weight)]}, shared_ids)."""
    points = sorted({t for sp in spans.values() for s, e in sp for t in (s, e)})
    pieces, shared = defaultdict(list), set()
    for a, b in zip(points, points[1:]):
        active = [i for i, sp in spans.items() if any(s <= a and b <= e for s, e in sp)]
        for i in active:
            pieces[i].append((a, b, 1 / len(active)))
        if len(active) > 1:
            shared.update(active)
    return pieces, shared


def counted(pieces):
    """Weighted hours inside the daily window, capped per day."""
    per_day = defaultdict(timedelta)
    for start, end, weight in pieces:
        day = start.astimezone(TZ).date()
        while day <= end.astimezone(TZ).date():
            lo, hi = day_bounds(day)
            overlap = min(end, hi) - max(start, lo)
            if overlap > timedelta(0):
                per_day[day] += overlap * weight
            day += timedelta(days=1)
    return sum((min(t, DAY_CAP) for t in per_day.values()), timedelta(0)).total_seconds() / 3600


def logged(issue):
    """Hours from the latest '⏱ Xh' comment, or None."""
    logs = sorted(
        (c["createdAt"], float(m.group(1).replace(",", ".")))
        for c in (issue.get("comments") or {}).get("nodes", [])
        if (m := LOG_RE.search(c["body"]))
    )
    return logs[-1][1] if logs else None


def resolve(issue, timer):
    """(hours, source) with fallbacks: comment > timer > estimate (Done only)."""
    log = logged(issue)
    if log is not None:
        return log, "comment"
    if timer > 0:
        return timer, "timer"
    if issue["state"]["type"] == "completed" and issue["estimate"] is not None:
        return float(issue["estimate"]), "estimate"
    return 0.0, "-"


def compute(issues, now):
    flags = defaultdict(list)
    by_owner = defaultdict(dict)
    for issue in issues:
        iid = issue["identifier"]
        spans = []
        for s, e, still_open in intervals(issue, now):
            e, forgot = cut_at_night(s, e)
            if forgot:
                flags["overnight"].append(iid)
            if still_open and not forgot:
                flags["running"].append(iid)
            if e > s:
                spans.append((s, e))
        owner = (issue["assignee"] or {}).get("name") or iid
        by_owner[owner][iid] = spans
    timer = {}
    for spans in by_owner.values():
        pieces, shared = split_shared(spans)
        flags["shared"] += sorted(shared)
        for iid in spans:
            timer[iid] = counted(pieces.get(iid, []))
    rows = []
    for issue in issues:
        hours, source = resolve(issue, timer[issue["identifier"]])
        rows.append((issue, timer[issue["identifier"]], hours, source))
        if source == "estimate":
            flags["estimate"].append(issue["identifier"])
        if issue["state"]["type"] == "completed" and source != "comment":
            flags["no_log"].append(issue["identifier"])
    rows.sort(key=lambda r: int(r[0]["identifier"].split("-")[1]))
    return rows, flags


def report(issues, now):
    rows, flags = compute(issues, now)
    print("| Issue | Title | Owner | State | Estimate (h) | Timer (h) | Actual (h) | Source |")
    print("|---|---|---|---|---|---|---|---|")
    for issue, timer, hours, source in rows:
        owner = (issue["assignee"] or {}).get("name", "-")
        est = issue["estimate"]
        print(f"| {issue['identifier']} | {issue['title'][:50]} | {owner} | {issue['state']['name']} | "
              f"{'-' if est is None else int(est)} | {timer:.1f} | {hours:.1f} | {source} |")
    total_est = sum(i["estimate"] or 0 for i, *_ in rows)
    print(f"\nTotal: estimate {int(total_est)} h, actual {sum(r[2] for r in rows):.1f} h")
    missing = [i["identifier"] for i, *_ in rows if i["estimate"] is None]
    notes = [
        ("No estimate", missing),
        ("Timer still running (counted until now, max 23:00)", flags["running"]),
        ("Left In Progress overnight (cut at 23:00, check real hours)", flags["overnight"]),
        ("Two+ In Progress at once (time split)", flags["shared"]),
        ("Done without timer or ⏱ comment (estimate used)", flags["estimate"]),
        ("Done without ⏱ comment (post Actual as '⏱ Xh — note')", flags["no_log"]),
    ]
    for label, ids in notes:
        if ids:
            print(f"{label}: {', '.join(sorted(set(ids), key=lambda x: int(x.split('-')[1])))}")


def test():
    utc = timezone.utc
    now = datetime(2026, 10, 30, 12, tzinfo=utc)

    def issue(iid, *ev, owner="A", state=("Todo", "unstarted"), est=2, created="2026-10-25T00:00:00Z", logs=()):
        return {
            "identifier": iid, "title": "t", "estimate": est, "createdAt": created,
            "assignee": {"name": owner}, "state": {"name": state[0], "type": state[1]},
            "history": {"nodes": [{"createdAt": t, "fromState": {"name": f} if f else None,
                                   "toState": {"name": s} if s else None} for t, f, s in ev]},
            "comments": {"nodes": [{"body": b, "createdAt": t} for t, b in logs]},
        }

    def hours(*issues):
        return {i["identifier"]: (h, src) for i, _, h, src in compute(list(issues), now)[0]}

    # 09:00-11:00 Istanbul (UTC+3) = 2 h
    i = issue("DEC-1", ("2026-10-26T06:00:00Z", "Todo", ACTIVE), ("2026-10-26T08:00:00Z", ACTIVE, "Paused"))
    assert abs(hours(i)["DEC-1"][0] - 2) < 1e-6
    # forgot Paused overnight: only 22:00-23:00 counts, next morning does not
    i = issue("DEC-1", ("2026-10-26T19:00:00Z", "Todo", ACTIVE), ("2026-10-27T09:00:00Z", ACTIVE, "Done"))
    rows, flags = compute([i], now)
    assert abs(rows[0][1] - 1) < 1e-6 and flags["overnight"] == ["DEC-1"]
    # long day capped at 8 h
    i = issue("DEC-1", ("2026-10-26T05:00:00Z", "Todo", ACTIVE), ("2026-10-26T19:00:00Z", ACTIVE, "Paused"))
    assert abs(hours(i)["DEC-1"][0] - 8) < 1e-6
    # two issues In Progress at once for one person: 09-11 shared -> 1 h each, 11-12 only DEC-2
    a = issue("DEC-1", ("2026-10-26T06:00:00Z", "Todo", ACTIVE), ("2026-10-26T08:00:00Z", ACTIVE, "Paused"))
    b = issue("DEC-2", ("2026-10-26T06:00:00Z", "Todo", ACTIVE), ("2026-10-26T09:00:00Z", ACTIVE, "Paused"))
    h = hours(a, b)
    assert abs(h["DEC-1"][0] - 1) < 1e-6 and abs(h["DEC-2"][0] - 2) < 1e-6
    # different people are not split
    b["assignee"] = {"name": "B"}
    h = hours(a, b)
    assert abs(h["DEC-1"][0] - 2) < 1e-6 and abs(h["DEC-2"][0] - 3) < 1e-6
    # created directly in In Progress (09:00), paused 10:00
    i = issue("DEC-1", ("2026-10-26T07:00:00Z", ACTIVE, "Paused"), created="2026-10-26T06:00:00Z")
    assert abs(hours(i)["DEC-1"][0] - 1) < 1e-6
    # latest ⏱ comment overrides the timer
    i = issue("DEC-1", ("2026-10-26T06:00:00Z", "Todo", ACTIVE), ("2026-10-26T08:00:00Z", ACTIVE, "Done"),
              logs=[("2026-10-26T09:00:00Z", "⏱ 3h — x"), ("2026-10-26T10:00:00Z", "⏱ 1,5h — fix")])
    assert hours(i)["DEC-1"] == (1.5, "comment")
    # Done but never In Progress: estimate fallback; not Done: 0
    i = issue("DEC-1", ("2026-10-26T06:00:00Z", "Todo", "Done"), state=("Done", "completed"), est=3)
    assert hours(i)["DEC-1"] == (3.0, "estimate")
    i["state"] = {"name": "Todo", "type": "unstarted"}
    assert hours(i)["DEC-1"] == (0.0, "-")
    # still running today, started 13:00 Istanbul, now 15:00
    i = issue("DEC-1", ("2026-10-30T10:00:00Z", "Todo", ACTIVE))
    rows, flags = compute([i], now)
    assert abs(rows[0][1] - 2) < 1e-6 and flags["running"] == ["DEC-1"]
    print("ok")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cycle", type=int, default=1)
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args()
    if args.test:
        test()
        sys.exit()
    load_env()
    key = os.environ.get("LINEAR_API_KEY")
    if not key:
        sys.exit("Set LINEAR_API_KEY in .env (see .env.example)")
    report(fetch_issues(key, args.cycle), datetime.now(timezone.utc))
