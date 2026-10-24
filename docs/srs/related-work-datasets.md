## Related Work: Public Eye-Tracking Datasets

Draft for DEC-33. Full comparison, sources and open checks: [dec-33-dataset-karsilastirma.md](../dec-33-dataset-karsilastirma.md).

Todo (when writing the Word report): merge the reference numbers below into the report's list. Aljehane et al. [3] is Proposal [1], Peitek et al. [2] is Proposal [2], Eraslan et al. [12] is Proposal [5].

### Approach

DECODE uses eye-tracking data that was recorded while two groups of programmers, novice and experienced, read the same code. Scanpath Trend Analysis (STA) [12] builds one trending path for each group. A new programmer's scanpath on the same code is compared with both trending paths, and the programmer is classified into the group whose trending path is more similar. Trending paths depend on the code, so each code snippet needs its own pair of trending paths.

### Datasets

We reviewed public eye-tracking datasets on code reading. Table 1 shows the two datasets DECODE will use and how each one separates the two groups.

**Table 1.** Datasets used by DECODE.

| Dataset | Language | Participants | Code read | Experience groups | Eye tracker | Access and licence |
|---|---|---|---|---|---|---|
| EMIP [1] | Java (95.8%), Python, Scala | 216 | 2 programs (Rectangle, Vehicle) | From the questionnaire (see below) | SMI RED250, 250 Hz | OSF; CC BY-NC-SA (paper), CC BY 4.0 (website) |
| Peitek et al. [2] | Java | 12 novice, 19 experienced | 10 programs, including Rectangle and Vehicle | Given by the authors: novice and experienced groups | Tobii EyeX, 60 Hz | GitHub; CC BY-SA 4.0 |

EMIP does not label participants as novice or experienced, so we will build the groups from its questionnaire in one of two ways:

- the 17 participants who rated their expertise "high", and 17 randomly selected other participants;
- participants with four or more years of programming, and those with less, as in Aljehane et al. [3].

EMIP has more participants, while Peitek et al. use more Java programs and already provide the two groups. Both datasets include the Rectangle and Vehicle classes.

The other datasets we reviewed were not selected:

- **Busjahn et al.** [4], [5]: novice and expert groups on partly shared programs. Access to the data is still being checked, so it may be added later.
- **McChesney & Bond** [6]: self-rated expertise, mostly "medium", so the groups are unbalanced.
- **Abid et al.** [7]: a code summarisation task on many different methods, not the same code for everyone.
- **Fang et al.** [8], **Zhang et al.** [9], **Wallace et al.** [10]: no experience labels.
- **Al Madi & Khan** [11]: natural-language text, not code.

### References

[1] Bednarik, R., et al. (2020). EMIP: The eye movements in programming dataset. *Science of Computer Programming, 198*, 102520. https://www.emipws.org/dataset/

[2] Peitek, N., Siegmund, J., & Apel, S. (2020). What drives the reading order of programmers? An eye tracking study. In *Proceedings of the 28th International Conference on Program Comprehension (ICPC '20)* (pp. 342–353). https://doi.org/10.1145/3387904.3389279

[3] Aljehane, S. D., Sharif, B., & Maletic, J. I. (2023). Studying developer eye movements to measure cognitive workload and visual effort for expertise assessment. *Proceedings of the ACM on Human-Computer Interaction, 7*(ETRA), Article 166. https://doi.org/10.1145/3591135

[4] Busjahn, T., et al. (2015). Eye movements in code reading: Relaxing the linear order. In *Proceedings of the 23rd International Conference on Program Comprehension (ICPC '15)*.

[5] Al Madi, N., Peterson, C. S., Sharif, B., & Maletic, J. I. (2021). From novice to expert: Analysis of token level effects in a longitudinal eye tracking study. In *Proceedings of the 29th International Conference on Program Comprehension (ICPC '21)*. Data: https://osf.io/t5je9/

[6] McChesney, I., & Bond, R. (2021). Eye tracking analysis of code layout, crowding and dyslexia: An open data set. In *ACM Symposium on Eye Tracking Research and Applications (ETRA '21)*. https://doi.org/10.1145/3448018.3457420

[7] Abid, N. J., Sharif, B., Dragan, N., Alrasheed, H., & Maletic, J. I. (2019). Developer reading behavior while summarizing Java methods: Size and context matters. In *Proceedings of the 41st International Conference on Software Engineering (ICSE '19)*. Data: https://doi.org/10.5281/zenodo.2550768

[8] Fang, Z., et al. (2026). Investigating the feasibility of conducting webcam-based eye-tracking studies in code comprehension. *IEEE Transactions on Software Engineering*. https://doi.org/10.1109/TSE.2026.3651615

[9] Zhang, Y., et al. (2024). EyeTrans: Merging human and machine attention for neural code summarization. *Proceedings of the ACM on Software Engineering, 1*(FSE), Article 6. Data: https://doi.org/10.5281/zenodo.10684985

[10] Wallace, R., et al. (n.d.). *Programmer visual attention during context-aware code summarization* [Preprint]. arXiv. https://arxiv.org/abs/2405.18573

[11] Al Madi, N., & Khan, J. (2018). Constructing semantic networks of comprehension from eye-movement during reading. In *2018 IEEE 12th International Conference on Semantic Computing (ICSC)*.

[12] Eraslan, S., Yesilada, Y., & Harper, S. (2016). Scanpath trend analysis on web pages: Clustering eye tracking scanpaths. *ACM Transactions on the Web, 10*(4), Article 20. https://doi.org/10.1145/2970818
