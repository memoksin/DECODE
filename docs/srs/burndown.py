"""Sprint 1 burndown (DEC-14). Remaining = estimated hours of tasks not yet done.
Run: experiments/dec-45/.venv/bin/python docs/srs/burndown.py  (needs matplotlib)
Update ACTUAL with the 27 Oct value when the sprint ends."""
from pathlib import Path

import matplotlib.pyplot as plt

TOTAL = 102  # 28 estimated tasks in Linear cycle 1
DAYS = ["7 Oct", "13 Oct", "20 Oct", "27 Oct"]
ACTUAL = [102, 95, 71, 68]  # last point: 23 Oct, sprint still running

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(range(4), [TOTAL * (1 - i / 3) for i in range(4)], "--", color="gray", label="Ideal")
x = list(range(len(ACTUAL)))
if len(ACTUAL) == 4:
    x[-1] = 2 + 3 / 7  # 23 Oct sits 3 days into week 3
ax.plot(x, ACTUAL, "o-", color="tab:blue", label="Remaining (estimated h)")
for xi, y in zip(x, ACTUAL):
    ax.annotate(str(y), (xi, y), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8)
ax.set_xticks(range(4), DAYS)
ax.set_ylabel("Remaining hours")
ax.set_title("Sprint 1 burndown")
ax.set_ylim(0, TOTAL * 1.1)
ax.legend()
fig.tight_layout()
fig.savefig(Path(__file__).with_name("burndown-sprint-1.png"), dpi=150)
