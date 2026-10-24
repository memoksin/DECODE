## Related Work: Public Eye-Tracking Datasets

Draft for DEC-33. Working notes, sources and open checks: [dec-33-dataset-karsilastirma.md](../dec-33-dataset-karsilastirma.md).

Todo (when writing the Word report): merge the reference numbers below into the report's list. Aljehane et al. [12] is Proposal [1], Peitek et al. [3] is Proposal [2], Eraslan et al. [13] is Proposal [5].

### Approach

DECODE uses eye-tracking data that was recorded while two groups of programmers, novice and experienced, read the same code. Scanpath Trend Analysis (STA) [13] builds one trending path for each group. A new programmer's scanpath on the same code is compared with both trending paths, and the programmer is classified into the group whose trending path is more similar. Trending paths depend on the code, so each code snippet needs its own pair of trending paths.

### Datasets

DECODE builds its novice and experienced trending paths from public data, so we reviewed public eye-tracking datasets on code reading. Following the supervisors' guidance, a dataset can be used, or merged with another, only if it has:

- the same programming language,
- novice / experienced labels,
- the same task (reading the same code).

Table 1 describes the datasets and Table 2 shows their access and our decision.

**Table 1.** Public eye-tracking datasets on code reading.

| Dataset | Language | Participants | Experience labels | Raw gaze (x, y, time) | Same code for all |
|---|---|---|---|---|---|
| EMIP [1] | Java (95.8%), Python, Scala | 216 | Self-rated expertise, years of programming | Yes | Yes: 2 programs |
| Corrected EMIP [2] | Java, Python | 159 | Via EMIP metadata | No, fixations mapped to tokens and lines | Yes: 2 programs |
| Peitek et al. [3] | Java | 12 novice, 19 experienced | Group labels | Yes | Yes: 10 programs |
| Busjahn et al. [4], [5] | Java, pseudocode | 14 novice, 6 expert | Group labels | n/r | Partly: 2 of 6 programs shared |
| McChesney & Bond [6] | Java | 30 (14 with dyslexia) | Self-rated, mostly "medium" | Yes | Yes: 3 programs |
| Abid et al. [7] | Java | 13 novice, 5 expert | Group labels | Processed (iTrace) | No: 63 methods |
| Fang et al. [8] | n/r | 49 lab, 10 remote | None | Yes | n/r |
| EyeTrans [9] | Java | 27 | None | Yes | No: 162 methods |
| Wallace et al. [10] | Java | 10 | None | n/r | No: 40 summaries |
| Al Madi & Khan [11] | English text, no code | 8 | n/r | Yes | n/a |

n/r = not reported, n/a = not applicable.

**Table 2.** Access, eye tracker and decision.

| Dataset | Licence | Eye tracker | Access | Decision |
|---|---|---|---|---|
| EMIP [1] | CC BY-NC-SA (paper), CC BY 4.0 (website) | SMI RED250, 250 Hz | OSF | Primary candidate |
| Corrected EMIP [2] | n/r | SMI RED250, 250 Hz | GitHub, OSF | Primary candidate |
| Peitek et al. [3] | CC BY-SA 4.0 | Tobii EyeX, 60 Hz | GitHub | Candidate |
| Busjahn et al. [4], [5] | n/r | SMI RED-m, 120 Hz | OSF | Candidate, to be verified |
| McChesney & Bond [6] | n/r | Tobii, 120 Hz | figshare | Supporting: unbalanced labels |
| Abid et al. [7] | CC BY-ND 4.0 | Tobii X60, 60 Hz | Zenodo | Supporting: summarisation task |
| Fang et al. [8] | n/r | Tobii Pro + WebGazer | IEEE DataPort (subscription) | Excluded: no labels; reference for webcam accuracy |
| EyeTrans [9] | CC BY 4.0 | Tobii Pro Fusion, 60 Hz | Zenodo | Excluded: no labels, summarisation task |
| Wallace et al. [10] | n/r | Tobii Pro Fusion, 120 Hz | Zenodo | Excluded: no labels, summarisation task |
| Al Madi & Khan [11] | n/r | EyeLink 1000 | GitHub | Excluded: not code reading |

### Findings

- **Language.** All candidate datasets use Java, so DECODE's first model is for Java.
- **Primary dataset.** EMIP [1] is the largest dataset that meets all three criteria: 216 participants read the same two Java programs, Rectangle and Vehicle, on the same eye tracker.
- **Shared code.** Peitek et al. [3] use the same Rectangle and Vehicle classes as EMIP, and most of their programs come from Busjahn et al. [4]. These datasets can therefore be merged on the same code.
- **Layout differs.** The same code is laid out differently in each dataset: in EMIP, short methods are written on one line. Line-level areas of interest (AOIs) do not match across datasets, but method or block AOIs do. This supports block-level AOIs, which also suit webcam gaze: Fang et al. found that webcam data captures patterns at the semantic level but struggles at the token level [8].
- **Eye trackers differ.** The datasets use eye trackers at 60, 120 and 250 Hz, so fixations will be computed again from raw gaze with one I-DT setting for all datasets.
- **Experience groups.** Peitek et al. and Busjahn et al. provide novice and experienced groups, and we use them as given. EMIP has no such labels, so we will build the groups from its questionnaire in one of two ways: the 17 participants who rated their expertise "high" and 17 randomly selected others, or participants with four or more years of programming and those with less, as in Aljehane et al. [12].
- **Licences.** Both EMIP licences are reported. Abid et al. [7] do not allow modified data to be redistributed, so we would only analyse it.

### References

[1] Bednarik, R., et al. (2020). EMIP: The eye movements in programming dataset. *Science of Computer Programming, 198*, 102520. https://www.emipws.org/dataset/

[2] Al Madi, N., Guarnera, D. T., Sharif, B., & Maletic, J. I. (2021). EMIP Toolkit: A Python library for customized post-processing of the eye movements in programming dataset. In *ACM Symposium on Eye Tracking Research and Applications (ETRA '21)*. https://doi.org/10.1145/3448018.3457425

[3] Peitek, N., Siegmund, J., & Apel, S. (2020). What drives the reading order of programmers? An eye tracking study. In *Proceedings of the 28th International Conference on Program Comprehension (ICPC '20)* (pp. 342–353). https://doi.org/10.1145/3387904.3389279

[4] Busjahn, T., et al. (2015). Eye movements in code reading: Relaxing the linear order. In *Proceedings of the 23rd International Conference on Program Comprehension (ICPC '15)*.

[5] Al Madi, N., Peterson, C. S., Sharif, B., & Maletic, J. I. (2021). From novice to expert: Analysis of token level effects in a longitudinal eye tracking study. In *Proceedings of the 29th International Conference on Program Comprehension (ICPC '21)*. Data: https://osf.io/t5je9/

[6] McChesney, I., & Bond, R. (2021). Eye tracking analysis of code layout, crowding and dyslexia: An open data set. In *ACM Symposium on Eye Tracking Research and Applications (ETRA '21)*. https://doi.org/10.1145/3448018.3457420

[7] Abid, N. J., Sharif, B., Dragan, N., Alrasheed, H., & Maletic, J. I. (2019). Developer reading behavior while summarizing Java methods: Size and context matters. In *Proceedings of the 41st International Conference on Software Engineering (ICSE '19)*. Data: https://doi.org/10.5281/zenodo.2550768

[8] Fang, Z., et al. (2026). Investigating the feasibility of conducting webcam-based eye-tracking studies in code comprehension. *IEEE Transactions on Software Engineering*. https://doi.org/10.1109/TSE.2026.3651615

[9] Zhang, Y., et al. (2024). EyeTrans: Merging human and machine attention for neural code summarization. *Proceedings of the ACM on Software Engineering, 1*(FSE), Article 6. Data: https://doi.org/10.5281/zenodo.10684985

[10] Wallace, R., et al. (n.d.). *Programmer visual attention during context-aware code summarization* [Preprint]. arXiv. https://arxiv.org/abs/2405.18573. Data: https://zenodo.org/records/14873017

[11] Al Madi, N., & Khan, J. (2018). Constructing semantic networks of comprehension from eye-movement during reading. In *2018 IEEE 12th International Conference on Semantic Computing (ICSC)*.

[12] Aljehane, S. D., Sharif, B., & Maletic, J. I. (2023). Studying developer eye movements to measure cognitive workload and visual effort for expertise assessment. *Proceedings of the ACM on Human-Computer Interaction, 7*(ETRA), Article 166. https://doi.org/10.1145/3591135

[13] Eraslan, S., Yesilada, Y., & Harper, S. (2016). Scanpath trend analysis on web pages: Clustering eye tracking scanpaths. *ACM Transactions on the Web, 10*(4), Article 20. https://doi.org/10.1145/2970818
