# DECODE: Developer Experience Classification via Eye-tracking Data Evaluation

**Type:** Research-based Development Project

## Description, Aims & Objectives

The literature has explored the effects of programmers' experience levels on eye-tracking data [1, 2]. Eye-tracking can provide valuable insights into how programmers read and understand source code, and these insights can identify potential difficulties and support targeted interventions. Previous work has used machine learning to predict programmer experience [3]. For example, [3] shows that binary classification of expertise with machine learning yields better results than classifying expertise into three levels (high, average, and low).

Scanpath Trend Analysis (STA) has been used to analyse eye-movement sequences (i.e. scanpaths) and observe differences between experienced and novice programmers [4]. STA analyses groups of scanpaths to identify a representative path, called a trending path, that represents where programmers look while reading code and how their visual attention moves across different areas of interest [5]. However, the literature has not yet used STA to predict programmer experience.

This project aims to use STA to create trending paths for both novice and experienced programmers. These trending paths will describe how each group reads source code. The scanpath of an unknown programmer will then be compared with the trending paths of both groups. If the programmer's scanpath is more similar to the trending path of experienced programmers, the programmer will be classified as experienced; otherwise, the programmer will be classified as novice. This approach has already been used for the classification of groups, for example, people with autism and a control group [6].

To use this user modelling, this project aims to develop an eye-tracking-based approach to classify users' experience in programming. More specifically, the project aims to develop an extension for a videoconferencing tool that uses the generated STA model. This extension will capture video streams during programming-related activities and process them to identify where programmers look while reading source code and in what sequence. These gaze sequences will be used to create individual scanpaths, which will then be compared with the STA-based trending paths to predict the programmer's level of experience.

By combining STA with eye-tracking data measured through videoconferencing, this project aims to provide a practical method for estimating programmer experience remotely. This could support technical interviews by offering additional insights into how candidates read and interpret source code.

## Milestones

1. Review the literature on related work that classifies developers based on their experience;
2. Search for available public eye-tracking datasets;
3. Generate individual developers' scanpaths from the selected eye-tracking data;
4. Apply Scanpath Trend Analysis (STA) to developers' individual scanpaths to identify the trending paths of novice and experienced developers;
5. Research how to analyse video streams to determine where people look and relate these gaze points to the lines of code they fixate on;
6. Research how to extract video streams from the videoconferencing tool;
7. Develop an extension for a videoconferencing tool that extracts video streams, processes them to determine where people look on the source code, generates scanpaths, and checks whether each scanpath is more similar to the trending paths of experienced or novice programmers for classification;
8. Evaluate and validate the extension with different techniques.

## Supervisors

- **Supervisor:** Yeliz Yesilada
- **Co-supervisor:** Sukru Eraslan

## Technical Requirements

This project requires skills in analysis and development, programming, and statistical analysis, as well as an interest in AI models, image processing, computer vision, and human-computer interaction, particularly eye tracking.

## References

1. Salwa D. Aljehane, Bonita Sharif, and Jonathan I. Maletic. 2023. Studying Developer Eye Movements to Measure Cognitive Workload and Visual Effort for Expertise Assessment. *Proc. ACM Hum.-Comput. Interact.* 7, ETRA, Article 166 (May 2023), 18 pages. <https://doi.org/10.1145/3591135>
2. Norman Peitek, Janet Siegmund, and Sven Apel. 2020. What Drives the Reading Order of Programmers? An Eye Tracking Study. In *Proceedings of the 28th International Conference on Program Comprehension (ICPC '20)*. Association for Computing Machinery, New York, NY, USA, 342–353. <https://doi.org/10.1145/3387904.3389279>
3. Zubair Ahsan and Unaizah Obaidellah. 2025. Eye-Tracking Indicators of Novice Programmers' Proficiency: A Machine Learning Approach. *ACM Trans. Comput. Educ.* 26, 1, Article 12 (March 2026), 24 pages. <https://doi.org/10.1145/3773898>
4. Zubair Ahsan and Unaizah Obaidellah. 2023. Is Clustering Novice Programmers Possible? Investigating Scanpath Trend Analysis in Programming Tasks. In *Proceedings of the 2023 Symposium on Eye Tracking Research and Applications (ETRA '23)*. Association for Computing Machinery, New York, NY, USA, Article 87, 1–7. <https://doi.org/10.1145/3588015.3589193>
5. Sukru Eraslan, Yeliz Yesilada, and Simon Harper. 2016. Scanpath Trend Analysis on Web Pages: Clustering Eye Tracking Scanpaths. *ACM Trans. Web* 10, 4, Article 20 (December 2016), 35 pages. <https://doi.org/10.1145/2970818>
6. Sukru Eraslan, Yeliz Yesilada, Victoria Yaneva, and Simon Harper. 2020. Autism detection based on eye movement sequences on the web: a scanpath trend analysis approach. In *Proceedings of the 17th International Web for All Conference (W4A '20)*. Association for Computing Machinery, New York, NY, USA, Article 11, 1–10. <https://doi.org/10.1145/3371300.3383340>
