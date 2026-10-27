"""Sprint 1 burndown (DEC-14). Remaining = estimated hours of sprint tasks not done yet.
Run: experiments/dec-45/.venv/bin/python docs/srs/burndown.py  (needs matplotlib)
Data: Linear cycle 1 on 27 Oct 2026. Tasks moved from Jira on 22 Oct keep their Jira done dates.
DEC-47..52 were split from DEC-24/25/29/35 on 26 Oct, so they count from the start.
Update DONE when more tasks close."""
from datetime import date, timedelta
from pathlib import Path

import matplotlib.pyplot as plt

START, END = date(2026, 10, 7), date(2026, 10, 27)
ADDED = date(2026, 10, 22)  # DEC-38..46 added after the second supervisor meeting (DEC-37 canceled)

ESTIMATE = {  # issue: hours
    9: 2, 10: 2, 11: 2, 12: 1, 13: 1, 14: 3, 15: 6, 16: 6, 17: 2, 18: 3, 19: 3, 20: 2, 21: 6, 22: 6,
    23: 4, 24: 2, 25: 2, 26: 3, 27: 6, 28: 6, 29: 1, 30: 3, 31: 6, 32: 6, 33: 4, 34: 2, 35: 1, 36: 5,
    47: 1, 48: 3, 49: 1, 50: 1, 51: 1, 52: 1,
    38: 1, 39: 4, 42: 2, 43: 3, 44: 1, 45: 2, 46: 2,
}
DONE = {  # issue: day of October
    9: 13, 10: 13, 11: 13, 13: 13,
    12: 20, 16: 20, 17: 20, 18: 20, 22: 20, 31: 20,
    38: 21, 42: 22, 19: 23, 44: 23, 45: 25,
    15: 26, 29: 26, 33: 26, 47: 26, 48: 26, 50: 26, 52: 26,
    14: 27, 25: 27, 27: 27, 35: 27, 36: 27, 43: 27, 51: 27,
    20: 27, 23: 27, 24: 27, 26: 27, 30: 27, 34: 27, 49: 27,
}


def in_scope(issue, day):
    return issue < 38 or issue > 46 or day >= ADDED


def remaining(day):
    return sum(h for i, h in ESTIMATE.items()
               if in_scope(i, day) and not (i in DONE and date(2026, 10, DONE[i]) <= day))


days = [START + timedelta(d) for d in range((END - START).days + 1)]
values = [remaining(d) for d in days]
assert values[0] == 104 and sum(ESTIMATE.values()) == 119, values

fig, ax = plt.subplots(figsize=(7, 3.8))
ax.plot([0, len(days) - 1], [values[0], 0], "--", color="gray", label="Ideal")
ax.plot(range(len(days)), values, "o-", ms=3, color="tab:blue", label="Remaining (estimated h)")
for i in (0, 6, 13, 15, len(days) - 1):
    ax.annotate(str(values[i]), (i, values[i]), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=8)
ax.annotate("+15 h added", (15, values[15]), textcoords="offset points", xytext=(18, 14), fontsize=8,
            arrowprops={"arrowstyle": "->", "color": "gray"})
ticks = [0, 6, 13, 20]
ax.set_xticks(ticks, [days[t].strftime("%-d %b") for t in ticks])
ax.set_xlabel("Week")
ax.set_ylabel("Remaining hours")
ax.set_title("Sprint 1 burndown")
ax.set_ylim(0, 125)
ax.legend()
fig.tight_layout()
fig.savefig(Path(__file__).with_name("burndown-sprint-1.png"), dpi=150)
print(dict(zip([d.strftime("%d %b") for d in days], values)))
