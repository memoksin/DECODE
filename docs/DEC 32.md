# **DEC 32:  Literature & Systems Review: Webcam-Based Gaze Tracking** 

1. **Investigating the Feasibility of Conducting Webcam-Based Eye-Tracking Studies in Code Comprehension (TSE, 2026)** 

   - **Language / Framework:** Python / Web-based client. 

   - **Algorithm:** Appearance-based CNN gaze estimation, fixation spatial dispersion filtering. 

   - **Dataset:** Code comprehension task cohort. 

   - **Features & Accuracy:** Correlates with infrared screen trackers on macro semantic reading patterns, but yields an angular error of 2.0°–3.5°, making token-level tracking unreliable. 

   - **Differentiation from DECODE:** Focuses strictly on hardware feasibility; contains no expertise classification model or STA aggregation. 

2. **WebGazer.js (Papoutsaki et al., IJCAI 2016)** 

   - **Language / Framework:** JavaScript (in-browser library). 

   - **Algorithm:** Pupil feature extraction combined with interaction-driven Ridge Regression. 

   - **Dataset:** Large-scale crowdsourced web benchmark. 

   - **Features & Accuracy:** Operates in client browsers with zero software installs, achieving 100–150 px average screen error. 

   - **Differentiation from DECODE:** Outputs raw coordinate streams (x, y) only; contains no code parsing, scanpath analysis, or expertise estimation. 

3. **LookAtChat (He et al., 2021)** 

   - **Language / Framework:** Node.js, WebRTC, WebGazer.js. 

   - **Algorithm:** Real-time gaze vector mapping to video tile targets. 

   - **Dataset:** Formative small-group study (5 participants). 

   - **Features & Accuracy:** Visualizes mutual eye contact and gaze awareness cues in video conferences. 

   - **Differentiation from DECODE:** Aimed at conversational awareness; lacks code comprehension tracking and candidate assessment functions. 

4. **Xobin EyeGazer (Commercial Product)** 

   - **Language / Framework:** Proprietary Web Platform. 

   - **Algorithm:** Facial landmark detection and off-screen gaze orientation tracking. 

   - **Features:** Real-time off-screen gaze flagging for remote online exam proctoring. 

   - **Differentiation from DECODE:** Strictly a proctoring/anti-cheating tool; does not assess candidate experience or code navigation. 

5. **RightPerson (Commercial Startup)** 

   - **Language / Framework:** Proprietary WebRTC Interview Platform. 

   - **Algorithm:** Multi-modal AI (voice injection detection, code plagiarism analysis, gaze tracking). 

   - **Features:** End-to-end interview integrity verification. 

   - **Differentiation from DECODE:** Focuses on anti-fraud detection rather than measuring candidate seniority through cognitive code reading dynamics. 

## **NASIL HAZIRLANDI VE YAPILMASI GEREKEN DUZENLEMELER:** 

PDF'te bazı  makalelerin altındaki matrislerde bazı kısımlar boştu veya soru işareti (?) ile bırakılmıştı. duzenlendi. srs e uygun sınıflandırmalar eklendi 

eklenmesi gerekem calısma olup olamdıgı kontrol edilecek 

raporun geneline uyum saglayıp saglamdıgı kontrol edilsin son asamada 

text yeniden yazılıp duızenlenmeye acık 

