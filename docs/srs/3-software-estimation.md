## 3 Software Estimation

Draft for DEC-19 and DEC-61. All numbers come from [estimation.py](estimation.py) (`python3 docs/srs/estimation.py`). The FP count is in `experiments/dec-59/fp.py`. Only methods from CNG491 Lecture 3 are used.

### 3.1 Method

1. Count the size in **Function Points** (IFPUG): unadjusted FP (UTFP), then adjusted FP (ATFP = UTFP × VAF).
2. Convert FP to code size: LOC = ATFP × language unit size (LOC per FP).
3. Estimate effort and schedule with **Basic COCOMO** (organic) [1] and **Jones First-Order** estimation [2].
4. Cross-check with a second size method: **analogy** with measured open-source code.
5. Compare all estimates with the team's capacity.

Part of DECODE is ready code: MiroTalk SFU gives the video room, recording and upload; the original STA code builds the trending paths. We show two scenarios: the ready code counted and not counted.

### 3.2 Function Points

| Type | Items | UTFP |
|---|---|---|
| ILF | Interviewer, Session, Developer, Code stimulus + AOIs, Scanpath + result, Dataset, Trending path | 49 |
| EIF | Public dataset files, MiroTalk room | 10 |
| EI | Create/end session, Consent, Calibration, Upload + analyse, Import dataset, Build trending paths, Add code stimulus | 29 |
| EO | Classification report, Live status, Calibration feedback, Camera check, Model evaluation | 25 |
| EQ | Session list, Developers joined, Code view, Stimulus list | 12 |
| **Total** | | **125** |

- VAF = 0.65 + 0.01 × ΣGSC = 0.65 + 0.01 × 41 = **1.06**
- Ready code counted: ATFP = 125 × 1.06 = **132.5**
- Ready code not counted (MiroTalk room, upload + analyse, live status, camera check, dataset import, trending paths: 28 UTFP): ATFP = 97 × 1.06 = **102.8**

### 3.3 Code size

| Language | Share of code | LOC per FP | Source |
|---|---|---|---|
| JavaScript | 34% | 47 | QSM Function Point Languages Table [3] |
| Python | 66% | 53.33 | Jones (2017), Table 16 [4]; the QSM table has no Python value |
| **Weighted** | | **51.18** | |

The language shares come from the analogy in 3.5 (823 JavaScript and 1,602 Python SLOC). Jones gives Python the same value as Java, while scripting languages usually need fewer lines, so the Python size may be an upper bound.

| Scenario | ATFP | Size |
|---|---|---|
| Ready code counted | 132.5 | 6.78 KDSI |
| Ready code not counted | 102.8 | 5.26 KDSI |

### 3.4 Effort and schedule

**Basic COCOMO, organic** [1]: MM = 2.4 × KDSI^1.05, TDEV = 2.5 × MM^0.38. The project is organic: a small team, a familiar environment and no hard constraints.

**Jones First-Order** [2]: Effort = ATFP^(3 × exp) / 27 PM, Schedule = ATFP^exp months. We use the Business class exponents (best 0.41, average 0.43, worst 0.46).

| Method | Ready code counted | Ready code not counted |
|---|---|---|
| Basic COCOMO | 17.9 PM, 2,722 h, 7.5 months | 13.7 PM, 2,086 h, 6.8 months |
| Jones, best | 15.1 PM, 2,295 h, 7.4 months | 11.1 PM, 1,680 h, 6.7 months |
| Jones, average | 20.2 PM, 3,077 h, 8.2 months | 14.6 PM, 2,219 h, 7.3 months |
| Jones, worst | 31.4 PM, 4,777 h, 9.5 months | 22.1 PM, 3,366 h, 8.4 months |

Hours use 152 h per person-month [1].

### 3.5 Second method: analogy

For each module we measured the code lines (`cloc`) of open-source code that does the same job.

| Module | Language | SLOC | Measured analog |
|---|---|---|---|
| Calibration page | JavaScript | 261 | WebGazer calibration demo [5] |
| Consent and result pages | JavaScript | 206 | WebGazer heatmap page (103) × 2 pages [5] |
| Code view with code-block AOIs | JavaScript | 150 | No analog found, team estimate |
| Backend: upload → Python job → report | JavaScript | 206 | MiroTalk `Server.js` recording endpoints [8] |
| Gaze pipeline | Python | 484 | Our DEC-45 gaze code (170) + WebGazer ridge regression (314) [5] |
| Fixations and AOI mapping | Python | 237 | EMIP-Toolkit AOI mapping and I-DT [6] |
| STA and classification | Python | 366 | Original STA implementation with tolerance level [7] |
| Dataset import | Python | 225 | EMIP-Toolkit dataset parsers [6] |
| Model evaluation | Python | 290 | Eye-tracking classifier training script [9] |
| **Total new** | | **2,425** | |

The MiroTalk recording and upload code we change is 826 SLOC (`RoomClient.js` RECORDING section and `Server.js` recording endpoints) [8].

| Scenario | Size | Basic COCOMO |
|---|---|---|
| MiroTalk code counted | 3,251 SLOC | 8.3 PM, 1,258 h, 5.6 months |
| MiroTalk code not counted | 2,425 SLOC | 6.1 PM, 925 h, 5.0 months |

### 3.6 Comparison with team capacity

Capacity: 4 students × 28 weeks × 8.5 h/week = **952 h (6.3 PM)**. 8.5 h/week comes from the Sprint 1 plan: 102 h of estimated tasks for 4 people in 3 weeks.

| Estimate | Hours | × capacity |
|---|---|---|
| FP + Basic COCOMO, ready code counted | 2,722 h | 2.9 |
| FP + Basic COCOMO, ready code not counted | 2,086 h | 2.2 |
| FP + Jones average, ready code counted | 3,077 h | 3.2 |
| FP + Jones average, ready code not counted | 2,219 h | 2.3 |
| Analogy, MiroTalk counted | 1,258 h | 1.3 |
| Analogy, MiroTalk not counted | 925 h | 1.0 |

- The FP estimates are 2–3 times the capacity. FP counts what the system does, so it also counts the functions that ready code already gives us.
- The analogy counts only the code we write, so it is close to the capacity.
- To stay within capacity, we build the core path first (F2–F6), reuse existing code (MiroTalk recording, EMIP-Toolkit parsers, the original STA code), and keep the research pipeline (F9, F10) as scripts.
- We compare these estimates with the hours we log per issue at the end of each sprint.

### 3.7 Assumptions

| Input | Value | Source / reason |
|---|---|---|
| FP count | 125 UTFP, VAF 1.06 | IFPUG count by the team, one counter |
| LOC per FP, JavaScript | 47 | QSM table [3] |
| LOC per FP, Python | 53.33 | Jones (2017) [4]; not in the QSM table |
| Language shares | 34% / 66% | Analogy, 3.5 |
| Jones class | Business | DECODE is an information system: sessions, records, reports |
| Hours per PM | 152 | Boehm (1981) [1] |
| Weekly hours per student | 8.5 | Sprint 1 plan |
| Project length | 28 weeks | Two semesters |
| Mode | Organic | Small team, no hard constraints |

### References

[1] Boehm, B. W. (1981). *Software engineering economics*. Prentice Hall.

[2] CNG491 Lecture 3. (2026). *Software estimation*, slides 48–49: Jones's first-order estimation. METU NCC.

[3] QSM. (n.d.). *Function point languages table* (Version 5.0). https://www.qsm.com/resources/function-point-languages-table

[4] Jones, C. (2017). *Software economics and function point metrics: Thirty years of IFPUG progress* (Version 10.0, Appendix B, Table 16). Namcook Analytics. https://www.ifpug.org/wp-content/uploads/2017/04/IYSM.-Thirty-years-of-IFPUG.-Software-Economics-and-Function-Point-Metrics-Capers-Jones.pdf

[5] Papoutsaki, A., et al. (n.d.). *WebGazer.js* [Computer software]. GitHub. https://github.com/brownhci/WebGazer

[6] Al Madi, N., et al. (n.d.). *EMIP-Toolkit* [Computer software]. GitHub. https://github.com/nalmadi/EMIP-Toolkit

[7] Eraslan, S. (n.d.). *STA: Scanpath trend analysis* [Computer software]. GitHub. https://github.com/SukruEraslan/sta

[8] Pejic, M. (n.d.). *MiroTalk SFU* [Computer software]. GitHub. https://github.com/miroslavpejic85/mirotalksfu

[9] *eyetracking_classification* [Computer software]. (n.d.). GitHub. https://github.com/Gittingthehubbing/eyetracking_classification
