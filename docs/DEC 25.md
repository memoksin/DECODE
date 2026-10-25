# **DEC 25: SRS 2.3 Usability & 2.4 Performance Requirements** 

2.3 Usability Requirements 

   - **UR-01 (Calibration Duration):** The candidate's 9-point gaze calibration process shall be completed in under 45 seconds to avoid elevating candidate anxiety and delaying the interview session. 

   - **UR-02 (Interviewer Report Usability):** The candidate scanpath and code-comprehension analytics report shall achieve a System Usability Scale (SUS) score of at least 75 (Grade B+) so technical recruiters can interpret findings without specialized eye-tracking training. 

   - **UR-03 (Task Completion Rate):** Technical interviewers shall achieve an initial task completion rate of at least 90% when configuring code snippets and launching analysis sessions to prevent workflow disruptions during live interviews. 

- 2.4 Performance Requirements 

   - **PR-01 (Gaze Extraction Frame Rate):** The client-side webcam frame capture and gaze inference pipeline shall sustain at least 25 FPS with an end-to-end frame processing latency not exceeding 40 ms, as typical human saccades last 30–80 ms and lower frame rates risk dropping fixation boundaries (Papoutsaki et al., 2016). 

   - **PR-02 (WebRTC Network Latency):** Media streams routed via the MiroTalk SFU server shall maintain a one-way end-to-end network latency under 200 ms to avoid verbal overlap and interactive communication degradation during live sessions (ITU-T G.114 standard). 

   - **PR-03 (Model Inference & Report Generation Time):** The STA processing and experience classification pipeline shall generate the final diagnostic evaluation report within 5 seconds of task completion to ensure timely decision support for the interviewer before proceeding to subsequent questions (Al Madi et al., 2021). 

## **NASIL HAZIRLANDI VE YAPILMASI GEREKEN DUZENLEMELER:** 

raporun tamamı ile uyusup uyusmadıgı srs ile kontrol edilmesi gerekiyor. diger req lerle uyumu. text duzenlenmeli 

