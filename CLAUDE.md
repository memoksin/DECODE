# DECODE

## Tracking

- Linear: linear.app/decode2026, team key DEC. Jira (decode2026.atlassian.net) is archive only, do not delete
- DEC-9..46 keep Jira numbers; DEC-1..8 are canceled placeholders
- Epic = project, Sprint 1 = cycle 1
- Estimate: 1 point = 1 hour
- Role labels: teknik-lider (Mehmet), teknik-tasarim (İrem), literatur-veri (Sude), literatur-kalite (Burcu). Label every new task; shared tasks get none
- Time spent: comment `⏱ Xh — note` on each finished issue (SRS 5.2 needs hours)
- Supervisor (2026-10-25): team may write the report and make burndown charts itself. Story points: no clear answer; SRS uses hours, may switch to story points later

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
- No Mermaid
- Per-type rules: `.claude/skills/diagramming/SKILL.md` (ERD: Chen in draw.io, not PlantUML)
- Keep diagrams simple: easy to follow at a glance, few elements, no clutter
- Keep text short and concise: brief labels, no long sentences
