# DECODE

## Tracking

- Linear: linear.app/decode2026, team key DEC
- DEC-1..8 are canceled placeholders
- Epic = project, Sprint 2 = cycle 2, ends Thu 26 Nov 2026 23:59 (Europe/Bucharest)
- Estimate: 1 point = 1 hour; label `30dk` = 30 minutes
- Role labels: teknik-lider (Mehmet), teknik-tasarim (İrem), literatur-veri (Sude), literatur-kalite (Burcu). Label every new task; shared tasks get none
- Hours (estimate + real) feed the sprint burndown and SRS 5.2
- Sprint 1 hours are estimates (real time was not measured)

## Time tracking

- Timer = Linear status: `In Progress` counts; `Paused`, `In Review`, `Done`, `Canceled` stop it
- One `In Progress` issue per person. Stop working → `Paused` (end of day too)
- Every new issue needs an estimate in hours
- Agent says the estimate before opening an issue; user accepts or changes it, then the agent opens it
- 30-minute work: estimate 1 + label `30dk`; `hours.py` counts the plan as 0.5 h (Linear takes whole numbers only)
- Hours: `python3 experiments/time/hours.py --cycle N` (needs `LINEAR_API_KEY` in `.env`, Read-only key; copy `.env.example`)
- Counts 08:00–23:00 Europe/Bucharest, max 8 h/day per issue; results are approximate
- Forgotten rules are handled by the script: timer stops at 23:00 of its start day; 2+ In Progress at once → time split; Done with no timer → estimate (source `estimate`)
- Latest `⏱ Xh` comment overrides the timer (use it to fix wrong hours)
- On Done: comment `⏱ Xh — note` with Actual from the script; script lists Done issues missing it
- Hours may be adjusted: see "Sprint backlog and estimates"
- Self-check: `python3 experiments/time/hours.py --test`
- Hook `.claude/hooks/linear-time-rules.py` blocks estimate-less issue creation, non-whole estimates and `30dk` without estimate 1; reminds on In Progress/Done; shows each new issue with its estimate in a prompt (user accepts or rejects)
- `.claude/hooks/setup_check.py` runs at SessionStart: repo behind origin, changed system files, missing `LINEAR_API_KEY`, failed self-checks. Silent when all is fine
- The team uses Windows: hooks and scripts stay Python stdlib only, no bash scripts, no `jq`. Needs Python + Git for Windows (hooks run in Git Bash)
- Claude Code runs it via `.claude/settings.json`; OpenCode via `.claude/plugins/linear-time.ts` (`.opencode` → `.claude` symlink)
- Agents remind the user every reply (In Progress / Paused / Done + ⏱); text in `.claude/hooks/time-reminder.md`, injected by both tools
- Cloud session (claude.ai/code): enable the claude.ai Linear connector (repo plugins don't load there); for `hours.py` add env var `LINEAR_API_KEY` and network access Custom + defaults + `api.linear.app`
- Never commit `.env`

## Agent messaging

- Channel: Linear comment + `@person`; DEC-54 if not tied to an issue
- People: @memoksin, @iremaltunsgt22, @sudeilaydamete, @burcubaran22
- Comment starts with `[agent]`; write high-level, not a full draft
- Before sending, tell the user in 1–2 lines what you will say; get approval
- On ambiguous topics the agent does not decide alone; rules: `.claude/hooks/inbox-rules.md`
- Delivery: `.claude/hooks/inbox.py`; at SessionStart and every 5 minutes as a prompt; each message once
- Everyone needs their own `LINEAR_API_KEY` in `.env`
- Self-check: `python3 .claude/hooks/inbox.py --test`

## Knowledge base

- Repo = team knowledge dump. Every finding goes into the repo, so reports (SRS, paper) can pull from it
- Findings: `docs/dec-XX-<topic>.md`, one file per issue, Turkish. Sections: Sonuç, Yöntem, Ölçümler, Sınırlamalar, Todo, SRS için cümle
- New result on an existing issue → update its file, do not open a new one
- Record at the time of work; reports cannot rebuild it later:
  - Measurements: raw numbers, date, who recorded, limitations
  - Hardware: device, camera model, CPU/GPU, OS
  - Versions: library, model, tool
  - Machine/system dependence: dependent or not, and whether it should be (in `Sınırlamalar`)
  - Sources: full citation of every paper and tool read
- Not recorded → write "not recorded" in the report; never guess
- Code and raw output: `experiments/dec-XX/`; recordings and weights stay local (git-ignored)
- Other docs: `docs/srs/`, `docs/toplantilar/`, `docs/arastirma-listesi.md`
- When asked "what did we find about X": search `docs/` first, cite the file
- Also post a short summary as a comment on the Linear issue

## Diagrams

- Use PlantUML syntax for diagrams (context, use case, etc.); ERD is the exception: Chen in draw.io
- Use Figma for UI design
- Per-type rules: `.claude/skills/diagramming/SKILL.md`
- Keep diagrams simple: easy to follow at a glance, few elements, no clutter
- Keep text short: brief labels, no long sentences

## Actors

- Developer: the person being interviewed. Never say "candidate"
- Interviewer: the person who runs the interview. Does not have to be HR; say so when you define it

## Reports and presentations

- From supervisor feedback (SRS presentation, 9 Nov 2026); applies to every report, slide, and spoken answer
- Presentation audience: 7 supervisors at the end of term
- Start every report and deck by defining the target audience and actors, with the terms in "Actors"
- Be specific: concrete numbers, names, versions, dates
- Results: name the hardware and say whether the result is machine- or system-dependent (data from the "Record at the time of work" notes)
- Slides: no sentences. Short labels, big fonts, readable visuals
- Animations welcome: they help supervisors picture a mechanism
- Spoken answers: max 10 seconds, short structure (e.g. "two reasons: …")
- Related work sources go into References

## Sprint backlog and estimates

- Supervisor: "it's just an estimate, keep it simple". Wanted: a general estimate, not a perfect day-by-day trace
- Estimate and real hours may both be changed, even by a lot
- Done far under estimate (2 h plan, 15 min real) → the estimate was wrong; cut it
- Timer forgotten (2 h plan, 6 h shown) → cut the real hours
- Mid-sprint additions are written as if planned from the start; trim other items to fit
- Hours may move. Work may not: never show work as done that was not done
- Note every adjustment in the `⏱` comment
