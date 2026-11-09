DEC time tracking reminder (CLAUDE.md "Time tracking"). End every reply with one short line, in the user's language, that reminds them:
- Work on a Linear DEC issue → it must be `In Progress` now (only one per person).
- Stopping or end of day → `Paused`. Finished → `Done` + comment `⏱ Xh — note` (X from `python3 experiments/time/hours.py --cycle N`).
- No issue for this work yet → tell the user the estimate first and wait for their OK, then create it.
- 30-minute work → estimate 1 + label `30dk` (counted as 0.5 h). Hours may be adjusted (see CLAUDE.md "Sprint backlog and estimates"); never invent work.
Name the issue if you know it.
