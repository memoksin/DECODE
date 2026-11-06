#!/usr/bin/env python3
"""SessionStart check that everyone runs the same system. Python stdlib only (Windows too).
Prints nothing when all is fine. Otherwise prints what is wrong so the agent tells the user.
Self-check: python3 .claude/hooks/setup_check.py --test"""
import os
import subprocess
import sys
from pathlib import Path

from inbox import api_key

ROOT = Path(__file__).resolve().parents[2]
SYSTEM_PATHS = ["CLAUDE.md", ".claude/settings.json", ".claude/hooks", ".claude/plugins", "experiments/time"]
SELF_CHECKS = [".claude/hooks/linear-time-rules.py", ".claude/hooks/inbox.py", "experiments/time/hours.py"]


def run(*cmd, timeout=8):
    """(exit code, output); a command that cannot run counts as failed."""
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, encoding="utf-8", errors="replace", timeout=timeout,
                           env={**os.environ, "GIT_TERMINAL_PROMPT": "0", "PYTHONIOENCODING": "utf-8"})
    except (OSError, subprocess.TimeoutExpired) as e:
        return 1, str(e)
    return r.returncode, (r.stdout + r.stderr).strip()


def repo_problems(git):
    problems = []
    code, _ = git("fetch", "--quiet", "origin", "main")
    if code:
        problems.append("Could not reach origin, so the update check was skipped.")
    else:
        code, behind = git("rev-list", "--count", "HEAD..origin/main")
        if code:
            problems.append(f"Could not compare with origin/main: {behind}")
        elif behind != "0":
            problems.append(f"Repo is {behind} commit(s) behind origin/main. Offer to run `git pull`, then restart the session.")
    code, changed = git("diff", "--name-only", "HEAD", "--", *SYSTEM_PATHS)
    if code:
        problems.append(f"Could not check system files: {changed}")
    elif changed:
        problems.append("System files differ from the repo: " + ", ".join(changed.split()))
    return problems


def check_problems(execute):
    problems = []
    for script in SELF_CHECKS:
        code, out = execute(sys.executable, script, "--test", timeout=10)
        if code:
            problems.append(f"Self-check failed: {script}: {out[-300:]}")
    return problems


def test():
    def git(*replies):
        answers = iter(replies)
        return lambda *a: next(answers)

    assert repo_problems(git((0, ""), (0, "0"), (0, ""))) == []
    assert "2 commit(s) behind" in repo_problems(git((0, ""), (0, "2"), (0, "")))[0]
    assert "CLAUDE.md" in repo_problems(git((0, ""), (0, "0"), (0, "CLAUDE.md")))[0]
    assert "skipped" in repo_problems(git((1, "no net"), (0, "")))[0]
    assert check_problems(lambda *a, timeout: (0, "ok")) == []
    assert len(check_problems(lambda *a, timeout: (1, "boom"))) == len(SELF_CHECKS)
    print("ok")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    problems = repo_problems(lambda *a: run("git", *a)) + check_problems(run)
    if not api_key():
        problems.append("LINEAR_API_KEY is missing. Copy .env.example to .env and add your own key.")
    if problems:
        print("DECODE setup check found problems. Tell the user now:")
        print("\n".join(f"- {p}" for p in problems))


if __name__ == "__main__":
    test() if "--test" in sys.argv else main()
