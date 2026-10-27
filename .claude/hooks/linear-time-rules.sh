#!/usr/bin/env bash
# PreToolUse hook for Linear save_issue: enforce the time-tracking rules in CLAUDE.md.
in=$(cat)
id=$(jq -r '.tool_input.id // empty' <<<"$in")
state=$(jq -r '.tool_input.state // empty' <<<"$in")
estimate=$(jq -r '.tool_input.estimate // empty' <<<"$in")

emit() { jq -n --arg k "$1" --arg v "$2" '{hookSpecificOutput: ({hookEventName: "PreToolUse"} + (if $k == "deny" then {permissionDecision: "deny", permissionDecisionReason: $v} else {additionalContext: $v} end))}'; }

if [ -z "$id" ] && [ -z "$estimate" ]; then
  emit deny "New Linear issues need an estimate in hours (1 point = 1 hour). Set estimate and retry."
elif [ "$state" = "In Progress" ]; then
  emit note "Timer starts now. Only one In Progress issue per person: move the assignee's other In Progress issues to Paused."
elif [ "$state" = "Done" ]; then
  emit note "Timer stops. Post a comment '⏱ Xh — note' on the issue; X comes from: python3 experiments/time/hours.py. The issue needs an estimate."
fi
