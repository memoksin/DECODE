# DEC-20 — SRS tutarlılık listesi

Hazırlık: 25 Ekim 2026. Teslim: 27 Ekim 22:55. Bölümler gelince her birini bu listeyle kontrol et.

## Bölüm durumu (25 Ekim)

| Bölüm | Görev | Sahibi | Durum | Repo'da |
|---|---|---|---|---|
| 1.1 Purpose, 1.2 Scope | DEC-17 | Mehmet | Done, **eski: Google Meet** | `1.1-1.2.md` |
| 1.3 Related Work | DEC-36 | Burcu | In Progress | yok |
| 1.4.1 Context diagram, 2.1 External interfaces | DEC-18 | Mehmet | Done, **eski: Google Meet** | `1.4.1-2.1.md`, `context-diagram.*` |
| 1.4.1 UI taslakları | DEC-23 | İrem | Todo | yok |
| 1.4.2 Product functions, 2.2 Use cases | DEC-24 | İrem | In Progress, **eski: Meet, satır AOI, 21 Ekim kararları yok** | `srs-1.4.2-2.2-taslak.md` |
| 1.4.3–1.4.5 User char., limitations, assumptions | DEC-29 | Sude | Todo | yok |
| 1.5 Definitions, 5.1 Acronyms | DEC-35 | Burcu | Todo | yok |
| 2.3 Usability, 2.4 Performance | DEC-25 | Burcu | Todo | yok |
| 2.5 ERD | DEC-26 | İrem | Todo | yok (draw.io) |
| 3 Software estimation | DEC-19 | Mehmet | Done | `3-software-estimation.md` |
| 4 References | DEC-34 | Burcu | In Progress | yok |
| 5.2 Sprint 1 | DEC-14 | Mehmet | 27 Ekim'de son nokta | `5.2-sprint-1.md` |
| Sunum (11 slayt) | DEC-30 | Sude | Todo | yok |

## Kontrol listesi

Her bölümde ara (`rg -i`), kararla çelişen yeri düzelt.

1. **Platform: MiroTalk SFU** ([DEC-44](../dec-44-video-platformu.md)). "Google Meet", "Chrome extension", "screen share" geçmemeli. Aday bizim client'ımıza girer; kod ve kalibrasyon bizim sayfada gösterilir, ekran paylaşımı yok.
2. **AOI: kod blokları**, satır değil ([DEC-45](../dec-45-kamera-cozunurlugu.md)). "line AOI", "code lines" geçmemeli.
3. **Analiz oturum sonrası**, gerçek zamanlı değil (Toplantı 2). Bu bir limitation değil.
4. **Use case kararları** (Toplantı 2): Researcher aktörü yok; Interviewer → Open Session; Candidate session use case'i; Classify + Map Gaze birleşik; kritik UC'ler: Run Analysis Session, Generate Trending Paths, Evaluate Classification Model.
5. **Kamera: minimum 720p @ 30 fps, önerilen 1080p.** 2.4 ve constraints'te aynı sayılar. Cümle: DEC-45 dosyasındaki "SRS için cümle".
6. **Rapor:** aday bazında sınıf + trending path'ten sapma derecesi (F7, UC-07).
7. **Gizlilik ↔ kayıt:** F8 "raw video is not stored" diyor; SRS 3 ise kaydı backend'e yüklüyor (upload → Python job). Tek cümleye bağla: ör. "video is deleted after analysis".
8. **Terimler aynı:** novice / experienced (expert / non-expert değil), scanpath, trending path, AOI, STA. 1.5 Definitions ile eşleşmeli.
9. **Kaynak numaraları** 4 References ile aynı sırada. 1.1 ve 1.4.2 şu an Proposal numaralarını kullanıyor ([3]–[6]).
10. **Dataset:** birleştirme uygun (aynı dil, etiket, task); dile göre ayrı model.

## Bulunan sorunlar (25 Ekim)

- Taslak düzeltme hazır, hocanın cevabını bekliyor: [mirotalk-guncelleme-taslak.md](mirotalk-guncelleme-taslak.md).
- `1.1-1.2.md`: Objectives "videoconferencing extension … shared code"; Limitations "Only Google Meet is supported" ve "areas of interest may need to be code blocks" (artık karar: blok). → Mehmet
- `1.4.1-2.1.md` ve context diyagramı: tümü Google Meet. → Mehmet
- `srs-1.4.2-2.2-taslak.md`: F2/UC-01/UC-04 Meet ve ekran paylaşımı; F4 ve UC-05 satır AOI; Researcher aktörü; açık sorular bölümü kararlarla kapanmamış. → İrem (F4/UC-05 için DEC-24'e yorum yazıldı)
