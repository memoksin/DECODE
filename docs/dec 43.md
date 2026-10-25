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

A core architectural requirement of the DECODE system is capturing candidate facial video at **uncompressed, raw quality** on the client side before network packetization, ensuring stable gaze extraction and calibration accuracy. Closed commercial solutions like Zoom and Google Meet impose sandboxed restrictions that block direct access to raw image frames (pixel arrays / HTML5 Canvas buffers) or require commercial SDK tiers. Among open-source alternatives, Apache OpenMeetings introduces operational overhead through its legacy Java/Tomcat and Kurento architecture, while offering an outdated guest interface. Jitsi Meet provides an established WebRTC stack, but its microservice configuration (Jicofo, Prosody, Videobridge) and heavy UI layers complicate client-side pipeline injection. 

**MiroTalk SFU** was selected because its Node.js and Mediasoup architecture is lightweight and modular. It allows candidate webcam frames to be extracted directly in the browser DOM for local calibration and gaze tracking, while providing native /recSync endpoints and JWT authentication (rec-upload) to store high-resolution (FHD/4K) session archives on the server. 

Furthermore, MiroTalk SFU operates without requiring third-party browser plugins or client installations, and its AGPL v3 license satisfies project self-hosting requirements. 

# **NASIL HAZIRLANDI VE YAPILMASI GEREKEN DUZENLEMELER:** 

textler rewrite edilecek tablo column kontrol ekleme yaoılcaka mı 

