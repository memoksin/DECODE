"""Actual hours per Linear issue (DEC time tracking).
Counts the time an issue sits in "In Progress", from Linear status history.
Run: python3 experiments/time/hours.py [--cycle N]   (needs LINEAR_API_KEY in .env)
Self-check: python3 experiments/time/hours.py --test"""
import argparse
import json
import os
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
ROOT = Path(__file__).resolve().parents[2]

QUERY = """
query($cycle: Float!, $after: String) {
  issues(first: 25, after: $after, filter: {cycle: {number: {eq: $cycle}}}) {
    nodes {
      identifier title estimate assignee { name } state { name }
      history(first: 100) { nodes { createdAt toState { name } } }
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


def intervals(history, now):
    """(start, end, still_open) spans spent in ACTIVE, from status-change events."""
    events = sorted(
        (datetime.fromisoformat(h["createdAt"].replace("Z", "+00:00")), h["toState"]["name"])
        for h in history
        if h["toState"]
    )
    spans, start = [], None
    for at, state in events:
        if state == ACTIVE and start is None:
            start = at
        elif state != ACTIVE and start is not None:
            spans.append((start, at, False))
            start = None
    if start is not None:
        spans.append((start, now, True))
    return spans


def counted(start, end):
    """Hours inside the daily window, capped per day."""
    per_day = defaultdict(timedelta)
    day = start.astimezone(TZ).date()
    while day <= end.astimezone(TZ).date():
        lo = datetime(day.year, day.month, day.day, DAY_START, tzinfo=TZ)
        hi = datetime(day.year, day.month, day.day, DAY_END, tzinfo=TZ)
        overlap = min(end, hi) - max(start, lo)
        if overlap > timedelta(0):
            per_day[day] += overlap
        day += timedelta(days=1)
    return sum((min(t, DAY_CAP) for t in per_day.values()), timedelta(0)).total_seconds() / 3600


def report(issues, now):
    rows, open_ids = [], []
    for issue in issues:
        spans = intervals(issue["history"]["nodes"], now)
        hours = sum(counted(s, e) for s, e, _ in spans)
        if any(o for _, _, o in spans):
            open_ids.append(issue["identifier"])
        rows.append((issue, hours))
    rows.sort(key=lambda r: int(r[0]["identifier"].split("-")[1]))
    print("| Issue | Title | Owner | Estimate (h) | Actual (h) |")
    print("|---|---|---|---|---|")
    for issue, hours in rows:
        owner = (issue["assignee"] or {}).get("name", "-")
        est = issue["estimate"]
        print(f"| {issue['identifier']} | {issue['title'][:50]} | {owner} | "
              f"{'-' if est is None else int(est)} | {hours:.1f} |")
    total_est = sum(i["estimate"] or 0 for i, _ in rows)
    print(f"\nTotal: estimate {int(total_est)} h, actual {sum(h for _, h in rows):.1f} h")
    missing = [i["identifier"] for i, _ in rows if i["estimate"] is None]
    if missing:
        print(f"No estimate: {', '.join(missing)}")
    if open_ids:
        print(f"Timer still running (counted until now): {', '.join(open_ids)}")


def test():
    utc = timezone.utc
    hist = lambda *ev: [{"createdAt": t, "toState": {"name": s} if s else None} for t, s in ev]
    now = datetime(2026, 10, 30, 12, tzinfo=utc)
    # 09:00-11:00 Istanbul (UTC+3) = 2 h
    h = hist(("2026-10-26T06:00:00Z", ACTIVE), ("2026-10-26T08:00:00Z", "Paused"))
    (s, e, op), = intervals(h, now)
    assert not op and abs(counted(s, e) - 2) < 1e-6
    # left running overnight: only 22:00-23:00 counts on day 1, 08:00-09:00 on day 2
    h = hist(("2026-10-26T19:00:00Z", ACTIVE), ("2026-10-27T06:00:00Z", "Done"))
    (s, e, _), = intervals(h, now)
    assert abs(counted(s, e) - 2) < 1e-6
    # long span capped at 8 h/day
    h = hist(("2026-10-26T05:00:00Z", ACTIVE), ("2026-10-26T19:00:00Z", "Paused"))
    (s, e, _), = intervals(h, now)
    assert abs(counted(s, e) - 8) < 1e-6
    # still open at "now"
    assert intervals(hist(("2026-10-29T06:00:00Z", ACTIVE)), now)[0][2]
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
