# SDD 2 Glossary and 4 References (DEC-80)

Draft for the SDD. Terms are the ones used in the SDD text and diagrams. Definitions and sources are taken from the SRS 1.5 Definitions and 4 References so the two reports match. Project-specific terms cite "This report".

## 2 Glossary

| Term | Definition | Source (citation) |
|---|---|---|
| Area of Interest (AOI) | A region of the displayed code that groups gaze points. Gaze points are mapped to AOIs to form a scanpath. | Busjahn et al. (2015) |
| Calibration | A short step in which the developer looks at known points on the screen, so that the gaze model fits their camera and screen setup. | This report (Activity Diagram 1) |
| Developer | The person being interviewed, who reads code while the webcam is recorded. Shown as "Candidate" in the diagrams. | This report |
| Experienced developer | A developer with substantial programming experience, used as the second classification label in DECODE's binary experience model. | Al Madi, Peterson, et al. (2021) |
| Fixation | A state where the eye remains relatively stationary over a visual coordinate for 100-300 ms, allowing the visual system to acquire information. | Al Madi, Guarnera, et al. (2021) |
| Gaze point | An estimated position on the screen where the developer is looking at one moment. | This report |
| Interviewer | The person who runs the interview. The interviewer may be an HR specialist or an engineer. | This report |
| MiroTalk SFU | An open-source videoconferencing platform based on an SFU. DECODE runs its own fork of it for the interview. | Pejic (n.d.) |
| Novice developer | A developer with limited programming experience, used as one of the two classification labels in DECODE's binary experience model. | Al Madi, Peterson, et al. (2021) |
| Scanpath | The spatial and temporal sequence of alternating fixations and saccades across a visual stimulus (here, the displayed code). | Eraslan et al. (2016) |
| Scanpath Trend Analysis (STA) | An algorithmic method that aggregates individual scanpaths into a single representative sequence (trending path) for a group of participants. | Eraslan et al. (2016) |
| Selective Forwarding Unit (SFU) | A WebRTC media server architecture that receives each participant's streams and forwards them to the other participants without mixing them. | Westerlund & Wenger (2015) |
| Trending path | The representative scanpath produced by STA for a given group (novice or experienced developers), used as a reference for comparison. | Eraslan et al. (2016) |
| Webcam-based eye tracking | A gaze estimation approach that infers eye position from standard RGB camera input using computer vision models, without specialised hardware. | Papoutsaki et al. (2016) |

## 4 References

Ahsan, Z., & Obaidellah, U. (2023). Is clustering novice programmers possible? Investigating scanpath trend analysis in programming tasks. In *Proceedings of the 2023 Symposium on Eye Tracking Research and Applications (ETRA '23)* (Article 87, pp. 1-7). Association for Computing Machinery. https://doi.org/10.1145/3588015.3589193

Al Madi, N., Guarnera, D. T., Sharif, B., & Maletic, J. I. (2021). EMIP Toolkit: A Python library for customized post-processing of the eye movements in programming dataset. In *ACM Symposium on Eye Tracking Research and Applications (ETRA '21)*. https://doi.org/10.1145/3448018.3457425

Al Madi, N., Peterson, C. S., Sharif, B., & Maletic, J. I. (2021). From novice to expert: Analysis of token level effects in a longitudinal eye tracking study. In *Proceedings of the 29th International Conference on Program Comprehension (ICPC '21)*. IEEE. https://doi.org/10.1109/ICPC52881.2021.00025

Busjahn, T., Bednarik, R., Begel, A., Crosby, M., Paterson, J. H., Schulte, C., Sharif, B., & Tamm, S. (2015). Eye movements in code reading: Relaxing the linear order. In *Proceedings of the 23rd International Conference on Program Comprehension (ICPC '15)* (pp. 255-265). IEEE. https://doi.org/10.1109/ICPC.2015.36

Eraslan, S., Yesilada, Y., & Harper, S. (2016). Scanpath trend analysis on web pages: Clustering eye tracking scanpaths. *ACM Transactions on the Web, 10*(4), Article 20. https://doi.org/10.1145/2970818

Kruchten, P. B. (1995). The 4+1 view model of architecture. *IEEE Software, 12*(6), 42-50. https://doi.org/10.1109/52.469759

Papoutsaki, A., Sangkloy, P., Laskey, J., Daskalova, N., Huang, J., & Hays, J. (2016). WebGazer: Scalable webcam eye tracking using user interactions. In *Proceedings of the 25th International Joint Conference on Artificial Intelligence (IJCAI '16)* (pp. 3839-3845). AAAI Press. https://dl.acm.org/doi/10.5555/3061053.3061156

Pejic, M. (n.d.). *MiroTalk SFU* [Computer software]. GitHub. https://github.com/miroslavpejic85/mirotalksfu

Westerlund, M., & Wenger, S. (2015). *RTP topologies* (RFC 7667). Internet Engineering Task Force. https://doi.org/10.17487/RFC7667

## Notes for the team (not for the SDD)

- Every in-text citation in the SDD text is in the list: Ahsan & Obaidellah (2023) and Kruchten (1995) from the Summary and Architectural Views, and the six sources from the Glossary. If another section (diagrams, rationale) cites more sources, add them here in alphabetical order.
- The Glossary avoids describing AOIs as lines or blocks (Mehmet's 26 Nov message, DEC-54).
- "Developer" is shown as "Candidate" in the diagrams (team decision, 26 Nov 2026). The note in the Developer row keeps the two terms consistent. Remove it if the team does not want it.
- The two Al Madi 2021 papers are told apart in the text as "Al Madi, Guarnera, et al. (2021)" and "Al Madi, Peterson, et al. (2021)", as in the SRS.
