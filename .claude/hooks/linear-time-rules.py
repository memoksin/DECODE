#!/usr/bin/env python3
"""Linear save_issue rules from CLAUDE.md. Python stdlib only, so it also runs on Windows.
Used by Claude Code (PreToolUse) and OpenCode (.claude/plugins/linear-time.ts).
Self-check: python3 .claude/hooks/linear-time-rules.py --test"""
import json
import sys

HALF_HOUR_LABEL = "30dk"


def decide(tool_input):
    """(decision, reason, note): decision is deny, ask or None; note is extra context."""
    estimate = tool_input.get("estimate")
    is_new = not tool_input.get("id")
    labels = (tool_input.get("labels") or []) + (tool_input.get("addLabels") or [])
    half = HALF_HOUR_LABEL in labels
    state = (tool_input.get("state") or "").lower()

    if is_new and estimate is None:
        return "deny", "New Linear issues need an estimate in hours (1 point = 1 hour). Set estimate and retry.", None
    if estimate is not None and (isinstance(estimate, bool) or not isinstance(estimate, (int, float)) or estimate % 1):
        return "deny", f"Linear estimates are whole numbers. For 30 minutes use estimate 1 and label {HALF_HOUR_LABEL}.", None
    if half and estimate is not None and estimate != 1:
        return "deny", f"Label {HALF_HOUR_LABEL} needs estimate 1.", None

    note = None
    if state == "in progress":
        note = ("Timer starts now. Only one In Progress issue per person: move the assignee's other In Progress "
                "issues to Paused. The timer stops by itself at 23:00; next day set In Progress again.")
    elif state == "done":
        note = ("Timer stops. Post a comment '⏱ Xh — note' on the issue; X = Actual from: "
                "python3 experiments/time/hours.py --cycle N. The issue needs an estimate.")
    if is_new:
        plan = "30 minutes" if half else f"{estimate:g} h"
        return "ask", f"New Linear issue: {tool_input.get('title', '?')}. Plan: {plan}. Accept this estimate?", note
    return None, None, note


def output(decision, reason, note):
    """Hook JSON, or None when there is nothing to say."""
    if not decision and not note:
        return None
    out = {"hookEventName": "PreToolUse"}
    if decision:
        out.update(permissionDecision=decision, permissionDecisionReason=reason)
    if note:
        out["additionalContext"] = note
    return {"hookSpecificOutput": out}


def test():
    assert decide({"title": "a"})[0] == "deny"
    assert decide({"title": "a", "estimate": 0.5})[0] == "deny"
    assert decide({"title": "a", "estimate": 2, "labels": ["30dk"]})[0] == "deny"
    assert decide({"id": "DEC-1", "estimate": 3, "addLabels": ["30dk"]})[0] == "deny"
    # every new issue asks the user; 0 stays a real estimate
    assert decide({"title": "a", "estimate": 2})[:2] == ("ask", "New Linear issue: a. Plan: 2 h. Accept this estimate?")
    assert "30 minutes" in decide({"title": "a", "estimate": 1, "labels": ["30dk"]})[1]
    assert decide({"title": "a", "estimate": 0})[0] == "ask"
    # new issue created straight into In Progress keeps the timer note
    assert decide({"title": "a", "estimate": 1, "state": "In Progress"})[2].startswith("Timer starts")
    # updates pass without a prompt
    assert decide({"id": "DEC-1", "addLabels": ["30dk"]}) == (None, None, None)
    assert decide({"id": "DEC-1", "state": "Done"})[2].startswith("Timer stops")
    assert output(None, None, None) is None
    assert output("deny", "x", None)["hookSpecificOutput"]["permissionDecisionReason"] == "x"
    assert "permissionDecision" not in output(None, None, "n")["hookSpecificOutput"]
    print("ok")


def main():
    try:
        tool_input = json.load(sys.stdin.buffer).get("tool_input") or {}
    except ValueError as e:
        print(f"linear-time-rules: bad hook input: {e}", file=sys.stderr)
        return
    result = output(*decide(tool_input))
    if result:
        print(json.dumps(result))  # ASCII only, safe on any Windows console encoding


if __name__ == "__main__":
    test() if "--test" in sys.argv else main()
