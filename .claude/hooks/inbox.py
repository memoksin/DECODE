#!/usr/bin/env python3
"""Agent inbox: prints this user's new Linear mentions and assignments, each one once.
Runs as a hook: SessionStart (--session) and UserPromptSubmit (at most every 5 min).
Prints nothing if there is nothing new, no key, or the request fails.
Needs the user's own LINEAR_API_KEY in .env (notifications are per user).
Self-check: python3 .claude/hooks/inbox.py --test"""
import contextlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
START = "2026-11-03T22:00:00.000Z"  # older notifications never show
THROTTLE = 300
LOCK_MAX_AGE = 30
MAX_MESSAGES = 10
MAX_CHARS = 400
WANTED = re.compile(r"mention|assigned", re.I)

QUERY = """
query($since: DateTimeOrDuration!) {
  notifications(first: 50, includeArchived: true, orderBy: createdAt,
                filter: {createdAt: {gt: $since}}) {
    nodes {
      type createdAt actor { displayName }
      ... on IssueNotification { issue { identifier title } comment { body } }
    }
  }
}"""


def api_key():
    key = os.environ.get("LINEAR_API_KEY")
    env = ROOT / ".env"
    if key or not env.exists():
        return key
    for line in env.read_text(encoding="utf-8").splitlines():
        name, sep, value = line.partition("=")
        if sep and name.strip() == "LINEAR_API_KEY":
            return value.strip().strip("\"'")
    return None


def fetch(key, since):
    req = urllib.request.Request(
        "https://api.linear.app/graphql",
        data=json.dumps({"query": QUERY, "variables": {"since": since}}).encode(),
        headers={"Authorization": key, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=5) as resp:
        body = json.load(resp)
    if "errors" in body:
        raise RuntimeError(body["errors"])
    return body["data"]["notifications"]["nodes"]


def select(nodes, since):
    new = [n for n in nodes if WANTED.search(n["type"]) and n["createdAt"] > since]
    return sorted(new, key=lambda n: n["createdAt"])[:MAX_MESSAGES]


def render(node):
    issue = node.get("issue") or {}
    actor = (node.get("actor") or {}).get("displayName", "?")
    comment = node.get("comment") or {}
    text = comment.get("body") or f"Assigned: {issue.get('title', '')}"
    if len(text) > MAX_CHARS:
        text = f"{text[:MAX_CHARS]}… (cut; read the full text in Linear)"
    return f"[{issue.get('identifier', '?')}] from @{actor}:\n{text}"


def state_dir():
    out = subprocess.run(
        ["git", "rev-parse", "--git-common-dir"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.strip()
    return ROOT / out / "agent-inbox"


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def save(path, state):
    tmp = path.with_suffix(f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(state), encoding="utf-8")
    os.replace(tmp, path)


@contextlib.contextmanager
def locked(folder):
    """Yields True if this process holds the lock. Two sessions never get the same message."""
    lock = folder / "lock"
    with contextlib.suppress(FileNotFoundError):
        if time.time() - lock.stat().st_mtime > LOCK_MAX_AGE:
            lock.rmdir()
    try:
        lock.mkdir()
    except FileExistsError:
        yield False
        return
    try:
        yield True
    finally:
        lock.rmdir()


def check(folder, get_nodes, session, now):
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "state.json"
    with locked(folder) as owner:
        if not owner:
            return
        state = load(path)
        if not session and now - state.get("last_check", 0) < THROTTLE:
            return
        since = state.get("last_seen", START)
        # Saved before the request: a dead network must not slow every prompt.
        save(path, {**state, "last_check": now})
        messages = select(get_nodes(since), since)
        if not messages:
            return
        rules = (ROOT / ".claude/hooks/inbox-rules.md").read_text(encoding="utf-8")
        print(rules.rstrip())
        print("\n<inbox-messages>")
        print("\n\n".join(render(m) for m in messages))
        print("</inbox-messages>")
        save(path, {**state, "last_check": now, "last_seen": messages[-1]["createdAt"]})


def main():
    # Headless workers (claude -p) must not use up messages meant for the person.
    if os.environ.get("CLAUDE_CODE_ENTRYPOINT", "").startswith("sdk"):
        return
    key = api_key()
    if not key:
        return
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        check(state_dir(), lambda since: fetch(key, since), "--session" in sys.argv, time.time())
    except Exception as e:  # a broken inbox must never block the user's prompt
        print(f"inbox.py: {e}", file=sys.stderr)


def test():
    def note(minute, kind="issueCommentMention", body="soru"):
        return {
            "type": kind,
            "createdAt": f"2026-11-04T10:{minute:02d}:00.000Z",
            "actor": {"displayName": "sude"},
            "issue": {"identifier": "DEC-54", "title": "t"},
            "comment": {"body": body},
        }

    def run(folder, nodes, session=True, now=1000):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            check(folder, lambda since: nodes, session, now)
        return out.getvalue()

    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        noise = note(1, "issueStatusChanged")
        assert run(folder, [noise]) == "", "other types stay out"

        first = run(folder, [noise, note(2, body="ilk")])
        assert "ilk" in first and "<inbox-messages>" in first
        assert run(folder, [note(2, body="ilk")]) == "", "a message comes once"

        assert run(folder, [note(3)], session=False, now=1100) == "", "throttled"
        assert "soru" in run(folder, [note(3)], session=False, now=1400), "after throttle"

        def fail(since):
            raise OSError("network")

        before = load(folder / "state.json")["last_seen"]
        try:
            check(folder, fail, True, 2000)
        except OSError:
            pass
        assert load(folder / "state.json")["last_seen"] == before, "failure loses nothing"
        assert not (folder / "lock").exists(), "lock released after failure"
        assert "soru" in run(folder, [note(4)]), "message survives the failure"

        many = [note(10 + i, body=f"m{i}") for i in range(12)]
        batch = run(folder, many)
        assert "m9" in batch and "m10" not in batch, "max 10 per check"
        rest = run(folder, many)
        assert "m10" in rest and "m11" in rest and "m9" not in rest, "the rest come next"

        (folder / "lock").mkdir()
        assert run(folder, [note(40)]) == "", "another session holds the lock"
        (folder / "lock").rmdir()
        assert "soru" in run(folder, [note(40)]), "nothing lost to the lock"

    assert "Assigned: t" in render({**note(1, "issueAssignedToYou"), "comment": None})
    assert "(cut;" in render(note(1, body="x" * 500))
    print("ok")


if __name__ == "__main__":
    test() if "--test" in sys.argv else main()
