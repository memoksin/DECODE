# DECODE

## Tracking

- Linear: linear.app/decode2026, team key DEC
- DEC-1..8 are canceled placeholders
- Epic = project, Sprint 1 = cycle 1
- Estimate: 1 point = 1 hour; label `30dk` = 30 minutes
- Role labels: teknik-lider (Mehmet), teknik-tasarim (İrem), literatur-veri (Sude), literatur-kalite (Burcu). Label every new task; shared tasks get none
- Time spent: comment `⏱ Xh — note` on each finished issue (SRS 5.2 needs hours)
- Sprint 1 hours = estimates (real time not measured). Real measurement starts Sprint 2

## Time tracking

- Timer = Linear status: `In Progress` counts; `Paused`, `In Review`, `Done`, `Canceled` stop it
- One `In Progress` issue per person. Stop working → `Paused` (end of day too)
- Every new issue needs an estimate in hours (1 point = 1 hour)
- Agent says the estimate before opening an issue; user accepts or changes it, then the agent opens it
- 30-minute work: estimate 1 + label `30dk`; `hours.py` counts the plan as 0.5 h (Linear takes whole numbers only)
- Real time is not multiplied or changed to fit a plan; small fixes only as in "Sprint backlog and estimates"
- Hours: `python3 experiments/time/hours.py --cycle N` (needs `LINEAR_API_KEY` in `.env`, Read-only key; copy `.env.example`)
- Counts 08:00–23:00 Istanbul, max 8 h/day per issue; results are approximate
- Forgotten rules are handled by the script: timer stops at 23:00 of its start day; 2+ In Progress at once → time split; Done with no timer → estimate (source `estimate`)
- Latest `⏱ Xh` comment overrides the timer (use it to fix wrong hours)
- On Done: comment `⏱ Xh — note` with Actual from the script; script lists Done issues missing it
- Self-check: `python3 experiments/time/hours.py --test`
- Hook `.claude/hooks/linear-time-rules.py` blocks estimate-less issue creation, non-whole estimates and `30dk` without estimate 1; reminds on In Progress/Done
- The same hook shows every new issue with its estimate in a prompt; the user accepts or rejects it
- `.claude/hooks/setup_check.py` runs at SessionStart: repo behind origin, changed system files, missing `LINEAR_API_KEY`, failed self-checks. Silent when all is fine
- The team uses Windows: hooks and scripts stay Python stdlib only, no bash scripts, no `jq`. Needs Python + Git for Windows (hooks run in Git Bash)
- Claude Code runs it via `.claude/settings.json`; OpenCode via `.claude/plugins/linear-time.ts` (`.opencode` → `.claude` symlink)
- Agents remind the user every reply (In Progress / Paused / Done + ⏱); text in `.claude/hooks/time-reminder.md`, injected by both tools
- Cloud session (claude.ai/code): enable the claude.ai Linear connector (repo plugins don't load there); for `hours.py` add env var `LINEAR_API_KEY` and network access Custom + defaults + `api.linear.app`
- Never commit `.env`
- Supervisor wants hours in the sprint burndown (estimate + real time); SRS uses hours

## Agent mesajlaşma

- Kanal: Linear yorumu + `@kişi`; işe bağlı değilse DEC-54
- Kişiler: @memoksin, @iremaltunsgt22, @sudeilaydamete, @burcubaran22
- Yorum `[agent]` ile başlar; high-level yaz, tam taslak değil
- Göndermeden önce kullanıcıya 1-2 satırla ne diyeceğini söyle, onay al
- Muğlak konuda agent tek başına karar vermez; kurallar: `.claude/hooks/inbox-rules.md`
- Teslim: `.claude/hooks/inbox.py`; SessionStart + 5 dakikada bir prompt; her mesaj bir kez
- Herkesin `.env` dosyasında kendi `LINEAR_API_KEY` olmalı
- Self-check: `python3 .claude/hooks/inbox.py --test`

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

## Reports and presentations

- Supervisor feedback (SRS presentation, 9 Nov 2026); applies to every report, slide, and answer
- Audience: 7 supervisors at the end-of-term presentation
- Define target audience and actors first, at the very start
- Be specific everywhere: concrete numbers, names, versions; no vague wording
- Hardware: name the exact device/model/spec. Say if a result is machine- or system-dependent, and whether it should be
- Slides: no sentences. Short labels, big fonts, readable visuals
- Animations welcome: they help supervisors picture a mechanism
- Spoken answers: max 10 seconds, short structure (e.g. "two reasons: …")
- Related work goes into References

## Sprint backlog and estimates

- Wanted: general estimation, not a perfect day-by-day trace
- Estimates and real hours may both be adjusted a little (supervisor allowed it)
- Task done far under estimate (2 h plan, 15 min real) → estimate was wrong, cut it
- Timer forgotten (2 h plan, 6 h shown) → real hours may be cut a little
- Mid-sprint additions are written as if planned from the start; trim other items to fit
- Note every adjustment in the `⏱` comment
