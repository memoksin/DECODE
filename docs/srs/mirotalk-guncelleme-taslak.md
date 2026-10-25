# 1.2, 1.4.1, 2.1 — MiroTalk güncellemesi (bekliyor)

Durum: hocaya sorulacak (26 Ekim). Cevap gelince seçilen seçeneğe göre `1.1-1.2.md`, `1.4.1-2.1.md` ve `context-diagram.puml` güncellenir. Kontrol listesi: [dec-20-tutarlilik-listesi.md](dec-20-tutarlilik-listesi.md).

## Hocaya soru

MiroTalk SFU'yu fork'layıp self-host ediyoruz (DEC-44), yani kodu bizim. Context diyagramında dış sistem ne olmalı?

- **A (öneri):** Web browser «system». Kamera tarayıcının MediaDevices API'sinden gelir. MiroTalk, dataset ve STA modeli DECODE'un içinde.
- **B:** MiroTalk SFU «system». Okuyan için tanıdık, ama kodunu değiştirdiğimiz için teknik olarak dış sistem değil.

Toplantı 2'deki açık soru da aynı: tek kutu (DECODE) mu, iki kutu (videoconf. + STA model builder) mu?

## 1.2 Scope (A ve B için aynı)

| Yer | Eski | Yeni |
|---|---|---|
| Objective 4 | Develop a videoconferencing extension that estimates where the candidate looks on the shared code… | Extend an open-source videoconferencing platform (MiroTalk SFU) so that the candidate's webcam is recorded in their browser while they read code, then estimate where they looked, build their scanpath and classify it against both trending paths. |
| Limitation 2 | Only code reading on the shared screen is analysed… | Only code reading in DECODE's code view is analysed. Typing and writing behaviour are not modelled. |
| Limitation 3 | …areas of interest may need to be code blocks instead of single lines. | Webcam gaze is less accurate than an eye tracker, so areas of interest are code blocks, not single lines, and the candidate's webcam must provide at least 720p at 30 fps. |
| Limitation 5 | Only Google Meet is supported… | Interviews run only on our self-hosted MiroTalk SFU fork. Google Meet and Zoom are not supported, because they do not give access to the candidate's raw camera video. |

## 1.4.1 ve 2.1 — Seçenek A

Diyagram: `[Web browser «system»] — [DECODE]`

- **Web browser:** The interviewer and the candidate open DECODE's web client from a link, with no installation. The candidate's browser gives the webcam video through the MediaDevices API and records it locally. The recording is uploaded when the session ends. The interviewer's browser shows the result.
- **Candidate's webcam:** Not a direct interface. DECODE reaches it only through the browser.
- **Scope:** DECODE has one system interface. The videoconferencing platform (our MiroTalk SFU fork), the datasets and the STA model are internal to the system.

| System Interface | Functionality | Input | Output |
|---|---|---|---|
| Web browser | Runs DECODE's client for the interviewer and the candidate, gives access to the candidate's webcam, and shows the code, calibration and result pages. | Candidate webcam recording (at least 720p, 30 fps) | Code view, calibration points, experience level result with deviation from the trending paths |

## 1.4.1 ve 2.1 — Seçenek B

Seçilirse yazılacak. Fark: dış sistem MiroTalk SFU; tablo satırı "MiroTalk SFU | provides the meeting and the candidate's local recording…"; scope maddesinde MiroTalk iç bileşen olarak geçmez.
