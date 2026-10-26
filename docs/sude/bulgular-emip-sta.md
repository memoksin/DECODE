# Bulgular: EMIP, düzeltilmiş EMIP ve STA girdisi

Hazırlayan: Sude. Tarih: 24 Ekim 2026. Kaynak: veri dosyaları ve kod incelendi (EMIP-Toolkit, Peitek replikasyon paketi, Eraslan'ın STA kodu).

## 1. EMIP'te katılımcılara aynı kod mu verildi?

Evet, ama birkaç ayrıntı var.

- **Aynı iki program:** Rectangle (~18 satır, dikdörtgen alanı) ve Vehicle (~21–22 satır, aracı hızlandırma). Her programdan sonra bir anlama sorusu sorulmuş.
- **Dil katılımcıya bırakılmış:** Aynı programların Java, Python ve Scala sürümleri var. %95,8 Java seçmiş. Düzeltilmiş veride Python'da sadece 2–4 kişi var.
- **Gösterim sırası herkeste aynı değil:** Düzeltilmiş veride Rectangle bazı katılımcılarda 2., bazılarında 5. denemede. EMIP sitesi de metadata'da gösterim sırasının ayrı bir alan olduğunu yazıyor.
- **Java'nın iki farklı ekran görüntüsü var** (`rectangle_java` / `rectangle_java2`, `vehicle_java` / `vehicle_java2`):
  - 29 kişi birinci, yaklaşık 100 kişi ikinci sürümü görmüş; ikisini birden gören yok.
  - Kod aynı, ama ekrandaki konum ve yazı boyutu farklı (aynı `class` token'ının genişliği 55 ve 47 piksel).
  - Vehicle'da sürümlerden biri 22, diğeri 21 satır. Peitek'teki fazla `System.out.println` satırı bununla ilgili olabilir; görüntüye bakılmadı.

**Sonuç:** "Aynı kod" koşulu sağlanıyor. AOI'ler piksel koordinatıyla değil kod bloğu üzerinden tanımlanmalı, yoksa ekran düzenleri uyuşmaz.

## 2. EMIP ve Peitek'te ortak kod

Rectangle ve Vehicle sınıfları EMIP'te ve Peitek vd. 2020'de aynı (iki dosya yan yana karşılaştırıldı).

- **Düzen farkı:** EMIP'te `width()`, `height()`, `area()` tek satırda; Peitek'te çok satırlı. Satır AOI'leri birebir eşleşmiyor, metot/blok AOI'leri eşleşiyor. Bu, DEC-22 / DEC-40'taki blok seviyesi AOI fikrini destekliyor.
- **Peitek'in 10 programı:** Peitek, 8'inin Busjahn vd.'den alındığını yazıyor.

## 3. Düzeltilmiş (corrected) EMIP nedir?

EMIP'in, EMIP-Toolkit ekibinin (Al Madi, Guarnera, Sharif, Maletic, ETRA 2021) işleyip temizlediği sürümü. Yeni deney değil.

| | Ham EMIP | Düzeltilmiş EMIP |
|---|---|---|
| Veri | Saniyede 250 bakış noktası (x, y, zaman) | Fixation listesi (zaman, süre, x, y) |
| Kod eşleşmesi | Yok, sadece piksel | Her fixation'ın satırı, token'ı ve srcML etiketi hazır |
| Katılımcı | 216 | 159 |
| Deneyim etiketi | Metadata dosyasında | Yok, katılımcı numarasıyla metadata'dan eşlenir |
| Nerede | OSF | EMIP-Toolkit GitHub reposu |

- Dosyada 61.799 fixation var.
- Neden 159 kişi kaldığı yazılmamış. Bir `quality` sütunu var, düşük kaliteli kayıtlar elenmiş olabilir.
- **Kullanım:** STA prototipine hızlı başlamak için düzeltilmiş sürüm, nihai model için ham EMIP.

## 4. STA ham gaze mi istiyor?

Hayır. Eraslan'ın orijinal kodu (`github.com/SukruEraslan/sta`) okundu. STA iki dosya istiyor:

1. **Katılımcı başına fixation listesi:** `Index, Time, Duration, XPoint, YPoint, PageName`.
2. **AOI tanım dosyası:** her AOI için ad, x, genişlik, y, yükseklik, harf.

STA, fixation'ları AOI'lerle eşlerken cihaz doğruluğuna göre kutuları biraz büyütüyor (eye tracker doğruluğu ve ekran çözünürlüğü parametre).

Bütün hat:

```
ham gaze → fixation tespiti (I-DT vb.) → fixation listesi → STA (AOI eşleme + trending path)
```

**Ham gaze yine de neden önemli?** STA istediği için değil, tutarlılık için:

- Adayın webcam verisi ham gaze olarak gelecek, fixation'ları biz çıkaracağız.
- Trending path'lerin çıktığı veri setindeki fixation'lar da aynı algoritma ve eşiklerle üretilmeli.
- Birden fazla veri seti birleşirse (EMIP 250 Hz, Peitek 60 Hz) hepsinde aynı algoritma çalıştırılmalı.

**Not:** Orijinal `STA.py` Python 2 ile yazılmış (Burcu'yla konuşulacak).

## 5. EMIP'teki deneyim soruları

Ankette iki ilgili soru var:

- **Öz değerlendirme:** "Seçtiğin dilde uzmanlığını nasıl değerlendirirsin?" Cevaplar: yok %13,9 (~30), düşük %31,9 (~69), orta %46,3 (~100), yüksek %7,9 (~17).
- **Yıl:** "Kaç yıldır programlama yapıyorsun?" Aljehane vd. 2023 ortanca 4 yılda bölmüş: 101 expert, 90 novice (deneyimi 0 olan 16 kişi çıkarılmış).

Karar durumu: [hoca-yazismalari.md](hoca-yazismalari.md).
