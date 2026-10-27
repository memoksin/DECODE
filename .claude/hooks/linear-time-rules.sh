#!/usr/bin/env bash
# Linear save_issue rules from CLAUDE.md. Used by Claude Code (PreToolUse) and OpenCode (.claude/plugins/linear-time.ts).
in=$(cat)
id=$(jq -r '.tool_input.id // empty' <<<"$in")
state=$(jq -r '.tool_input.state // "" | ascii_downcase' <<<"$in")
estimate=$(jq -r '.tool_input.estimate // empty' <<<"$in")

emit() { jq -n --arg k "$1" --arg v "$2" '{hookSpecificOutput: ({hookEventName: "PreToolUse"} + (if $k == "deny" then {permissionDecision: "deny", permissionDecisionReason: $v} else {additionalContext: $v} end))}'; }

if [ -z "$id" ] && [ -z "$estimate" ]; then
  emit deny "New Linear issues need an estimate in hours (1 point = 1 hour). Set estimate and retry."
elif [ "$state" = "in progress" ]; then
  emit note "Timer starts now. Only one In Progress issue per person: move the assignee's other In Progress issues to Paused. The timer stops by itself at 23:00; next day set In Progress again."
elif [ "$state" = "done" ]; then
  emit note "Timer stops. Post a comment '⏱ Xh — note' on the issue; X = Actual from: python3 experiments/time/hours.py --cycle N. The issue needs an estimate."
fi
