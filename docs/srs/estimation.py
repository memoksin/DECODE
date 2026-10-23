"""SRS 3 Software Estimation (DEC-19). Run: python3 docs/srs/estimation.py"""

# Size by analogy: cloc "code" lines of open-source code doing the same job (measured 2026-10-23).
# Libraries we only call (MediaPipe, L2CS-Net, NumPy) count 0.
NEW_MODULES = {  # name: (language, SLOC, analog)
    "Calibration page": ("JavaScript", 261, "WebGazer www/ calibration demo"),
    "Consent and result pages": ("JavaScript", 206, "WebGazer heatmap page (103) x 2 pages"),
    "Gaze pipeline": ("Python", 484, "our DEC-45 code (170) + WebGazer ridge regression (314)"),
    "Fixations and AOI mapping": ("Python", 237, "EMIP-Toolkit AOI + I-DT"),
    "STA and classification": ("Python", 366, "SukruEraslan/sta STA_withToleranceLevel.py"),
    "Dataset import": ("Python", 225, "EMIP-Toolkit parsers"),
    "Model evaluation": ("Python", 290, "eyetracking_classification main.py"),
}

# COCOMO II reuse model: MiroTalk SFU recording + recSync upload code we adapt
ADAPTED_SLOC = 826  # RoomClient.js RECORDING section + Server.js rec endpoints
DM, CM, IM = 20, 30, 30  # % design / code modified, % integration effort
AA = 4      # some module test and evaluation
SU = 40     # Low: RoomClient.js is a 10k-line monolith
UNFM = 0.8  # mostly unfamiliar

BASIC_ORGANIC = (2.4, 1.05, 2.5, 0.38)

# COCOMO II.2000 post-architecture
A, B, C, D = 2.94, 0.91, 3.67, 0.28
SCALE_FACTORS = {  # name: (rating, value)
    "PREC": ("Low", 4.96),   # first gaze/STA product for the team
    "FLEX": ("High", 2.03),  # supervisors set goals, not process
    "RESL": ("Low", 5.65),   # gaze accuracy risk still open
    "TEAM": ("High", 2.19),  # 4 classmates, weekly meetings
    "PMAT": ("Low", 6.24),   # student team, light process
}
EFFORT_MULTIPLIERS = {  # name: (rating, value); unlisted = Nominal (1.00)
    "RELY": ("Low", 0.92),   # research prototype, low cost of failure
    "CPLX": ("High", 1.17),  # computer vision + sequence analysis
    "ACAP": ("Low", 1.19),   # undergraduate analysts
    "PCAP": ("Low", 1.15),   # undergraduate programmers
    "APEX": ("Low", 1.10),   # new domain for the team
    "TOOL": ("High", 0.90),  # modern IDEs, git, Linear
}
HOURS_PER_PM = 152

TEAM_SIZE = 4
WEEKS = 28  # CNG 491 + CNG 492, two semesters
HOURS_PER_WEEK = 8.5  # per student, from the Sprint 1 plan (102 h / 4 people / 3 weeks)


def equivalent_sloc(asloc):
    aaf = 0.4 * DM + 0.3 * CM + 0.3 * IM
    aam = (AA + aaf * (1 + 0.02 * SU * UNFM)) / 100 if aaf <= 50 else (AA + aaf + SU * UNFM) / 100
    return asloc * aam


def kloc_total():
    return (sum(s for _, s, _ in NEW_MODULES.values()) + equivalent_sloc(ADAPTED_SLOC)) / 1000


def basic_cocomo(kloc):
    a, b, c, d = BASIC_ORGANIC
    pm = a * kloc**b
    return pm, c * pm**d


def cocomo2(kloc):
    e = B + 0.01 * sum(v for _, v in SCALE_FACTORS.values())
    eaf = 1.0
    for _, v in EFFORT_MULTIPLIERS.values():
        eaf *= v
    pm = A * kloc**e * eaf
    return e, eaf, pm, C * pm ** (D + 0.2 * (e - B))


def main():
    new = sum(s for _, s, _ in NEW_MODULES.values())
    esloc = equivalent_sloc(ADAPTED_SLOC)
    kloc = kloc_total()
    print(f"Size: new {new} SLOC + adapted {ADAPTED_SLOC} -> {esloc:.0f} ESLOC = {kloc:.2f} KSLOC")
    pm, months = basic_cocomo(kloc)
    print(f"Basic COCOMO organic: {pm:.1f} PM, {months:.1f} months, {pm / months:.1f} people, {pm * HOURS_PER_PM:.0f} h")
    e, eaf, pm, months = cocomo2(kloc)
    print(f"COCOMO II: E={e:.4f}, EAF={eaf:.3f}, {pm:.1f} PM, {months:.1f} months, {pm / months:.1f} people, {pm * HOURS_PER_PM:.0f} h")
    hours = TEAM_SIZE * WEEKS * HOURS_PER_WEEK
    print(f"Capacity: {TEAM_SIZE} x {WEEKS} weeks x {HOURS_PER_WEEK} h = {hours:.0f} h = {hours / HOURS_PER_PM:.1f} PM")


if __name__ == "__main__":
    # Sanity check against Boehm's organic example: 32 KLOC -> ~91 PM, ~14 months
    pm, months = basic_cocomo(32)
    assert 90 < pm < 92 and 13.5 < months < 14.5, (pm, months)
    # COCOMO II manual example: 100 KSLOC, E=1.15 -> 586.6 PM, 29.7 months
    pm = A * 100**1.15
    assert abs(pm - 586.6) < 0.5 and abs(C * pm ** (D + 0.2 * (1.15 - B)) - 29.7) < 0.1
    main()
