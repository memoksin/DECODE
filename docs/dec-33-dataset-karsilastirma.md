# DEC-33 — Public eye-tracking dataset karşılaştırma tablosu

Hazırlayan: Sude. Tarih: 24 Ekim 2026. Durum: **taslak**, her satır kaynağından kontrol edildi, `?` olanlar doğrulanacak.

Kriterler (Toplantı 2, 21 Ekim): birleştirilecek dataset'lerde aynı dil, expert/non-expert etiketi, aynı task (okuma / merge). Kapsam: geniş tarama. Uymayanlar da tabloda, nedeniyle birlikte.

## Karşılaştırma tablosu

| Dataset | Dil | Katılımcı | Deneyim etiketi | Ham gaze (x, y, zaman) | Aynı kod mu? | Lisans | Cihaz | Link | Durum |
|---|---|---|---|---|---|---|---|---|---|
| **EMIP** (Bednarik vd. 2020) | Java (%95,8), Python, Scala | 216 (makale); site: 269 katıldı, 254 kaldı (A) | Öz bildirim (yok/düşük/orta/yüksek) + yıl. Aljehane vd. 2023: medyan 4 yıl → 101 expert, 90 novice (Java) | Evet. Katılımcı başına TSV; Time, POR X/Y (piksel) ve diğer alanlar | Evet. 2 program: Rectangle, Vehicle | Makale: CC-BY-NC-SA. Site: CC BY 4.0 (B) | SMI RED250, 250 Hz | [osf.io/53kts](https://osf.io/53kts/), [emipws.org](https://www.emipws.org/dataset/) | **Ana aday** |
| **EMIP düzeltilmiş** (Al Madi vd. 2021) | Aynı | Aynı | Aynı | Token seviyesinde düzeltilmiş sürüm; kolonlar ? | Evet | Belirtilmemiş | SMI RED250 | [osf.io/djn9s](https://osf.io/djn9s) | **Ana aday** (içerik doğrulanacak) |
| **Peitek vd. 2020** (ICPC, okuma sırası) | Java | 12 novice (3 elendi) + 19 intermediate | Grup: novice / intermediate (lisansüstü). "Expert" yok | Evet, katılımcı başına CSV; kolonlar ? | 10 Java programı (anlamlı + obfuscated sürüm); katılımcıya dağılım ? | CC-BY-SA-4.0 | Tobii EyeX, 60 Hz | [GitHub](https://github.com/brains-on-code/eyetracking-linearity-replication/) | **Aday** (etiket uyumu tartışılmalı) |
| **Busjahn vd. 2015** (doğrusal olmayan okuma) | Java (+ İngilizce pseudo-kod) | 14 novice + 6 expert | Novice / expert (5–28 yıl deneyimli profesyonel) | ? | Novice 3 program, expert 6 program görmüş; 2'si ortak | ? | SMI RED-m, 120 Hz | Veri linki bulunamadı | **Belirsiz** (veri erişimi yok) |
| **Fang vd. 2026** (webcam + Tobii) | ? | 49 | Sayfada yok | CSV; zaman ve gaze alanları var, birim ? | ? (kod fonksiyonları) | Belirtilmemiş | Tobii Pro + WebGazer | [IEEE DataPort](https://ieee-dataport.org/documents/investigating-feasibility-conducting-webcam-based-eye-tracking-studies-code-comprehension) | **Belirsiz** (abonelik gerekiyor, dosya yüklenmemiş notu var) |
| **EyeTrans** (Zhang vd. 2024) | Java | 27 | Yok. Öğrenciler, Data Structures + Java testi geçmiş | Ham veri var denmiş; kolonlar ? | Hayır. 162 metot, kişi başı 24–25 | CC BY 4.0 | Tobii Pro Fusion, 60 Hz | [Zenodo](https://zenodo.org/records/10684985) | **Elendi**: etiket yok, task özetleme |
| **EyeContext** (Bansal vd.) | Java | 10 | Yok (en az 1 yıl Java, ort. 2,8) | ? | Hayır. 5 proje, 40 özet | Belirtilmemiş | Tobii Pro Fusion, 120 Hz | [Zenodo](https://zenodo.org/records/14873017) | **Elendi**: etiket yok, task özetleme |

(A) ve (B): aşağıdaki "Çelişkiler" bölümünde.

## Veri paylaşımı belirtilmeyen çalışmalar

| Çalışma | Bilinenler | Not |
|---|---|---|
| Ahsan & Obaidellah 2023 [4] (ETRA) | 66 CS lisans öğrencisi, hepsi novice; yüksek / düşük performanslı diye ayrılmış. Dil ve cihaz özet sayfasında yok | Veri linki yok. Yazarlara sorulabilir |
| Tablatin & Rodrigo (ICCE) | Yüksek / düşük performanslı öğrenciler, hata bulma, STA with tolerance | Katılımcı sayısı, dil, cihaz ve veri durumu sayfada yok |
| Ahsan & Obaidellah 2025 [3] (TOCE) | Sayfa açılmadı | PDF'ten okunacak |
| Aljehane vd. 2023 [1] | EMIP'in Java kısmını analiz etmiş | Yeni veri seti değil, [OSF](https://osf.io/rsqdx/) (sayfa açılmadı) |

## Çelişkiler ve eksikler

- **(A) EMIP katılımcı sayısı:** Makale 216 diyor. Sitede 269 kişi katılmış, 15'i elenmiş, 254 kalmış, verinin %15'i yayınlanmamış. Hangisini yazacağımıza karar verilecek.
- **(B) EMIP lisansı:** Makale CC-BY-NC-SA, site CC BY 4.0. Sitedeki daha serbest. Raporda ikisini de belirtip siteye atıf yapmak güvenli.
- **EMIP kolonları:** Sitede SMI formatı anlatılıyor (Time, Type, L/R POR X/Y piksel). Ham dosyayı açıp doğrulamadık.
- **EMIP-Toolkit** README'si dört dataset sayıyor (EMIP2020, AlMadi2018, McChesney2021, AlMadi2021). EMIP dışındakilerin dil, katılımcı ve etiket bilgisi alınamadı, bakılacak.
- **Busjahn:** Makalede örnek olarak bir `Vehicle` sınıfı var. EMIP'in `Vehicle`'ıyla aynı kod mu, kontrol edilecek.
- **Peitek:** Etiket "intermediate". Toplantıdaki expert/non-expert kriteriyle birebir uyuşmuyor.

## İlk okuma (kriterlere göre)

- Hepsi Java: dil kriteri sağlanıyor.
- Etiketli ve kod okuma task'lı olanlar: EMIP, Peitek, Busjahn.
- Aynı kodu paylaşma ihtimali olan tek ikili: EMIP ve Busjahn (kontrol edilecek).
- Veri azsa ne olur, AI ile veri üretimi: DEC-46'da ele alınacak.

## Kaynaklar

- Bednarik vd. 2020, EMIP, Science of Computer Programming 198: [emipws.org](https://www.emipws.org/dataset/), [makale](https://par.nsf.gov/servlets/purl/10251907)
- Al Madi vd. 2021, EMIP Toolkit, ETRA '21: [GitHub](https://github.com/MyNameBeJohn/EMIP-Toolkit)
- Aljehane, Sharif, Maletic 2023, ETRA: [PDF](https://www.cs.kent.edu/~jmaletic/papers/ETRA2023.pdf)
- Peitek, Siegmund, Apel 2020, ICPC: [PDF](https://www.se.cs.uni-saarland.de/publications/docs/PSA20.pdf), [GitHub](https://github.com/brains-on-code/eyetracking-linearity-replication/)
- Busjahn vd. 2015: [PDF](https://huang.isis.vanderbilt.edu/cs8395-f23/paper/linear-order-eye.pdf)
- Fang vd. 2026: [IEEE DataPort](https://ieee-dataport.org/documents/investigating-feasibility-conducting-webcam-based-eye-tracking-studies-code-comprehension)
- EyeTrans: [arXiv](https://arxiv.org/pdf/2402.14096), [Zenodo](https://zenodo.org/records/10684985)
- EyeContext: [arXiv](https://arxiv.org/html/2405.18573v2), [Zenodo](https://zenodo.org/records/14873017)
- Ahsan & Obaidellah 2023: [doi](https://doi.org/10.1145/3588015.3589193)
- Tablatin & Rodrigo: [ICCE](https://library.apsce.net/index.php/ICCE/article/view/3660)
