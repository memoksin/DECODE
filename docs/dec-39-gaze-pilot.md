# DEC-39 — Gaze pilot: MediaPipe vs L2CS-Net, bilinen ekran noktaları

Durum: test planı hazır, kayıt alınmadı (19 Kasım 2026, İrem). Kapsam: tek cihazlık pilot (Mehmet'in 10 Kasım yorumu). Tam model karşılaştırması bu pilotla bitmiş sayılmaz.

## Sonuç

Henüz yok. Pilot kayıt alınınca doldurulacak.

## Neden bu pilot

- DEC-45 titreme ve sapmayı ölçtü. Ekran noktasına göre **doğruluk** ölçülmedi, çünkü ground truth yoktu.
- Bu pilotta ground truth var: kişi ekranda yeri bilinen noktalara bakar.
- Issue açıklamasındaki DEC-37/Meet kaydı eski yaklaşım. DEC-44 kararına göre aday kamerası tarayıcıda yerel kaydedilir; pilot da böyle kaydedilir.

## Yöntem (plan)

### Kayıt düzeni

- Tek sayfa (`experiments/dec-39/pilot.html`) hem noktaları gösterir hem kamerayı kaydeder. Böylece noktalar ve video aynı saatle zamanlanır.
- Kamera: `getUserMedia` 1920×1080 @ 30 fps istenir, `MediaRecorder` ile WebM kaydedilir (DEC-44'teki yol). Gerçekte verilen çözünürlük ve fps `track.getSettings()` ile kaydedilir.
- Sayfa tam ekran, beyaz arka plan, siyah nokta (çap ~20 px, ortasında küçük kırmızı merkez).
- Sayfa sonunda iki dosya indirir: `pilot-<tarih>.webm` ve `pilot-<tarih>.json` (nokta konumları, zamanlar, ekran ve tarayıcı bilgisi).

### Noktalar

Konumlar ekran genişliği/yüksekliğinin yüzdesi olarak verilir.

| Küme | Noktalar | Sayı | Amaç |
|---|---|---|---|
| Kalibrasyon | 3×3 ızgara: x, y ∈ {%10, %50, %90} | 9 | Modeli kişiye/ekrana eşlemek |
| Değerlendirme | x, y ∈ {%30, %70} + (%50, %25), (%50, %75), (%25, %50), (%75, %50) | 8 | Doğruluk ölçmek; kalibrasyonda hiç kullanılmaz |

- Her nokta **2 sn** gösterilir. İlk **0.5 sn** atılır (göz noktaya gidiyor), kalan 1.5 sn ölçülür.
- Sıra: önce 9 kalibrasyon noktası, sonra 8 değerlendirme noktası karışık sırada (sabit seed, JSON'a yazılır). Sonra aynı 17 nokta bir tur daha (tekrarlanabilirlik).
- Başta 3 sn geri sayım. Toplam ~75 sn.

### Ortam

- Kişi ekrandan ~60 cm uzakta, mezura ile ölçülür ve yazılır.
- Normal oda ışığı, pencere arkada değil. Gözlük takılıyorsa not edilir.
- Baş serbest, ama mümkün olduğunca sabit tutulur.

### Analiz (`experiments/dec-39/analyze.py`)

Aynı video, aynı kareler, iki model:

1. **MediaPipe Face Landmarker:** iris merkezi ve göz köşeleri → normalize iris konumu. Kalibrasyon noktalarında ikinci derece polinom + ridge regresyonu ile ekran koordinatına eşlenir.
2. **L2CS-Net (Gaze360, ResNet50, DEC-45'teki ağırlıklar):** pitch/yaw → aynı kalibrasyon noktalarında aynı regresyonla ekran koordinatına eşlenir.

Her iki model de yalnızca 9 kalibrasyon noktasıyla eşlenir, 8 değerlendirme noktasında ölçülür.

### Ölçülecekler

| Ölçüm | Nasıl |
|---|---|
| Hata (px) | Değerlendirme noktasında tahmin ile gerçek nokta arası mesafe: ort. / medyan / p95 |
| Hata (°) | px → cm (ekran fiziksel boyutu) → açı (göz–ekran mesafesi) |
| Yüz bulma | Karelerin yüzde kaçında yüz bulundu |
| İşlem süresi | Kare başına ms, aynı cihazda, CPU |
| Tekrar farkı | 1. tur ile 2. tur hatası arasındaki fark |

Karşılaştırma ölçütü: kod bloğu AOI'si model hatasından büyük olmalı (DEC-22, DEC-45). Bir satır ≈ 0.5°.

## Cihaz (pilotun yapılacağı makine)

19 Kasım 2026'da Windows'tan okundu (İrem).

| | |
|---|---|
| Bilgisayar | HP ProBook 450 G10 (15.6") |
| CPU | Intel Core i7-1355U |
| GPU | Intel Iris Xe (entegre). NVIDIA yok → L2CS CPU'da çalışır |
| OS | Windows 11 Pro 10.0.26200 |
| Kamera | HP HD Camera (dahili; tam model not edilmedi) |
| Ekran | 1920×1080, 15.6" (~34.5 × 19.4 cm, hesaplanan) |
| Tarayıcı | kayıtta JSON'a yazılacak |
| Gerçek kayıt çözünürlüğü / fps | kayıtta JSON'a yazılacak |
| Windows ölçekleme | %125 (`devicePixelRatio` 1.25, tarayıcıda okundu): CSS 1536×864 = 1920×1080 fiziksel px |
| Göz–ekran mesafesi | kayıtta ölçülecek |

## Ölçümler

Henüz yok.

## Sınırlamalar (beklenen)

- Tek kişi, tek cihaz, tek ışık koşulu, ~75 sn. Sonuç genellenemez; yalnızca yöntemi ve kabaca büyüklüğü gösterir.
- HP HD Camera büyük ihtimalle 720p. 1080p istense de kamera vermezse 720p kaydedilir; gerçek değer JSON'da.
- `MediaRecorder` kaydı değişken kare hızlı olabilir (DEC-45'te Windows Kamera ~16 fps vermişti). Gerçek fps kare sayısından hesaplanır.
- Noktaya bakmak kod okumak değildir. Kod okurken göz hareketi farklı.
- Video ile nokta zamanlaması arasında onlarca ms kayma olabilir. İlk 0.5 sn atıldığı için etkisi küçük.
- İşlem süresi yalnızca bu CPU için geçerli; GPU'lu makinede L2CS çok daha hızlı olur. Bu laptopta L2CS kare başına ~316 ms (yüz yokken ölçüldü), yani gerçek zamanlı değil; analiz zaten kayıttan sonra (DEC-44).

## Todo

- [x] `pilot.html` yaz (nokta gösterimi + kamera kaydı + JSON). 19 Kasım'da sahte kamerayla denendi: 34 nokta, ~71 sn, webm + JSON indi. Gerçek kamerayla denenmedi.
- [ ] Mesafeyi ölç, pilot kaydını al, cihaz tablosunu tamamla.
- [x] `analyze.py` yaz (DEC-45 kodunu ve ağırlıklarını kullan). 19 Kasım: matematik kısmı `--test` ile sınandı (sentetik veri). Model kısmı gerçek kayıtla henüz çalışmadı.
- [x] Bu makineye DEC-45 ortamını kur (`uv`, ffmpeg, model ağırlıkları). 19 Kasım: kuruldu, sentetik (yüzsüz) videoyla uçtan uca çalıştı. Kare başına MediaPipe 14 ms, L2CS 316 ms (CPU); bir pilot ~10 dk. Ayrıntı: `experiments/dec-39/README.md`.
- [ ] İki modeli gerçek pilot kaydında çalıştır; MediaPipe göz/baş özelliklerine ilk kayıtta bak.
- [ ] Ölçümler ve Sonuç bölümlerini doldur, Linear'a kısa özet yaz.
- [ ] Sonra (pilot dışı): daha fazla kişi ve cihaz, kod okuma görevi.

## SRS için cümle

Pilot bitince yazılacak.
