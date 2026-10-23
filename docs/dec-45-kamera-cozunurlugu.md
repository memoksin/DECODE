# DEC-45 — Minimum kamera çözünürlüğü

Durum: ilk ölçüm bitti (23 Ekim 2026). Gerçek 720p kamera testi bekliyor. Kod: [experiments/dec-45](../experiments/dec-45/).

## Sonuç

- **Minimum: 720p @ 30 fps. Önerilen: 1080p.**
- Aday videosunu adayın tarayıcısında kaydediyoruz ([DEC-44](dec-44-video-platformu.md)). Kamera destekliyorsa 1080p istemenin bir maliyeti yok.
- 480p'de yüz hâlâ bulunuyor, ama sapma daha da artıyor ve iris yalnızca ~12 piksel kalıyor.

## Yöntem

- Bir kayıt: Mehmet, 60 sn, 1920×1080, 30 fps, Mehmet'in kamerası (model not edilmedi). Ekranın köşelerine ve ortasına bakış, kod okuma.
- Aynı videodan ffmpeg ile 720p ve 480p kopyaları üretildi. Her 2. kare analiz edildi (900 kare).
- Hazır modeller kullanıldı, eğitim yapılmadı:
  - MediaPipe FaceLandmarker: yüz bulma, iris ve gözler arası mesafe (piksel).
  - L2CS-Net (Gaze360, ResNet50): bakış açısı (pitch/yaw).
- Ground truth yok. Referans olarak 1080p'nin tahmini kullanıldı, her çözünürlükte aynı karede açı farkı ölçüldü.
- Kontrol ölçümü: 1080p videoyu küçültmeden yeniden kodlayıp aynı farkı ölçtük. Bu, modelin piksel gürültüsüne duyarlılığını, yani taban seviyeyi verir.

## Ölçümler

| Video | Yüz bulma (MediaPipe / L2CS) | 1080p'den sapma: ort. / medyan / p95 | İris (px) | Gözler arası (px) |
|---|---|---|---|---|
| 1080p | %100 / %100 | — | 28.0 | 161 |
| 1080p yeniden kodlanmış (kontrol) | %100 / %100 | 1.1° / 0.9° / 2.9° | — | — |
| 720p | %100 / %100 | 2.7° / 2.4° / 5.8° | 18.6 | 107 |
| 480p | %100 / %100 | 3.3° / 2.9° / 7.1° | 12.4 | 72 |

- Yalnızca yeniden kodlamak bile 1.1° fark yaratıyor. Model küçük piksel değişikliklerine duyarlı.
- Çözünürlük düşürmek bunun üstüne yaklaşık +1.6° (720p) ve +2.2° (480p) ekliyor. Bunlar kaba tahmin, çünkü sapmalar doğrusal toplanmaz.
- Karşılaştırma: modelin kendi hatası 2–4°, bir kod satırı ~0.5° ([DEC-22](dec-22-gaze-kutuphaneleri.md)). 720p'deki ek sapma satır bazında takibi imkânsız kılıyor, blok bazında takip mümkün.

## Sınırlamalar

- **Küçültülmüş 720p, gerçek 720p kamera değil.** Küçültme gürültüyü azaltır. Ucuz bir 720p kamera, özellikle kötü ışıkta, daha kötü sonuç verebilir. Bu yüzden 720p sonucu iyimser.
- Tek kişi, tek kamera, tek ışık koşulu, 60 sn.
- Sapma, doğruluk kaybı değildir: 1080p'nin kendisi de hatalı olabilir. Doğruluk için bilinen noktalara bakılan bir kalibrasyon kaydı gerekir.
- Kayıt ffmpeg'in varsayılan x264 ayarıyla alındı (~1 Mbps).

## Todo

- [ ] Mehmet'in kamerasıyla doğrudan 720p kayıt, aynı script.
- [ ] Ekip arkadaşının gerçek 720p laptop kamerasıyla kayıt (biri kötü ışıkta), aynı script.

## SRS için cümle

> The candidate's webcam must provide at least 1280×720 at 30 fps; 1920×1080 is recommended. In our measurement, downscaling from 1080p to 720p added about 1.6° of gaze deviation and to 480p about 2.2°, on top of a 2–4° model error, so gaze is mapped to code blocks rather than single lines.
