## 3 Software Estimation

Draft for DEC-19. All numbers come from [estimation.py](estimation.py) (`python3 docs/srs/estimation.py`). The design follows DEC-44: a MiroTalk SFU fork records the candidate's camera in the browser, and the analysis runs in Python.

Todo (when writing the Word report): enter the same inputs into the COCOMO II web tool (http://softwarecost.org/tools/COCOMO/), add a screenshot of the result and cite it as the estimation tool.

### 3.1 Method

1. Estimate the size (KSLOC) **by analogy**: for each module, we measured the code lines (`cloc`) of open-source code that does the same job.
2. Count only code we write or change. Libraries we only call (MediaPipe, L2CS-Net, NumPy) count 0. MiroTalk code we adapt is converted to equivalent lines with the COCOMO II reuse model [2].
3. Estimate effort and schedule with Basic COCOMO (organic) [1] and COCOMO II.2000 post-architecture [2].
4. Compare the estimates with the team's capacity.

### 3.2 Size

**New code**

| Module | Language | SLOC | Measured analog |
|---|---|---|---|
| Calibration page | JavaScript | 261 | WebGazer calibration demo [3] |
| Consent and result pages | JavaScript | 206 | WebGazer heatmap page (103) × 2 pages [3] |
| Code view with line AOIs from the DOM | JavaScript | 150 | No analog found, team estimate |
| Backend: upload → Python job → report | JavaScript | 206 | MiroTalk `Server.js` recording endpoints [7] |
| Gaze pipeline | Python | 484 | Our DEC-45 gaze code (170) + WebGazer ridge regression to screen (314) [3] |
| Fixations and AOI mapping | Python | 237 | EMIP-Toolkit AOI mapping and I-DT [4] |
| STA and classification | Python | 366 | Original STA implementation with tolerance level [5] |
| Dataset import | Python | 225 | EMIP-Toolkit dataset parsers [4] |
| Model evaluation | Python | 290 | Eye-tracking classifier training and evaluation script [6] |
| **Total new** | | **2,425** | |

**Adapted code (COCOMO II reuse model)**

MiroTalk SFU already records and uploads video. We adapt this code: the client "RECORDING" section of `RoomClient.js` and the `/recSync` endpoints in `Server.js`, **826 SLOC** [7].

| Parameter | Value | Reason |
|---|---|---|
| DM (design modified) | 20% | Recording moves to the candidate side and starts automatically |
| CM (code modified) | 30% | Upload target and file naming change |
| IM (integration) | 30% | Link to the Python pipeline |
| AA (assessment) | 4 | Some module test and evaluation |
| SU (understanding) | 40 | Low: `RoomClient.js` is a large single file |
| UNFM (unfamiliarity) | 0.8 | Mostly unfamiliar to the team |

- AAF = 0.4 × 20 + 0.3 × 30 + 0.3 × 30 = 26
- AAM = [AA + AAF × (1 + 0.02 × SU × UNFM)] / 100 = [4 + 26 × 1.64] / 100 = 0.466
- Equivalent SLOC = 826 × 0.466 = **385 ESLOC**

**Total size = 2,425 + 385 = 2,810 SLOC ≈ 2.81 KSLOC**

### 3.3 Basic COCOMO (organic)

The project is organic: a small team, a familiar environment, and no hard hardware or real-time constraints.

- Effort: E = 2.4 × 2.81^1.05 = **7.1 person-months (PM)**
- Duration: D = 2.5 × 7.1^0.38 = **5.3 months**
- Average staff: 7.1 / 5.3 = 1.3 full-time people

### 3.4 COCOMO II.2000 (post-architecture)

- Effort: PM = A × Size^E × ΠEM, with A = 2.94 and E = B + 0.01 × ΣSF, B = 0.91 [2]
- Schedule: TDEV = C × PM^(D + 0.2 × (E − B)), with C = 3.67 and D = 0.28 [2]

**Scale factors**

| Factor | Rating | Value | Reason |
|---|---|---|---|
| PREC (precedentedness) | Low | 4.96 | First gaze or STA product for the team |
| FLEX (development flexibility) | High | 2.03 | Supervisors set goals, not the process |
| RESL (architecture/risk resolution) | Low | 5.65 | Gaze accuracy risk is still open |
| TEAM (team cohesion) | High | 2.19 | Four classmates, weekly meetings |
| PMAT (process maturity) | Low | 6.24 | Student team, light process |
| **Sum** | | **21.07** | E = 0.91 + 0.2107 = **1.121** |

**Effort multipliers** (all others Nominal, 1.00)

| Driver | Rating | Value | Reason |
|---|---|---|---|
| RELY (required reliability) | Low | 0.92 | Research prototype, failure costs little |
| CPLX (product complexity) | High | 1.17 | Computer vision and sequence analysis |
| ACAP (analyst capability) | Low | 1.19 | Undergraduate analysts |
| PCAP (programmer capability) | Low | 1.15 | Undergraduate programmers |
| APEX (application experience) | Low | 1.10 | New domain for the team (about 6 months) |
| TOOL (software tools) | High | 0.90 | Modern IDEs, git, Linear |
| **Product (EAF)** | | **1.458** | |

- Effort: PM = 2.94 × 2.81^1.121 × 1.458 = **13.6 PM**
- Schedule: TDEV = 3.67 × 13.6^(0.28 + 0.2 × 0.211) = **8.5 months**
- Average staff: 1.6 full-time people

### 3.5 Comparison with team capacity

| | Effort | Hours (152 h/PM [2]) | Duration |
|---|---|---|---|
| Basic COCOMO | 7.1 PM | 1,080 h | 5.3 months |
| COCOMO II | 13.6 PM | 2,075 h | 8.5 months |
| **Team capacity** | **6.3 PM** | **952 h** | **7 months (28 weeks)** |

- Capacity: 4 students × 28 weeks × 8.5 h/week. 8.5 h/week comes from the Sprint 1 plan: 102 h of estimated tasks for 4 people in 3 weeks.
- Basic COCOMO is about 13% above the capacity. COCOMO II is about 2.2 times the capacity, mainly because it rates the team as inexperienced (ACAP, PCAP, APEX, PREC, PMAT).
- COCOMO II is our upper bound. To stay within capacity, we build the core path first (F2–F6), reuse existing code where possible (MiroTalk recording, EMIP-Toolkit parsers, the original STA code), and keep the research pipeline (F9, F10) as scripts.
- We compare these estimates with the hours we log per issue and update them at the end of each sprint.

### 3.6 Assumptions to defend

| Input | Value | Source / reason |
|---|---|---|
| Size | 2.81 KSLOC | `cloc` on analog open-source code per module, see 3.2; code view (150) is a team estimate |
| Libraries | 0 SLOC | We only call MediaPipe, L2CS-Net and NumPy, we do not change them |
| MiroTalk reuse | 826 → 385 ESLOC | COCOMO II reuse model [2] |
| Hours per PM | 152 | COCOMO II default [2] |
| Weekly hours per student | 8.5 | Sprint 1 plan |
| Project length | 28 weeks | Two semesters |
| Mode | Organic | Small team, no hard constraints |

### References

[1] Boehm, B. W. (1981). *Software engineering economics*. Prentice Hall.

[2] Center for Software Engineering, University of Southern California. (2000). *COCOMO II model definition manual* (Version 2.1).

[3] Papoutsaki, A., et al. (n.d.). *WebGazer.js* [Computer software]. GitHub. https://github.com/brownhci/WebGazer

[4] Al Madi, N., et al. (n.d.). *EMIP-Toolkit* [Computer software]. GitHub. https://github.com/nalmadi/EMIP-Toolkit

[5] Eraslan, S. (n.d.). *STA: Scanpath trend analysis* [Computer software]. GitHub. https://github.com/SukruEraslan/sta

[6] *eyetracking_classification* [Computer software]. (n.d.). GitHub. https://github.com/Gittingthehubbing/eyetracking_classification

[7] Pejic, M. (n.d.). *MiroTalk SFU* [Computer software]. GitHub. https://github.com/miroslavpejic85/mirotalksfu
