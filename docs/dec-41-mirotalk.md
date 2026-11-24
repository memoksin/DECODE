# DEC-41 — MiroTalk'u indir ve çalıştır (prototip tabanı)

Durum: çalışıyor (24 Kasım 2026, Mehmet + agent). Kayıt Mehmet'in kamerasıyla alındı.

## Sonuç

- MiroTalk SFU yerelde ilk denemede çalıştı. Developer'ın kamerası **tarayıcıda** kaydedildi: **1280×720, 30,0 fps, VP9 + Opus, WebM**.
- Kaydedilen görüntü kameranın kendisi, sekme/ekran kaydı değil (kare kontrol edildi, arayüz yok). DEC-44 varsayımı doğrulandı.
- PR-01 (≥ 720p, 30 fps) bu donanımda sağlanıyor.
- 720p, MiroTalk'un masaüstü varsayılanı (`getVideoConstraints`: `ideal` 1280×720, 30 fps). Kamera daha yüksek çözünürlük destekliyor olabilir; 1080p (`fhd`) ayarı denenmedi.
- Kaydı **host (interviewer) başlatır**: eklentide hazır kodlardan birini seçer, kod developer'ın önüne gelir ve kayıt başlar (Mehmet, 24 Kasım). Fork'ta gereken: host'un komutuyla kayıt **developer'ın tarayıcısında** başlamalı. Bu denemede tek kişiydik, kaydı başlatan ve kaydedilen aynı tarayıcıydı; iki kişilik akış denenmedi.
- Sonraya: ses kapatılabilir; sunucuya yükleme (`/recSync`) denenmedi, dosya tarayıcıdan indirildi.

## Yöntem

1. `git clone --depth 1 https://github.com/miroslavpejic85/mirotalksfu` → `local/dec-41/` (git-ignored).
2. `cp app/src/config.template.js app/src/config.js`, `npm install` (415 paket, 24 sn).
3. Başlatma (`.env` dosyası yok, ayarlar ortam değişkeniyle):
   ```
   JWT_SECRET=$(openssl rand -hex 32) RECORDING_ENABLED=true STATS_ENABLED=false npm start
   ```
   - `JWT_SECRET` zorunlu; yoksa sunucu açılmıyor. Her çalıştırmada rastgele üretildi, dosyaya yazılmadı.
   - `STATS_ENABLED=false`: varsayılan ayar sayfaya `stats.mirotalk.com` analitik script'i ekliyor; kapatıldı.
4. Chrome → `https://localhost:3010/join/dec41test` (kendi imzalı sertifika uyarısı geçildi), kamera: MacBook Pro Kamerası, ad: "Developer".
5. Alt çubukta ⌃ menüsü → Recording & Capture → Start Recording; ~30 sn; Stop Recording. Dosya `~/Downloads`'a indi, `local/dec-41/rec/`'e taşındı.
6. Ölçüm: `ffprobe` (stream bilgisi + `-count_frames`), bir kare `ffmpeg` ile çıkarılıp bakıldı.

## Ölçümler

| Özellik | Değer |
|---|---|
| Dosya | `Rec_2026-11-24-10_09_42.webm`, 10,6 MB |
| Süre | 32,3 sn |
| Video | VP9, 1280×720 |
| Kare | 970 kare / 32,3 sn = **30,0 fps** |
| Ses | Opus |
| Ortalama bitrate | 2,63 Mbps |

Donanım ve yazılım:

| | |
|---|---|
| Bilgisayar | MacBook Pro, Apple M4 Max (14 çekirdek), 36 GB RAM |
| Kamera | MacBook Pro Kamerası (dahili) |
| OS | macOS 27.2.1 |
| Tarayıcı | Google Chrome (sürüm not edilmedi) |
| MiroTalk SFU | 2.8.68, commit `363cbe2` (24 Kasım 2026) |
| Node.js | 24.19.0 (`package.json` ≥ 24.22.1 istiyor; uyarı yok, sorunsuz çalıştı) |

## Sınırlamalar

- **Makineye bağlı:** çözünürlük ve fps kameraya ve tarayıcıya bağlı. Tek makine, tek kamera; Windows ve düşük kaliteli laptop kamerası denenmedi (DEC-45'te bir arkadaşın kaydı 16 fps'e düşmüştü). Bağımlı olması beklenen bir şey: gereksinim cihaz sınıfına göre (≥ 720p / 30 fps kamera) tanımlı.
- Tek katılımcı, yerel ağ. Ağ gecikmesi (PR-02) ve iki kişilik görüşme denenmedi.
- Kayıt tarayıcıdan indirildi; sunucuya parçalı yükleme (`/recSync`) denenmedi.
- Kayıt ses de içeriyor; analiz için gerekmiyor, gizlilik açısından fork'ta kapatılabilir.
- WebM başlığında "unknown-sized element" uyarısı var (MediaRecorder çıktısı); ffprobe ve ffmpeg dosyayı sorunsuz okudu.

## Todo

- [ ] 1080p (`fhd`) ayarıyla tekrar kaydet; kamera gerçekten 1080p veriyor mu?
- [ ] Bir Windows laptopta aynı deneme (DEC-62 ile birlikte).
- [ ] Sunucuya yükleme (`/recSync`, `rec-upload` JWT) dene.
- [ ] Fork: host komutuyla developer tarafında kayıt, sesi kapat, kalibrasyon ve kod sayfasını `public/` altına ekle (DEC-69, DEC-70).

## SRS için cümle

> In a first test on a self-hosted MiroTalk SFU instance (v2.8.68), the developer's built-in laptop webcam (MacBook Pro, Apple M4 Max, macOS) was recorded in the browser at 1280×720 and 30 fps (VP9/WebM), which meets PR-01; resolution and frame rate depend on the developer's camera and browser.

## Kaynaklar

1. Pejic, M. (2026). *MiroTalk SFU* (Version 2.8.68) [Computer software]. GitHub. https://github.com/miroslavpejic85/mirotalksfu (commit 363cbe2)
2. DEC-44 video platformu kararı: `docs/dec-44-video-platformu.md`
3. DEC-45 minimum kamera çözünürlüğü: `docs/dec-45-kamera-cozunurlugu.md`
