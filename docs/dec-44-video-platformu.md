# DEC-44 — Video platformu kararı

Durum: karar verildi, **MiroTalk SFU** (23 Ekim 2026). Kaynak: [Toplantı 2](toplantilar/2026-10-21-toplanti-2.md#video-platformu). Tablo DEC-43 (Burcu) için taslak.

## Öneri

- Platform: **MiroTalk SFU, self-host, fork**. Yedek: **Jitsi Meet** (`lib-jitsi-meet` ile kendi client'ımız).
- Prototip tahmini: MiroTalk 24–40 saat, Jitsi 40–60 saat (scout tahmini, ölçülmedi).
- Aday videosu **platformdan alınmaz**. Self-host ettiğimiz için adayın açtığı web client'ı biz sunarız. Adayın kamerası kendi tarayıcısında `getUserMedia` ile tam çözünürlükte alınır, oturumda yerel kaydedilir, oturum bitince yüklenir. Görüşme akışı yalnızca konuşma içindir.
- Analiz gerçek zamanlı değil (Toplantı 2), bu yüzden sonradan yükleme yeterli.
- Adayda kurulum yok: yalnızca link açar. 20 Ekim kısıtı ("aday kurulum yapmaz") korunur.
- Kalibrasyon ve kod da bizim client'ta gösterilir, ekran paylaşımı gerekmez. Kalibrasyon noktaları ve kod satırlarının ekrandaki konumu DOM'dan kesin bilinir, AOI eşlemesi kolaylaşır. Bu, 20 Ekim'deki "link + ekran paylaşımı" kararının yerini alır.
- Sonuç: ağ sıkıştırması gaze verisini etkilemez. DEC-37 büyük ihtimalle gereksiz. DEC-45 (minimum kamera) hâlâ gerekli.

## Karşılaştırma

| | Jitsi Meet | MiroTalk SFU | OpenMeetings | Zoom (referans) |
|---|---|---|---|---|
| Lisans | Apache-2.0 [1] | AGPL-3.0, değişiklik yayınlanmalı [5] | Apache-2.0 [8] | Kapalı kaynak [11] |
| Self-host | Prosody, Jicofo, JVB; Debian/Ubuntu, TLS [2] | Node 22, mediasoup, HTTPS [6] | Java 21, Kurento, DB, TURN [9] | Yok |
| API | IFrame API (track yok) [3]; `lib-jitsi-meet` `TRACK_ADDED` ile track verir [4] | REST + iframe; client açık kaynak [5] | REST/SOAP; JS embed yok [9] | Web SDK uzak ham veri yok; native SDK YUV verir [12] |
| Video | Varsayılan 720p, simulcast açık, AV1/VP9/VP8/H264 [3] | Simulcast, 5 Mbps, 30 fps (kod) [7] | Kamera en çok 1024×768 [10] | Uzak kare sıkıştırılmış, örnek 360p [12] |
| Kayıt | Jibri: birleşik ekran, 1080p MP4, kişi bazlı değil [2] | Tarayıcıda yerel kamera `MediaRecorder` (WebM VP9/VP8), sunucuya parçalı yükleme [7][14] | MP4, ffmpeg dönüşüm hataları var [10] | Bulut kaydı, RTMS kredili [13] |
| Aday tarafı | Tarayıcı, link; misafir girişi sunucu ayarına bağlı | Tarayıcı, link | Tarayıcı; misafir girişi doğrulanmadı | Tarayıcı (Web SDK) |
| Sağlık | Son sürüm 14 Eylül 2026, ~30k yıldız | Push 23 Ekim 2026, ~3k yıldız, tek geliştirici, sürüm yok | 9.1.0 (Temmuz 2026), ~700 yıldız | — |
| Aday kamerasını ham alma | Kendi client'ımız: `createLocalTracks({constraints})` → `getTrack()` [4] | Fork + hook: `localVideoStream` [7] | Yol yok | Yol yok |
| Uygunluk | İyi | **En iyi** | Zayıf | Zayıf |

**Neden MiroTalk:** İhtiyacımız olan şeyin çoğu zaten içinde var.
- Yerel kamera kaydı: `MediaRecorder` doğrudan `localVideoStream` üzerinde çalışır, yani tek katılımcıyı kaydeder, oda görüntüsünü birleştirmez [7].
- Parçalı yükleme: kayıt `/recSync*` endpoint'lerine 4 saniyelik parçalar halinde gider. Endpoint'ler oda bazlı `rec-upload` JWT ile korunur [14].
- Çözünürlük: `fhd` (1920×1080) ve `4k` var. Producer `stopTracks: false` ile oluşturulduğu için track kapanmaz [7].
- UI düz JS, framework yok. Kendi sayfamızı (kalibrasyon, kod görüntüleyici) `public/` altına ekleriz.
- Misafir girişi: `HOST_PROTECTED=true`, `HOST_USER_AUTH=false` ile görüşmeci giriş yapar, aday `/join/<oda>` ile misafir olarak gelir [15].
- AGPL bizim için sorun değil, repo zaten public.

**MiroTalk riskleri:**
- `RoomClient.js` tek parça ve büyük (~650 KB), testi yok. Upstream güncellemeleri fork'u bozabilir, bu yüzden bir sürüme sabitleriz.
- Tek geliştirici, sürüm etiketi yok.
- Medya 40000–40100 portlarından gider. Üniversite ağında bu portlar kapalıysa çalışmaz, TURN gerekir.
- Node ≥24.22.1 gerekiyor (`package.json`), README "Node 22" diyor.

**Jitsi'nin yeri:** Apache-2.0, büyük topluluk, düzenli sürüm, belgeli API [4]. Ama yerel kayıt ve yükleme hazır değil. Tam uygulamayı fork'lamak ağır (React 19, Redux), bu yüzden `lib-jitsi-meet` ile kendi client'ımızı yazmamız gerekir. MiroTalk fork'u tıkanırsa buna geçeriz.

**Elenenler:** OpenMeetings (düşük çözünürlük, ham video yolu yok), Zoom (kapalı kaynak, kredi gerekiyor, ham video yalnızca native uygulamada).

## SRS için cümle

> Video conferencing is provided by a self-hosted, modified MiroTalk SFU instance. The candidate's webcam video is captured in the candidate's browser by the DECODE web client at the camera's native resolution, before network encoding, and uploaded after the session. This avoids compression loss and keeps gaze estimation error as low as possible.

## Açık konular

- Aday videosu yükleniyor: rıza ekranı (F3, F7, F8) bunu açıkça söylemeli.
- DEC-41 prototipi: MiroTalk'u kur, adayın kamerasını 1080p kaydet, yükle, kalibrasyon sayfasını göster. Üniversite ağında portları test et.
- Doğrulanmadı: mobil ve tarayıcı desteği, kaydın bitrate'i, uzun oturumda `MediaRecorder`'ın bellek kullanımı.

## Kaynaklar

1. https://github.com/jitsi/jitsi-meet
2. https://jitsi.github.io/handbook/docs/devops-guide/devops-guide-quickstart, https://github.com/jitsi/jibri
3. https://github.com/jitsi/jitsi-meet/blob/master/config.js, https://jitsi.github.io/handbook/docs/dev-guide/dev-guide-iframe-functions
4. https://github.com/jitsi/lib-jitsi-meet/blob/master/JitsiConferenceEvents.ts (`TRACK_ADDED`, satır 472)
5. https://github.com/miroslavpejic85/mirotalksfu
6. https://docs.mirotalk.com/mirotalk-sfu/self-hosting/
7. https://github.com/miroslavpejic85/mirotalksfu/blob/main/public/js/RoomClient.js
8. https://github.com/apache/openmeetings
9. https://openmeetings.apache.org/InstallMediaServer.html, https://openmeetings.apache.org/RestAPISample.html
10. https://openmeetings.apache.org/WebcamResolutions.html, https://issues-test.apache.org/jira/browse/OPENMEETINGS-2140
11. https://developers.zoom.us/docs/video-sdk/
12. https://developers.zoom.us/docs/meeting-sdk/web/, https://developers.zoom.us/docs/video-sdk/linux/raw-data/receive-raw-data/
13. https://developers.zoom.us/docs/rtms/meetings/media/
14. https://github.com/miroslavpejic85/mirotalksfu/blob/main/app/src/Server.js (`/recSync*`, `rec-upload`)
15. https://docs.mirotalk.com/mirotalk-sfu/host-protection/
