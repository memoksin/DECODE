# **DEC 43** 

# **Table 6.1: Video Conferencing Platform Comparison** 

|**Criterion**|**MiroTalk SFU**|**Jitsi Meet**|**Apache**<br>**OpenMeetings**|**Zoom**<br>**(Reference)**|
|---|---|---|---|---|
|License & Cost|AGPL v3 (Open<br>source, free<br>self-hosting)|Apache 2.0<br>(Open source,<br>free self-hosting)|Apache 2.0<br>(Open source,<br>free self-hosting)|Proprietary<br>(Requires paid<br>Pro/Business<br>plans; API/SDK<br>usage fees)|
|API Openness|Yes (REST API,<br>WebSocket<br>signaling, JWT<br>validation)|Yes (Jitsi Meet<br>External API,<br>lib-jitsi-meet)|Yes<br>(REST/SOAP<br>API)|Yes (Zoom<br>Video SDK /<br>REST API,<br>strictly metered)|
|Extensibility|High (Node.js &<br>Mediasoup<br>modular<br>codebase;<br>unopinionated<br>frontend)|Medium/Difficult<br>(Complex<br>monolithic base;<br>multi-layered<br>React wrapper)|Low (Legacy<br>Java stack;<br>cumbersome<br>client-side<br>integration)|Low<br>(Sandboxed<br>Zoom Apps;<br>restricted<br>execution<br>environment)|
|Raw Video<br>Access|Direct<br>(Client-side<br>/recSync capture<br>and<br>uncompressed<br>canvas buffer<br>access)|Possible<br>(TRACK_ADDE<br>D via<br>lib-jitsi-meet,<br>requires<br>significant<br>adaptation)|Complex (Relies<br>on server-side<br>Kurento<br>recording<br>pipelines)|Blocked<br>(Client-side raw<br>canvas/pixel<br>extraction is<br>restricted)|
|Candidate<br>Access|Zero Install<br>(Standard<br>modern<br>WebRTC|Zero Install<br>(Modern web<br>browsers|Outdated guest<br>flow; historically<br>dependent on|App installation<br>strongly pushed;<br>browser client|



||browsers:<br>Chrome, Firefox,<br>Safari)|supported<br>natively)|heavy server<br>components|has reduced<br>capabilities|
|---|---|---|---|---|
|Platform Support|Fully responsive<br>across desktop<br>and mobile<br>WebRTC<br>browsers|Comprehensive<br>desktop browser<br>and native<br>mobile SDK<br>support|Weak and<br>unoptimized<br>mobile browser<br>responsiveness|Full<br>cross-platform<br>client support<br>(closed-source)|
|Setup &<br>Maintenance|Low<br>(Single-comman<br>d deployment<br>via Docker /<br>Mediasoup)|High (Requires<br>orchestrating<br>Prosody, Jicofo,<br>and Jitsi<br>Videobridge)|High (Requires<br>MySQL,<br>Red5/Tomcat,<br>and Kurento<br>services)|Zero operational<br>maintenance<br>(SaaS), but<br>closed<br>ecosystem|
|Maintenance<br>Health|Actively<br>maintained<br>lightweight SFU<br>architecture|Highly active<br>(Core release<br>verified<br>September<br>2026)|Low activity<br>(Infrequent<br>updates, legacy<br>codebase)||



# **Platform Selection Rationale** 

Platform Selection Rationale

DECODE requires access to the candidate’s raw webcam video in the browser before network encoding, so that gaze estimation is not affected by compression artefacts. Closed or proprietary solutions (Zoom, Google Meet) restrict client-side access to raw camera frames. Among open-source alternatives, Apache OpenMeetings limits webcam resolution to 1024×768 and relies on a legacy Java/Kurento stack. Jitsi Meet requires orchestrating multiple services (Jicofo, Prosody, Jitsi Videobridge) and does not provide a ready-made local recording pipeline.

MiroTalk SFU was selected because it is self-hosted, open-source (AGPL v3), and provides direct access to the local camera stream via the browser’s getUserMedia API. The candidate’s video is recorded locally in the browser using MediaRecorder and uploaded to the server in chunks after the session ends. No client installation is required; the candidate joins via a link. This architecture ensures that gaze data quality depends only on the candidate’s camera, not on network conditions.

# **NASIL HAZIRLANDI VE YAPILMASI GEREKEN DUZENLEMELER:** 

textler rewrite edilecek tablo column kontrol ekleme yaoılcaka mı 

