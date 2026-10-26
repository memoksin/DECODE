# DEC-33 — Public eye-tracking dataset karşılaştırma tablosu

Hazırlayan: Sude. Güncelleme: 24 Ekim 2026. Durum: **taslak v4** (AOI seviyesi sütunu eklendi, Mehmet'in DEC-33 yorumu).

Kriterler (Toplantı 2, 21 Ekim): birleştirilecek dataset'lerde aynı dil, expert/non-expert etiketi, aynı task (okuma / merge). Kapsam: geniş tarama. Uymayanlar da tabloda, nedeniyle birlikte.

Doğrulama düzeyi: 📂 = veri dosyası açılıp kontrol edildi, 📄 = makale veya veri sayfasından, `?` = bulunamadı.

## Karşılaştırma tablosu

| Dataset | Dil | Katılımcı | Deneyim etiketi | Ham gaze (x, y, zaman) | Aynı kod mu? | AOI seviyesi | Lisans | Cihaz | Link | Durum |
|---|---|---|---|---|---|---|---|---|---|---|
| **EMIP** — Bednarik vd. 2020 | Java (%95,8), Python, Scala | 216 yayında 📄 | Öz değerlendirme (yok / düşük / orta / yüksek) + programlama yılı 📄 | Var. Katılımcı başına TSV: `Time`, `R POR X/Y [px]`, geçerlilik 📂 (EMTK parser) | Evet: Rectangle, Vehicle | Token, satır numarasıyla (EMIP-Toolkit AOI dosyası) 📂; bloklara toplanabilir | Makale: CC BY-NC-SA; site: CC BY 4.0 | SMI RED250, 250 Hz | [osf.io/53kts](https://osf.io/53kts/) | **Ana aday** |
| **EMIP düzeltilmiş** — Al Madi vd. 2021 | Java (fixation'ların %99'u), Python | 159 📂 | Dosyada yok. EMIP metadata ile katılımcı no'su üzerinden eşlenir | Yok. Fixation seviyesi: zaman, süre, x, y + token, satır, srcML AOI 📂 | Evet: Rectangle, Vehicle | Token ve satır 📂; bloklara toplanabilir | Belirtilmemiş | SMI RED250 | [EMIP-Toolkit (GitHub)](https://github.com/nalmadi/EMIP-Toolkit), [osf.io/djn9s](https://osf.io/djn9s) | **Ana aday** (AOI hazır) |
| **Peitek vd. 2020** — okuma sırası | Java | 12 novice + 19 experienced 📂 | Grup: novice / experienced (makalede "intermediate"). Java yılı medyan 3 / 6 📂 | Var. CSV: `Time; Gaze.X; GazeY` 📂 | Evet: 10 program herkese, her biri normal ya da karıştırılmış sürümde 📂. Rectangle ve Vehicle EMIP ile aynı kod 📂 | Satır ve blok, bloklar hazır (Rectangle: 29 satır, 6 blok) 📂 | CC BY-SA 4.0 📂 | Tobii EyeX, 60 Hz | [GitHub](https://github.com/brains-on-code/eyetracking-linearity-replication) | **Aday (güçlü)** |
| **Busjahn vd. 2015 / Al Madi vd. 2021** — uzunlamasına | Java + pseudo-kod + doğal metin | 14 novice + 6 expert 📄 | Novice: önceki deneyim yok. Expert: 5–28 yıl profesyonel 📄 | ? | Kısmen: expert'ler 6 program, 2'si novice'lerle ortak 📄 | Token (Al Madi vd. 2021) 📄; veri kontrol edilmedi | ? | SMI RED-m, 120 Hz | [osf.io/t5je9](https://osf.io/t5je9/overview) (makaleden; içerik okunamadı) | **Aday** (veri doğrulanacak) |
| **McChesney & Bond 2021** — disleksi | Java 📂 | 30 (14 disleksili, 16 değil) 📂 | Novice/expert grubu yok. Öz değerlendirme: düşük 3, orta 24, yüksek 3; yıl 0,5–10 📂 | Var. Tobii TSV: zaman, `Gaze point X/Y`, fixation/saccade, AOI isabeti 📂 | Evet: 3 kısa program, sıkışık ya da aralıklı düzen 📂 | Satır (L01…) ve kod parçası (`i++`, `int i = 0;`) 📂; bloklara toplanabilir | Makale CC BY; veri ? | Tobii, 120 Hz 📂 | [figshare](https://doi.org/10.6084/m9.figshare.c.5304473), EMIP-Toolkit içinde | **Yardımcı** (etiket dengesiz) |
| **Abid vd. 2019** — Java metot özetleme | Java | 13 novice + 5 expert 📄 | Expert: 5+ yıl veya açık kaynak katkılı doktora öğrencisi. Novice: ~1 yıl 📄 | İşlenmiş gaze (iTrace) 📄; paket içeriği ? (12,7 MB zip) | Hayır: 63 metot, kişi başı ~15, IDE'de serbest gezinme 📄 | Satır ve sütun (iTrace) 📄 | CC BY-ND 4.0 📄 | Tobii X60, 60 Hz | [Zenodo 2550768](https://doi.org/10.5281/zenodo.2550768) | **Yardımcı** (task özetleme) |
| **Fang vd. 2026** — webcam + Tobii | ? | 49 laboratuvarda + 10 uzaktan 📄 | Yok | CSV, zaman ve gaze alanları; birim ? 📄 | ? | ? | ? | Tobii Pro + WebGazer | [IEEE DataPort](https://ieee-dataport.org/documents/investigating-feasibility-conducting-webcam-based-eye-tracking-studies-code-comprehension) | **Elendi** (abonelik gerekiyor, etiket yok). Webcam referansı olarak kalır |
| **EyeTrans** — Zhang vd. 2024 | Java | 27 📄 | Yok (öğrenciler, Java testini geçmiş) | "İşlenmemiş veri" denmiş 📄 | Hayır: 162 metot, kişi başı 24–25 | Token 📄 | CC BY 4.0 | Tobii Pro Fusion, 60 Hz | [Zenodo 10684985](https://zenodo.org/records/10684985) | **Elendi** (etiket yok, task özetleme) |
| **EyeContext** — Wallace vd. | Java | 10 📄 | Yok (ort. 2,8 yıl Java) | ? | Hayır: 5 proje, 40 özet | Token 📄 | ? | Tobii Pro Fusion, 120 Hz | [Zenodo 14873017](https://zenodo.org/records/14873017) | **Elendi** (etiket yok, task özetleme) |
| **AlMadi2018** | Kod yok, İngilizce cümleler 📂 | 8 📂 | ? | Var (EyeLink ASC) 📂 | — | — (metin) | ? | EyeLink 1000 | EMIP-Toolkit içinde | **Elendi** (kod okuma değil) |

## Verisi paylaşılmamış çalışmalar

| Çalışma | Bilinenler | Not |
|---|---|---|
| Ahsan & Obaidellah 2023 [4] | 66 lisans öğrencisi, hepsi novice; yüksek / düşük performanslı | Veri linki yok, yazarlara sorulabilir |
| Ahsan & Obaidellah 2025 [3] | — | Makale sayfası açılmadı, PDF'ten okunacak |
| Tablatin & Rodrigo (ICCE) | Yüksek / düşük performanslı öğrenciler, hata bulma, STA with tolerance | Katılımcı, dil ve veri bilgisi sayfada yok |
| Obaidellah vd. 2020 (ETRA) | 51 lisans öğrencisi, 6 pseudo-kod görevi | Etiket ve veri bilgisi yok |
| Aljehane vd. 2023 [1] | EMIP'in Java kısmı: medyan 4 yıl ile 101 expert, 90 novice | Yeni veri değil, EMIP'i kullanıyor |

## Bulgular

**1. Aynı kod üç veri setinde.** Rectangle ve Vehicle Java sınıfları EMIP'te ve Peitek'te aynı (iki dosya karşılaştırıldı). Peitek, programlarının 8'inin Busjahn vd.'den alındığını yazıyor; Busjahn makalesinde de Vehicle örneği var. Toplantıdaki "aynı kod için 10 expert + 10 novice" koşulu bu iki kodla sağlanabilir:

- EMIP: 216 katılımcı
- Peitek: 31 katılımcı, novice ve experienced grupları hazır
- Busjahn: 20 katılımcı, doğrulanacak

**2. Kod aynı, düzen farklı.** EMIP'te `width()`, `height()` ve `area()` metotları tek satırda; Peitek'te çok satırlı. Satır AOI'leri birebir eşleşmiyor, metot/blok AOI'leri eşleşiyor. Bu, DEC-22 ve DEC-40'taki blok seviyesi AOI fikrini destekliyor. Vehicle'da Peitek'te bir `System.out.println` satırı fazla görünüyor; EMIP görüntüsünden kontrol edilmeli.

**3. Cihazlar farklı.** 250, 120 ve 60 Hz olan cihazlar var. Birleştirirken fixation'ları her veri setinde aynı algoritmayla (I-DT, aynı eşikler) ham gaze'den yeniden çıkarmak gerekir. Bu yüzden ham gaze sütunu kritik. Düzeltilmiş EMIP sadece fixation içeriyor.

**4. Etiketler farklı.**

- EMIP: öz değerlendirme ve yıl
- Peitek ve Busjahn: grup
- McChesney: öz değerlendirme

Ortak bir "expert" kuralı gerekiyor (aşağıdaki karar 1).

**5. Önceki çelişki çözüldü.** EMIP sitesi 254 geçerli katılımcı ve %15 yayınlanmamış veri diyor; 254 × 0,85 ≈ 216, yani makaledeki sayı. Raporda 216 yazılabilir.

## Kararlar

1. **EMIP'te expert tanımı — beklemede.** Şükrü Hoca'nın önerdiği seçenekler (24 Ekim):
   - (a) Öz değerlendirmede "yüksek" diyen 17 kişi + diğerlerinden rastgele seçilen 17 kişi; her gruba ayrı trending path.
   - (b) 4 yıl ve üstü / altı (Aljehane vd.): 101 expert, 90 novice.

   SRS'te iki seçenek de yazıldı, seçim Sprint 2'de yapılacak.
2. **Peitek grupları — karar verildi (24 Ekim, Şükrü Hoca).** Yazarların novice / experienced ayrımı olduğu gibi kullanılır.

Hocanın notları: Peitek'te daha çok Java kodu var, EMIP'te katılımcı sayısı daha fazla. EMIP'teki diğer diller farklı dilleri de dahil etme şansı verebilir; ama Aljehane vd.'ye göre Python'da 5, Scala'da 4 katılımcı var.
3. **EMIP lisansı — karar verildi (24 Ekim):** Raporda iki kaynak da gösterilir. Makale (Bednarik vd. 2020) CC BY-NC-SA, emipws.org CC BY 4.0 diyor.

**Lisans notu (Abid vd. 2019):** CC BY-ND 4.0 "türev yok" demek. Veriyi analiz etmek sorun değil, ama değiştirilmiş veriyi yeniden paylaşmak kısıtlı. Yardımcı veri olarak kullanılırsa raporda belirtilmeli.

## Açık kalanlar

- EMIP ham dosyası ve `emip_metadata.csv` (OSF) çalışma alanından indirilemedi. Kolon bilgisi EMTK parser kodundan ve site açıklamasından.
- Busjahn/Al Madi OSF (t5je9): sayfa JavaScript ile yükleniyor, dosya listesi ve lisans okunamadı. Tarayıcıdan bakılıp dosya listesi not edilmeli.
- Abid Zenodo (2550768): lisans ve dosya boyutu doğrulandı. Zip'in içi (ham gaze mi, fixation mı) açılmadı.
- McChesney figshare sayfası açılamadı; Tobii modeli ve veri lisansı ?.
- Veri azsa ne olur, AI ile veri üretimi: DEC-46.

## Kaynaklar

- Bednarik vd. 2020, *EMIP*, Science of Computer Programming 198: [emipws.org](https://www.emipws.org/dataset/), [makale](https://par.nsf.gov/servlets/purl/10251907)
- Al Madi, Guarnera, Sharif, Maletic 2021, *EMIP Toolkit*, ETRA '21: [GitHub](https://github.com/nalmadi/EMIP-Toolkit), [düzeltilmiş veri](https://www.emipws.org/corrected-dataset/)
- Peitek, Siegmund, Apel 2020, ICPC: [PDF](https://www.se.cs.uni-saarland.de/publications/docs/PSA20.pdf), [GitHub](https://github.com/brains-on-code/eyetracking-linearity-replication)
- Busjahn vd. 2015, *Eye Movements in Code Reading: Relaxing the Linear Order*, ICPC: [PDF](https://huang.isis.vanderbilt.edu/cs8395-f23/paper/linear-order-eye.pdf)
- Al Madi, Peterson, Sharif, Maletic 2021, *From Novice to Expert*, ICPC (aynı veri, novice/expert sınıflandırma %72): [PDF](https://par.nsf.gov/servlets/purl/10267218)
- McChesney & Bond 2021, ETRA: [Ulster](https://pure.ulster.ac.uk/en/publications/eye-tracking-analysis-of-code-layout-crowding-and-dyslexia-an-ope/)
- Abid vd. 2019, ICSE: [arXiv](https://arxiv.org/pdf/1903.03358)
- Fang vd. 2026, IEEE TSE: [Vanderbilt](https://www.vanderbilt.edu/valiant/2026/02/25/investigating-the-feasibility-of-conducting-webcam-based-eye-tracking-studies-in-code-comprehension), [IEEE DataPort](https://ieee-dataport.org/documents/investigating-feasibility-conducting-webcam-based-eye-tracking-studies-code-comprehension)
- Zhang vd. 2024, *EyeTrans*, FSE: [arXiv](https://arxiv.org/pdf/2402.14096)
- Wallace vd., *Programmer Visual Attention During Context-Aware Code Summarization*: [arXiv](https://arxiv.org/html/2405.18573v2)
- Aljehane, Sharif, Maletic 2023, ETRA: [PDF](https://www.cs.kent.edu/~jmaletic/papers/ETRA2023.pdf)
- Ahsan & Obaidellah 2023, ETRA: [doi](https://doi.org/10.1145/3588015.3589193)
- Obaidellah vd. 2020, ETRA: [UM eprints](https://eprints.um.edu.my/37134)
- Tablatin & Rodrigo, ICCE: [sayfa](https://library.apsce.net/index.php/ICCE/article/view/3660)
