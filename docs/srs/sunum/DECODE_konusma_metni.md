# DECODE – SRS Sunumu: Konuşma Metni (11 slayt)

Toplam: ~14 dk (2085 kelime, dakikada ~145) + soru-cevap.

Kişi başı: Sude ~3.3 dk · Mehmet ~3.2 dk · Burcu ~3.4 dk · İrem ~4.4 dk

| # | Slayt | Konuşmacı / süre |
|---|---|---|
| 1 | In a remote interview, you cannot see how a candidate reads code | Sude ~1.4 dk |
| 2 | No reviewed study combines all four | Sude ~1.8 dk |
| 3 | Two external systems feed DECODE | Mehmet ~0.7 dk, Burcu ~1.0 dk |
| 4 | A side panel inside the MiroTalk call | İrem ~1.0 dk |
| 5 | Nine functions, three that make or break it | İrem ~1.0 dk |
| 6 | Eight use cases, two critical | İrem ~1.3 dk |
| 7 | Usable by HR staff with no eye-tracking training | Burcu ~1.0 dk |
| 8 | Three numbers, each with a test | Mehmet ~1.2 dk |
| 9 | Six entities; the video is never stored | İrem ~1.1 dk |
| 10 | COCOMO II is 2.2× our capacity, so we cut scope | Mehmet ~1.3 dk |
| 11 | Sprint 1: goal mostly met, lessons taken | Burcu ~1.4 dk, Sude ~0.1 dk |

## Metin (İngilizce, sunumda okunacak)

### 1. In a remote interview, you cannot see how a candidate reads code

**Sude:** Good morning, we are the DECODE team: Burcu, İrem, Mehmet and me, Sude. DECODE stands for Developer Experience Classification via Eye-tracking Data Evaluation. Our starting point: in a remote technical interview, the interviewer sees the candidate’s answer but not how the candidate actually reads the code — and research shows novices and experienced programmers read the same code in different orders. So our aim is to estimate whether a candidate is a novice or an experienced programmer from the order of their gaze on the code, using only their ordinary webcam. Scope: we extend the open-source MiroTalk SFU to record the webcam in the candidate’s browser; we map gaze to code blocks, build the scanpath, and compare it with novice and experienced trending paths built with Scanpath Trend Analysis from public Java datasets. Nothing is recorded without consent, the video is deleted after analysis, and the result supports the interviewer — it never replaces their decision. STA has been used before to describe groups of programmers, and eye tracking has been used to separate novices from experts with machine learning — but to our knowledge we are the first to use STA itself as the classifier for programming experience.

### 2. No reviewed study combines all four

**Sude:** Our SRS compares eleven studies; here is the condensed version, grouped into three building blocks. Experience and eye movements in programming: Aljehane and Peitek show that gaze on code relates to experience, but only at group level. Al Madi et al. and Ahsan and Obaidellah 2026 do classify individuals, reaching 72 and up to 76 percent — but with feature-based machine learning that summarises gaze as counts and durations and throws away the order of reading. Scanpath Trend Analysis: Eraslan et al. turned STA into a classifier for autism detection with about 60 percent accuracy, and Ahsan and Obaidellah 2023 used STA on code, but only to describe groups by clustering, which failed when AOI counts differed between stimuli. Webcam feasibility: Fang et al. show webcams capture semantic reading patterns on code, but not token-level detail. The highlighted row is the gap: nobody combines individual classification, gaze order, code and a webcam. Why STA? We gain the reading order that feature-based models discard; an interpretable trending path that shows why a candidate was matched; no model to train, which matters because labelled datasets are small; and it is light enough for a report within a minute. Building one pair of paths per snippet also avoids the AOI-count problem. The risks: the earlier STA classifier reached only about 60 percent, one path per group hides variation inside the group, we are limited to dataset snippets in Java, and our paths come from infrared trackers while candidates use webcams. Whether order beats features has never been tested — so we do not assume it, we measure it.

### 3. Two external systems feed DECODE

**Mehmet:** Thanks, Sude. This is our context diagram: DECODE talks to exactly two external systems. On the left, MiroTalk. We first looked at Google Meet, but its Media API is closed to new projects and it lowers resolution on low bandwidth, so we chose the open-source MiroTalk SFU and fork it. The call runs in the browser with nothing to install, and the candidate’s webcam is recorded locally, before network encoding, at 720p and 30 fps or more, then uploaded after the call. Because MiroTalk is AGPL-3.0, our changes are open source, and we pin the fork to one upstream commit.

**Burcu:** On the right is the public eye-tracking dataset, the source of our trending paths. We researched in three tracks at the same time: video conferencing, datasets, and STA suitability. Sude and I reviewed ten public datasets against three rules: same language, novice/experienced labels, and the same code for every reader — because a trending path only makes sense for one snippet. Three are strong. EMIP is the largest, 216 readers, but only two programs, self-reported labels and token-level AOIs. Corrected EMIP has 159 readers with cleaned fixations. Peitek has fewer readers — 12 novices and 19 intermediates — but ten shared Java programs and code blocks already defined. So we start with Peitek to build the whole pipeline, then run it on EMIP and corrected EMIP and compare all three on held-out participants. Its limits: small groups, intermediate is not expert, and code linearity affects reading order strongly.

### 4. A side panel inside the MiroTalk call

**İrem:** Thank you, Burcu. DECODE appears as a side panel inside the MiroTalk call, and these four screens are the key steps. UI-1, Consent: before anything is recorded, the candidate sees what will be captured and can accept or decline — this is function F2. UI-2, Calibration: the candidate looks at nine points and one validation point so the gaze model fits their camera and screen — F3. UI-3, Live session: the interviewer follows the recording status while the candidate reads the code — F4. And UI-4, the Classification report: after the session, the interviewer sees each candidate’s predicted class, the confidence, and how reliable the result is, for example if calibration error was high — F8. Two screens are for the candidate and two for the interviewer, and the report is designed so that someone without eye-tracking training can read it.

### 5. Nine functions, three that make or break it

**İrem:** Our SRS defines nine product functions. They form two paths. During the call: F1 the interviewer sets up the session and picks the snippet, F2 consent, F3 calibration, F4 recording. After the call: F5 maps gaze to code, F6 builds the scanpath, F7 classifies, and F8 reports. F9, offline, stores the trending paths built with STA and feeds F7. Three of them are critical — highlighted in dark. F2, because eye and face images are personal data under GDPR and KVKK: without consent nothing is recorded, and the video is deleted after analysis. F5, because webcam error is two to four degrees while one line is half a degree — so we can only map gaze to code blocks; if this fails, nothing downstream works. And F7, the core of our idea: the candidate’s scanpath is compared with both trending paths of the same snippet, and the more similar group wins.

### 6. Eight use cases, two critical

**İrem:** Our use case diagram has three actors — the interviewer, the candidate, and MiroTalk as an external system — and eight use cases. The two critical ones are described in detail in the SRS. Run Analysis Session: the interviewer starts the analysis, the system asks for consent, the candidate calibrates and the system validates the error against a threshold, then the code is shown and the webcam is recorded while the candidate reads. When the interviewer ends it, the recording is uploaded, gaze is mapped to code blocks, the scanpath is compared with both trending paths, the result is stored, and the video is deleted. Alternative courses: if consent is declined, nothing is recorded; if the face is lost, the interviewer is warned and recalibration is offered. View Classification Report: the interviewer picks a session, sees candidates with class and confidence, and can drill into the similarity to each trending path and the calibration error. If that error is above the threshold, the result is clearly marked as unreliable. Give Consent, Calibrate Gaze, Read Code, Capture Video Streams and Analyze Gaze on Code are included in Run Analysis Session.

### 7. Usable by HR staff with no eye-tracking training

**Burcu:** Our usability requirements follow the three ISO dimensions: effectiveness, efficiency and satisfaction. Our users may be HR staff without programming or eye-tracking knowledge, so UR-01 says at least 90 percent of interviewers must complete the core task without help: pick a snippet, open a session, send the link and open the report. We will evaluate this with a task-based test including both technical and non-technical participants and count unaided completions. UR-02 is for the candidate: the nine-point calibration plus the validation point must take under 45 seconds, because a long calibration delays the interview and more head movement means worse gaze accuracy. We will log the time from calibration start to accepted validation in every session. UR-03: the classification report must reach a System Usability Scale score of at least 75 — above the commonly used average of 68 — measured with the SUS questionnaire right after participants read a sample report.

### 8. Three numbers, each with a test

**Mehmet:** We have three measurable performance requirements, each with a way to verify it. PR-01, webcam capture: at least 1280 by 720 at 30 frames per second, with 1080p recommended. This is not a guess — we measured it on two team members’ cameras: downscaling from 1080p to 720p adds about 1.6 degrees of gaze deviation on top of the model’s 2 to 4 degrees. At that level we can still map to code blocks, but not lines. We verify it by reading the actual resolution and frame rate of the camera track at session start and warning below the minimum. PR-02, network latency: under 200 milliseconds one-way through our SFU server. ITU-T G.114 says most applications are fine below 150 and recommends never exceeding 400, so 200 is our target in between. We verify it with WebRTC statistics during test interviews. PR-03: once the gaze data is available, the STA analysis and classification must produce the report within 60 seconds, even for 30 minutes of gaze data — verified by timing runs on our longest sessions.

### 9. Six entities; the video is never stored

**İrem:** Our logical data model uses a relational database with six entities, drawn in Chen notation. An Interviewer conducts many Sessions. A Session shows one or more Code Stimuli, and a stimulus can be used in many sessions, so that is many-to-many. Candidates attend a session. A Scanpath is the ordered sequence of AOIs of one reader on one stimulus — and the same Scanpath entity serves both sides: candidate scanpaths, linked through the RESULTS relationship that holds the predicted class and the similarity to the novice and the experienced trending path, and dataset scanpaths, which the Dataset contains together with their experience level. Some rules cannot be shown in the ERD, so we list them as integrity constraints: the class is either novice or experienced, similarities are between 0 and 1, and a candidate without consent has no scanpath or result. And one rule for privacy: the webcam video is never stored in the database; it is deleted after analysis.

### 10. COCOMO II is 2.2× our capacity, so we cut scope

**Mehmet:** For estimation we sized each module by analogy: for every module we found open-source code doing the same job and counted its lines with cloc. Libraries we only call, like MediaPipe or L2CS-Net, count as zero. That gives 2,425 new lines; plus 826 lines of MiroTalk recording code we adapt, which the COCOMO II reuse model converts to 385 equivalent lines — 2.81 KSLOC in total. Basic COCOMO in organic mode gives 7.1 person-months over 5.3 months, about 1,080 hours. COCOMO II.2000 gives 13.6 person-months over 8.5 months — about 2,075 hours — mainly because it rates us as an inexperienced team on analyst, programmer and domain experience. We cross-checked it with the COCOMO II web tool and got the same result. Our capacity is four students, 28 weeks, 8.5 hours a week — 952 hours. So Basic COCOMO is 13 percent above capacity and COCOMO II is 2.2 times capacity. We take COCOMO II as the upper bound and respond by building the core path F1 to F6 first, reusing existing code, keeping the research function F9 as scripts, and comparing logged hours with the estimate every sprint.

### 11. Sprint 1: goal mostly met, lessons taken

**Burcu:** This is the evidence from Sprint 1, 7 to 27 October. We closed 36 tasks, about 94 hours. The sprint started with 104 hours of work, 15 hours were added after the second supervisor meeting, and 24 hours moved to Sprint 2: two literature scans, the gaze model test and the dataset merging plan. What we delivered: all SRS sections, the related work table of 11 studies, the comparison of 10 datasets, the switch from Google Meet to MiroTalk SFU, and the measured 720p minimum. We are also honest about what went wrong: the platform changed in the middle of the sprint so parts of the SRS were rewritten, tasks were added late, the burndown stayed above the ideal line because most tasks were closed in the last two days, and the load was not balanced. For Sprint 2, the board status is our timer, every task gets an estimate when it is created, tasks are split to at most three hours, and we check load in a mid-sprint meeting. Sprint 2 also starts the technical work: testing MediaPipe and L2CS-Net on the same recordings, and importing Peitek’s dataset to build the first trending paths, then EMIP and corrected EMIP.

**Sude:** That concludes our presentation. Thank you for listening; we are happy to take your questions.

## Soru-cevap hazırlığı

**Why STA instead of a trained classifier (Random Forest etc.)?** — STA uses reading order, is interpretable, and needs no training set beyond the trending paths; the labelled datasets are small. We do not claim it beats ML; we will compare on held-out participants.

**~60% accuracy in Eraslan et al. 2020 — isn't that too low?** — That is why the output is supplementary, never a hiring decision. Our contribution is testing whether reading order on code carries experience information; a negative result is still a result.

**Why start with Peitek if the SRS calls EMIP the primary candidate?** — Peitek has code blocks already defined and 10 shared snippets, so we can build and debug the whole pipeline first. EMIP stays the main dataset for scale (207 usable readers); we will run all three and compare.

**Peitek has novice vs. intermediate, not expert.** — Correct; we report this as a label limitation and use EMIP (4-year split, 101 vs. 90) to test the novice/experienced boundary.

**Infrared paths vs. webcam scanpaths — is that comparable?** — It is an explicit assumption (SRS 1.4.5). Block-level AOIs reduce the mismatch; we will test it with degraded (noise-added) dataset scanpaths and with our own webcam recordings.

**What if the candidate reads code from another window?** — Assumption in the SRS; the code view is part of DECODE and face loss triggers a warning and recalibration.

**Privacy / KVKK?** — Explicit consent before recording, candidate can decline, video deleted after analysis, never stored in the database.

**COCOMO II says 2.2× capacity — can you finish?** — Core path F1–F6 first, heavy reuse (MiroTalk recording, EMIP-Toolkit, original STA code), F9 as scripts, re-estimate every sprint.
