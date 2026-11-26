"""SRS 3 Software Estimation (DEC-19, DEC-61). Run: python3 docs/srs/estimation.py

Only methods from CNG491 Lecture 3: FP -> LOC -> Basic COCOMO, Jones First-Order, analogy.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "experiments" / "dec-59"))
from fp import function_points  # noqa: E402

# UTFP of the items mostly done by ready code (MiroTalk room, upload, live status,
# camera check, dataset import, STA trending paths), see docs/dec-61-fp-cocomo.md.
READY_UTFP = 28

# Size by analogy: cloc "code" lines of open-source code doing the same job (measured 2026-10-23).
NEW_MODULES = {  # name: (language, SLOC, analog)
    "Calibration page": ("JavaScript", 261, "WebGazer www/ calibration demo"),
    "Consent and result pages": ("JavaScript", 206, "WebGazer heatmap page (103) x 2 pages"),
    "Code view with code-block AOIs from the DOM": ("JavaScript", 150, "no analog found, team estimate"),
    "Backend: upload -> Python job -> report": ("JavaScript", 206, "MiroTalk Server.js rec endpoints"),
    "Gaze pipeline": ("Python", 484, "our DEC-45 code (170) + WebGazer ridge regression (314)"),
    "Fixations and AOI mapping": ("Python", 237, "EMIP-Toolkit AOI + I-DT"),
    "STA and classification": ("Python", 366, "SukruEraslan/sta STA_withToleranceLevel.py"),
    "Dataset import": ("Python", 225, "EMIP-Toolkit parsers"),
    "Model evaluation": ("Python", 290, "eyetracking_classification main.py"),
}
MIROTALK_SLOC = 826  # RoomClient.js RECORDING section + Server.js rec endpoints

# Language unit size (LOC per FP): QSM table (slide 41) for JavaScript; QSM has no
# Python, so Python from Jones (2017) Table 16.
LOC_PER_FP = {"JavaScript": 47.0, "Python": 53.33}

BASIC_ORGANIC = (2.4, 1.05, 2.5, 0.38)
JONES_BUSINESS = {"best": 0.41, "average": 0.43, "worst": 0.46}  # slide 49
HOURS_PER_PM = 152  # Boehm (1981)

TEAM_SIZE, WEEKS, HOURS_PER_WEEK = 4, 28, 8.5  # 8.5 h from the Sprint 1 plan (102 h / 4 / 3 weeks)


def loc_per_fp():
    total = sum(s for _, s, _ in NEW_MODULES.values())
    return sum(LOC_PER_FP[lang] * s / total for lang, s, _ in NEW_MODULES.values())


def basic_cocomo(kdsi):
    a, b, c, d = BASIC_ORGANIC
    mm = a * kdsi**b
    return mm, c * mm**d


def jones(atfp, exp):
    return atfp ** (3 * exp) / 27, atfp**exp  # effort PM, schedule months


def main():
    _, utfp, vaf, _ = function_points()
    lpf = loc_per_fp()
    print(f"LOC/FP (weighted by analogy share): {lpf:.2f}")
    for name, u in [("ready code counted", utfp), ("ready code not counted", utfp - READY_UTFP)]:
        atfp = u * vaf
        kdsi = atfp * lpf / 1000
        mm, tdev = basic_cocomo(kdsi)
        print(f"\n{name}: UTFP {u}, ATFP {atfp:.1f}, {kdsi:.2f} KDSI")
        print(f"  Basic COCOMO: {mm:.1f} PM, {mm * HOURS_PER_PM:.0f} h, {tdev:.1f} months")
        for label, e in JONES_BUSINESS.items():
            pm, months = jones(atfp, e)
            print(f"  Jones {label} ({e}): {pm:.1f} PM, {pm * HOURS_PER_PM:.0f} h, {months:.1f} months")

    new = sum(s for _, s, _ in NEW_MODULES.values())
    for name, sloc in [("MiroTalk counted", new + MIROTALK_SLOC), ("MiroTalk not counted", new)]:
        mm, tdev = basic_cocomo(sloc / 1000)
        print(f"\nAnalogy, {name}: {sloc} SLOC -> {mm:.1f} PM, {mm * HOURS_PER_PM:.0f} h, {tdev:.1f} months")

    hours = TEAM_SIZE * WEEKS * HOURS_PER_WEEK
    print(f"\nCapacity: {TEAM_SIZE} x {WEEKS} weeks x {HOURS_PER_WEEK} h = {hours:.0f} h = {hours / HOURS_PER_PM:.1f} PM")


if __name__ == "__main__":
    # Boehm organic example: 32 KDSI -> ~91 PM, ~14 months
    mm, tdev = basic_cocomo(32)
    assert 90 < mm < 92 and 13.5 < tdev < 14.5, (mm, tdev)
    # Slide 47 example: 350 ATFP x 128 LOC/FP (C) = 44.8 KDSI
    mm, tdev = basic_cocomo(350 * 128 / 1000)
    assert 130 < mm < 132 and 15.5 < tdev < 16.5, (mm, tdev)
    main()
