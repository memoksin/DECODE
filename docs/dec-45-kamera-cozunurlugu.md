# DEC-45 — Minimum kamera çözünürlüğü

Durum: bitti (25 Ekim 2026). Kendi kamerayla ve ekip arkadaşının gerçek 720p laptop kamerasıyla ölçüldü. Kod: [experiments/dec-45](../experiments/dec-45/).

## Sonuç

- **Minimum: 720p @ 30 fps. Önerilen: 1080p.**
- Karar (Mehmet, 25 Ekim 2026): gerçek 720p kamerada p95 titremesi ~2 kat çıksa da minimum 720p kalıyor. Fiyat-performans laptopların çoğu 720p kamerayla geliyor; 1080p şartı büyük bir aday kitlesini dışarıda bırakır. Uç sapmalar sınırlama olarak yazıldı.
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

## Ek ölçüm: sabit bakışta titreme (gerçek 720p)

Doğrudan 720p kaydında aynı anın 1080p hali olmadığı için yukarıdaki "1080p'den sapma" ölçülemez. Bunun yerine her kayıtta ekranın ortasına 20 sn sabit bakıldı. Her karenin medyan bakış yönünden sapması ölçüldü (`stability.py`). Bu yöntem referans gerektirmez.

| Video (600 kare) | Yüz bulma | Titreme: ort. / medyan / p95 | İris (px) |
|---|---|---|---|
| 1080p | %100 | 1.59° / 1.33° / 3.54° | 28.8 |
| 720p, 1080p'den küçültülmüş | %100 | 1.48° / 1.30° / 2.85° | 19.2 |
| 720p, kamera doğrudan (native) | %100 | 1.72° / 1.34° / 4.25° | 18.1 |

- Üç kaydın medyan titremesi aynı (~1.3°). Sabit bakışta 720p, 1080p kadar kararlı.
- Doğrudan 720p'nin uç değerleri daha kötü: p95 4.25°, küçültülmüşte 2.85°. Bu, küçültmenin gürültüyü azalttığını, yani ilk testin iyimser olduğunu doğruluyor. Ama fark yalnızca uç değerlerde görülüyor ve küçük.
- Titremenin içinde gözün ve başın gerçek küçük hareketleri de var. Tek kayıt, 20 sn.

## Ek ölçüm: ekip arkadaşının 720p laptop kamerası

Aynı yöntem (`stability.py`, ekranın ortasına sabit bakış). Ekip arkadaşı Windows Kamera uygulamasıyla iki kayıt aldı (23 Ekim): normal ışık ve loş ışık, ~32 sn, 1280×720. Ortalama parlaklık (Y): normal 141, loş 87.

İlk ölçüm tam kayıtlarla yapıldı. Kayıtlar 32 sn olduğu için yavaş göz/baş kayması titremeyi şişiriyordu. Adil karşılaştırma için her iki kaydın 6.–26. saniyeleri alındı (ilk 6 sn kurulum hareketi olabilir).

| Video | Kare | Yüz bulma | Titreme: ort. / medyan / p95 | İris (px) |
|---|---|---|---|---|
| Mehmet, 720p native (referans) | 600 | %100 | 1.72° / 1.34° / 4.25° | 18.1 |
| Arkadaş, normal ışık, 32 sn | 497 | %100 | 3.13° / 2.17° / 9.18° | 26.8 |
| Arkadaş, loş ışık, 32 sn | 964 | %100 | 2.91° / 1.84° / 8.45° | 26.6 |
| Arkadaş, normal ışık, 20 sn | 304 | %100 | 3.01° / 2.03° / 8.46° | 26.9 |
| Arkadaş, loş ışık, 20 sn | 600 | %100 | 2.39° / 1.32° / 8.63° | 26.7 |

- Loş ışık yüz bulmayı bozmadı (%100). Loş kayıt normalden kötü değil, bu iki kayıtta ışık belirleyici değil.
- Süreyi eşitleyince loş kaydın medyanı (1.32°) Mehmet'inkiyle aynı. Tipik karede model arkadaşın kamerasında da kararlı.
- Fark uç değerlerde: p95 ~8.5°, Mehmet'te 4.25°. Kırpma, kısa baş hareketi gibi sıçramalar. Kamera mı kişi mi, bu veriyle ayrılamaz.
- İris daha büyük (27 px, Mehmet'te 18 px): arkadaş kameraya daha yakın oturmuş. Buna rağmen uç değerler daha kötü.

## Sınırlamalar

- **Küçültülmüş 720p, gerçek 720p kamera değil.** Küçültme gürültüyü azaltır. Ucuz bir 720p kamera, özellikle kötü ışıkta, daha kötü sonuç verebilir. Bu yüzden 720p sonucu iyimser.
- Tek kişi, tek kamera, tek ışık koşulu, 60 sn.
- Sapma, doğruluk kaybı değildir: 1080p'nin kendisi de hatalı olabilir. Doğruluk için bilinen noktalara bakılan bir kalibrasyon kaydı gerekir.
- Kayıt ffmpeg'in varsayılan x264 ayarıyla alındı (~1 Mbps).
- Arkadaşın normal ışık kaydı 60 fps etiketli ama değişken kare hızlı, gerçekte ~16 fps (31.7 sn'de 497 kare). Windows Kamera uygulaması kare hızını düşürmüş. Loş kayıt sabit 30 fps.
- Arkadaşın kayıtları ffmpeg ile kırpılırken yeniden kodlandı (x264, CRF 18). Yeniden kodlama tek başına ~1.1° fark yaratabiliyor (yukarıdaki kontrol), ama bu titreme ölçümünde her kare aynı kayıttaki medyana göre ölçüldüğü için etkisi daha küçük.
- Kamera modeli not edilmedi. İki kişi, iki kamera: kişi ve kamera etkisi ayrılamaz.
- Ölçümler CPU'da yapıldı (`run.py`'de `torch.device("cpu")`). GPU'ya (MPS) geçilirse sayılar ondalıkta değişebilir; karşılaştırmalar aynı cihazda yapılmalı.

## Todo

- [x] Mehmet'in kamerasıyla doğrudan 720p kayıt (yukarıda, ek ölçüm).
- [x] Ekip arkadaşının gerçek 720p laptop kamerasıyla kayıt (biri kötü ışıkta), aynı script (yukarıda).

Sprint 2 adayları (25 Ekim, Mehmet ile konuşuldu). Sorun medyanda değil, p95'teki sıçramalarda; önce modeli değil sinyali iyileştir:
- [ ] Zamansal filtre (One Euro veya Kalman): mevcut kayıtlarda p95 düşüyor mu, `stability.py` ile ölç.
- [ ] Göz kırpma tespiti: MediaPipe göz kapağı noktalarıyla kırpma karelerini at.
- [ ] Minimum fixation süresi: çok kısa bakışları fixation sayma (fixation tespitiyle birlikte, F5).
- [ ] Ancak bunlar yetmezse: L2CS'yi küçültülmüş etiketli dataset'lerle (Gaze360, MPIIFaceGaze) ince ayar. Etiketli veri gerekir, haftalar sürer.
- [ ] Kontrol: blok AOI'leri gaze hatasından (2–4° + sıçrama) büyük mü? STA girdisi buna bağlı.

## SRS için cümle

> The candidate's webcam must provide at least 1280×720 at 30 fps; 1920×1080 is recommended. In our measurement, downscaling from 1080p to 720p added about 1.6° of gaze deviation and to 480p about 2.2°, on top of a 2–4° model error, so gaze is mapped to code blocks rather than single lines. On a second team member's native 720p laptop camera, including a dim-light recording, the face was detected in every frame and median fixation jitter matched ours (1.3°), while 95th-percentile jitter was about twice as high (8.5° vs 4.3°).
