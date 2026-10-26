# SRS 2.5 — Taslak (DEC-26)

Durum: **yedek alternatif**, SRS'te [sade sürüm](../srs-2.5-sade-taslak.md) kullanılıyor. Kaynak: [srs-1.4.2-2.2-taslak.md](../srs-1.4.2-2.2-taslak.md).

Diyagram kaynağı: [erd.drawio](erd.drawio) (Chen notasyonu)

### Açık sorular

- Researcher kaldırıldı (2.2 ile aynı karar). Model verisi (Dataset, Participant, ClassificationModel, TrendingPath) sınıflandırma için gerekli olduğu için kaldı. EvaluationReport kalsın mı?
- Candidate kaydı tutulacak mı, yoksa oturum anonim mi? (F8)

---

## 2.5 Logical Database Requirements

The system uses a relational database to store sessions, classification results and the STA model. Raw webcam and screen video is never stored (F8).

### Entity Relationship Diagram

![ERD](erd.drawio.png)

### Entity Summary

| Entity | Purpose | Attributes | Relationships |
|--------|---------|------------|---------------|
| Interviewer | User who opens and runs analysis sessions. | <u>InterviewerID</u>, name, email | CONDUCTS Session (1:N). |
| Candidate | Person whose code reading is analysed. Has no account. | <u>CandidateID</u>, name | ATTENDS Session (1:N). |
| Session | One analysis session in a meeting. | <u>SessionID</u>, startTime, endTime, consentGiven | Conducted by Interviewer (N:1), attended by Candidate (N:1), SHOWS CodeStimulus (N:1), HAS Calibration (1:N), PRODUCES Scanpath (1:1), YIELDS ClassificationResult (1:1). |
| Calibration | Weak entity. One calibration attempt in a session. | <u>SessionID</u> + attemptNo (partial key), error, accepted | Identified by Session through HAS (N:1). |
| CodeStimulus | Source code shown to the reader. | <u>StimulusID</u>, title, language | CONTAINS AOI (1:N), has TrendingPath FOR it (1:N), shown in Session (1:N). |
| AOI | Weak entity. One code line of a stimulus. | <u>StimulusID</u> + lineNo (partial key) | Identified by CodeStimulus through CONTAINS (N:1), fixated in Scanpath through FIXATES_ON (M:N). |
| Scanpath | Ordered sequence of fixations on AOIs. | <u>ScanpathID</u>, length | FIXATES_ON AOI (M:N, with order and duration), produced by Session (1:1) or recorded for Participant (N:1). |
| ClassificationResult | Predicted experience level of a candidate. | <u>ResultID</u>, predictedClass, noviceSim, expertSim, {warnings} | Yielded by Session (1:1), USES ClassificationModel (N:1). |
| ClassificationModel | One version of the STA-based model. | <u>ModelID</u>, version | DEFINES TrendingPath (1:N), TRAINED_ON Dataset (N:1), used by ClassificationResult (1:N), evaluated by EvaluationReport (1:N). |
| TrendingPath | Representative AOI path of one group for one stimulus. | <u>TrendingPathID</u>, group, aoiSequence | Defined by ClassificationModel (N:1), FOR CodeStimulus (N:1). |
| Dataset | Public labelled eye-tracking dataset. | <u>DatasetID</u>, name, source | INCLUDES Participant (1:N), used to train ClassificationModel (1:N). |
| Participant | Weak entity. One programmer in a dataset. | <u>DatasetID</u> + participantNo (partial key), experienceLabel | Identified by Dataset through INCLUDES (N:1), RECORDS Scanpath (1:N). |
| EvaluationReport | Accuracy results of a model version. | <u>ReportID</u>, accuracy, precision, recall | EVALUATES ClassificationModel (N:1). |

### Integrity Constraints

**Entity integrity**
- Every primary key is unique and not null.
- A weak entity's key is its owner's key plus its partial key: Session + attemptNo, CodeStimulus + lineNo, Dataset + participantNo.

**Referential integrity**
- Every foreign key refers to an existing row.
- Deleting an owner deletes its weak entities (cascade). For example, deleting a Session deletes its Calibration rows.

**Domain constraints**
- predictedClass, experienceLabel, group ∈ {novice, experienced}.
- noviceSim, expertSim, accuracy, precision, recall ∈ [0, 1].
- duration > 0 and endTime > startTime.

**Business rules**
- If consentGiven is false, the Session has no Calibration, Scanpath or ClassificationResult (Run Analysis Session, alternative flow 2a).
- Each ClassificationModel has exactly two TrendingPaths per CodeStimulus: one novice, one experienced.
- A Session SHOWS exactly one CodeStimulus, chosen in Open Session. That stimulus must have trending paths in the model the result uses.
- All AOIs in a session's Scanpath belong to the CodeStimulus the Session SHOWS.
- A Scanpath belongs to exactly one Session or exactly one Participant, never both.
- All AOIs in one Scanpath belong to the same CodeStimulus.

### Assumptions

- The code shown in an interview is one of the dataset's code stimuli. STA comparison is only meaningful on the same code.
- AOIs are at line level (see the open question in 2.2).
- Raw video is not stored, so there is no video entity.
