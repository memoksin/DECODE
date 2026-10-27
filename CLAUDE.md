# DECODE

## Tracking

- Linear: linear.app/decode2026, team key DEC
- DEC-1..8 are canceled placeholders
- Epic = project, Sprint 1 = cycle 1
- Estimate: 1 point = 1 hour
- Role labels: teknik-lider (Mehmet), teknik-tasarim (İrem), literatur-veri (Sude), literatur-kalite (Burcu). Label every new task; shared tasks get none
- Time spent: comment `⏱ Xh — note` on each finished issue (SRS 5.2 needs hours)
- Sprint 1 hours = estimates (real time not measured). Real measurement starts Sprint 2

## Time tracking

- Timer = Linear status: `In Progress` counts; `Paused`, `In Review`, `Done`, `Canceled` stop it
- One `In Progress` issue per person. Stop working → `Paused` (end of day too)
- Every new issue needs an estimate in hours (1 point = 1 hour)
- Hours: `python3 experiments/time/hours.py --cycle N` (needs `LINEAR_API_KEY` in `.env`, Read-only key; copy `.env.example`)
- Counts 08:00–23:00 Istanbul, max 8 h/day per issue; results are approximate
- On Done: comment `⏱ Xh — note` with hours from the script
- Hook `.claude/hooks/linear-time-rules.sh` blocks estimate-less issue creation and reminds on In Progress/Done
- Never commit `.env`
- Supervisor wants hours in the sprint burndown (estimate + real time); SRS uses hours

## Knowledge base

- Repo = team knowledge dump. Every finding goes into the repo, so reports (SRS, paper) can pull from it
- Findings: `docs/dec-XX-<topic>.md`, one file per issue, Turkish. Sections: Sonuç, Yöntem, Ölçümler, Sınırlamalar, Todo, SRS için cümle
- New result on an existing issue → update its file, do not open a new one
- Keep raw numbers, dates, who recorded, and limitations; reports need them later
- Code and raw output: `experiments/dec-XX/`; recordings and weights stay local (git-ignored)
- Other docs: `docs/srs/`, `docs/toplantilar/`, `docs/arastirma-listesi.md`
- When asked "what did we find about X": search `docs/` first, cite the file
- Also post a short summary as a comment on the Linear issue

## Diagrams

- Use PlantUML syntax for all diagrams (context, use case, ERD, etc.)
- Use Figma for UI design.
- Per-type rules: `.claude/skills/diagramming/SKILL.md` (ERD: Chen in draw.io, not PlantUML)
- Keep diagrams simple: easy to follow at a glance, few elements, no clutter
- Keep text short and concise: brief labels, no long sentences
