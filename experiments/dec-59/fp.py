"""DEC-59: IFPUG Function Point cross-check of the SRS 3 size estimate.

Run: python3 experiments/dec-59/fp.py
"""

WEIGHTS = {"EI": (3, 4, 6), "EO": (4, 5, 7), "EQ": (3, 4, 6), "ILF": (7, 10, 15), "EIF": (5, 7, 10)}
L, A, H = 0, 1, 2

# Complexity from IFPUG DET/RET/FTR matrices, using ERD attributes and UI-1..UI-5 fields.
ITEMS = [
    ("ILF", "Interviewer", L), ("ILF", "Session", L), ("ILF", "Candidate", L),
    ("ILF", "CodeStimulus + AOI blocks", L), ("ILF", "Scanpath + result", L),
    ("ILF", "Dataset", L), ("ILF", "Trending path (F9)", L),
    ("EIF", "Public dataset raw files", L), ("EIF", "MiroTalk room/participants", L),
    ("EI", "Create session", L), ("EI", "End session", L), ("EI", "Consent", L),
    ("EI", "Calibration + validation", L), ("EI", "Upload + analyse recording", H),
    ("EI", "Import dataset", A), ("EI", "Build trending paths (STA)", A), ("EI", "Add code stimulus", L),
    ("EO", "Classification report", H), ("EO", "Live session status", A),
    ("EO", "Calibration feedback", L), ("EO", "Camera quality check", L), ("EO", "Model evaluation", A),
    ("EQ", "Session list", L), ("EQ", "Candidates joined", L), ("EQ", "Code view", L), ("EQ", "Stimulus list", L),
]

# 14 General System Characteristics, 0-5, in IFPUG order.
GSC = [4, 3, 4, 3, 1, 2, 4, 2, 5, 2, 3, 3, 3, 2]

# Share of new code per language, from SRS 3.2 (823 JS, 1602 Python of 2425 SLOC).
JS_SHARE, PY_SHARE = 823 / 2425, 1602 / 2425

# LOC per FP: Jones 2017 Table 16 (JS 71.11, Python 53.33); QSM table (JS 47, no Python).
SCENARIOS = [("Jones JS + Jones Python", 71.11, 53.33), ("QSM JS + Jones Python", 47.0, 53.33)]

# Same COCOMO II inputs as SRS 3.4.
EAF, EXP = 1.458, 1.121
ANALOGY_KSLOC, HOURS_PER_PM = 2.81, 152


def function_points():
    by_type = {}
    for kind, _, level in ITEMS:
        by_type[kind] = by_type.get(kind, 0) + WEIGHTS[kind][level]
    utfp = sum(by_type.values())
    vaf = sum(GSC) * 0.01 + 0.65
    return by_type, utfp, vaf, utfp * vaf


def main():
    by_type, utfp, vaf, afp = function_points()
    assert utfp == 125 and len(GSC) == 14 and abs(vaf - 1.06) < 1e-9
    print(f"{by_type}  UTFP {utfp}  VAF {vaf:.2f}  AFP {afp:.1f}")
    for name, js, py in SCENARIOS:
        loc_per_fp = JS_SHARE * js + PY_SHARE * py
        ksloc = afp * loc_per_fp / 1000
        basic = 2.4 * ksloc ** 1.05
        c2 = 2.94 * ksloc ** EXP * EAF
        print(f"{name}: {loc_per_fp:.1f} LOC/FP -> {ksloc:.2f} KSLOC ({ksloc / ANALOGY_KSLOC:.1f}x analogy) | "
              f"Basic {basic:.1f} PM {basic * HOURS_PER_PM:.0f} h | COCOMO II {c2:.1f} PM {c2 * HOURS_PER_PM:.0f} h")


if __name__ == "__main__":
    main()
