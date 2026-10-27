# Sude — çalışma klasörü

Rol: Literatür + Veri (`literatur-veri`). Veri hattı (ham gaze → fixation → scanpath), AOI tanımı, dataset'ler, Related Work dataset kısmı.

## Bu klasörde

| Dosya | İçerik |
|---|---|
| [dec-33-dataset-karsilastirma.md](dec-33-dataset-karsilastirma.md) | DEC-33 çalışma notu (Türkçe): 10 veri setinin tam karşılaştırması, doğrulama düzeyi, bulgular, kararlar, kaynaklar |
| [bulgular-emip-sta.md](bulgular-emip-sta.md) | EMIP'te aynı kod, EMIP ile Peitek'te ortak kod, düzeltilmiş EMIP, STA'nın girdi formatı, EMIP deneyim soruları |
| [hoca-yazismalari.md](hoca-yazismalari.md) | Şükrü Hoca'nın uzmanlık ayrımı önerileri, EMIP lisans kararı |
| [DEC-33-related-work-datasets.docx](DEC-33-related-work-datasets.docx) | SRS dataset bölümünün Word hali (rapora yapıştırmak ve hocaya göndermek için) |
| [DEC-33-Table1-datasets.docx](DEC-33-Table1-datasets.docx) | Table 1'in son hali (AOI level sütunuyla), rapora kopyalamak için |

SRS bölümünün kendisi ekibin düzenine uygun olarak [docs/srs/related-work-datasets.md](../srs/related-work-datasets.md) içinde (İngilizce, iki tablo, yöntem paragrafı, 13 kaynak).

## Atanan işler (Linear, 26 Ekim 2026)

Cycle 1: 23–27 Ekim. SRS teslimi 27 Ekim 22:55. Tahmin: 1 puan = 1 saat.

| Anahtar | İş | Proje | Puan | Durum (Linear) | Not |
|---|---|---|---|---|---|
| DEC-29 | SRS 1.4.3 User characteristics | SRS Raporu | 1 | Done (⏱ 2h) | En fazla 3 kullanıcı tipi; programlama geçmişi, erişilebilirlik. 26 Ekim'de daraltıldı |
| DEC-47 | SRS 2.3 Usability requirements | SRS Raporu | 1 | Done (⏱ 2h) | Yeni (26 Ekim, DEC-25'ten ayrıldı). En fazla 3 ölçülebilir metrik (effectiveness, efficiency, satisfaction), her birine 1 gerekçe; 1.4.3 ile tutarlı. Burcu'nun taslağı: `docs/DEC 25.md` |
| DEC-50 | SRS 1.4.4 Limitations | SRS Raporu | 1 | Done (⏱ 1h) | Yeni (26 Ekim, DEC-29'dan ayrıldı). 3–5 madde |
| DEC-51 | SRS 1.4.5 Assumptions and dependencies | SRS Raporu | 1 | Done (⏱ 1.5h) | Yeni (26 Ekim, DEC-29'dan ayrıldı). 2–3 varsayım + 2–3 bağımlılık |
| DEC-30 | SRS sunumu (11 slayt) | SRS Raporu | 3 | Todo | Son tarih 27 Ekim |
| DEC-33 | Public eye-tracking dataset listesi + karşılaştırma tablosu | Dataset | 4 | Done (⏱ 4h) | Taslak hazır. Mehmet tabloya "AOI seviyesi" sütunu istiyor (aşağıda) |
| DEC-46 | Veri az olursa: birleştirme kriterleri ve AI ile veri üretme | Dataset | 2 | Todo | |
| DEC-28 | Yeni tarama: göz takibiyle deneyim sınıflandırma + Yeliz Hoca'nın makalesi ve atıfları | Literatür Taraması | 6 | Todo | Mehmet'in önerisi: Fang vd. 2026 |
| DEC-27 | 6 proposal makalesini oku | Literatür Taraması | 6 | Paused | |
| DEC-40 | Kod parçasından bağımsız (code-agnostic) AOI ve trending path | Teknik Araştırma | — | Backlog | Sprint 1 dışı |

**Mehmet'in DEC-33 yorumu (25 Ekim):** Dataset tablosuna **AOI seviyesi** sütunu (satır / blok / yok) eklenmeli. DEC-45 kararıyla adayın bakışı kod bloklarına eşlenecek; trending path aynı birimde olmalı. Satır seviyesindeki dataset'lerin bloklara toplanıp toplanamayacağı da not edilmeli. Açık soru DEC-40'ta.

**DEC-40'taki sorular:**

- Dataset'teki satır AOI'leri semantik bloklara (fonksiyon imzası, döngü, koşul, return) nasıl eşlenir?
- Farklı kod parçalarından gelen scanpath'ler tek trending path'te birleşebilir mi?
- Literatürde içerikten bağımsız AOI ile STA kullanımı var mı?

## Çalışma günlüğü

### 24 Ekim 2026

- **DEC-33 veri seti taraması:**
  - 10 veri seti karşılaştırıldı.
  - EMIP-Toolkit, Peitek ve McChesney verileri indirilip dosyalardan kontrol edildi.
- **Ana bulgu:** Rectangle ve Vehicle sınıfları EMIP ve Peitek'te aynı kod. Satır düzeni farklı, bu yüzden blok AOI gerekiyor.
- **Çözülen çelişki:** EMIP'te 216 / 254 katılımcı farkı (254'ün %15'i yayınlanmamış, kalan 216).
- **STA girdisi:** STA ham gaze değil fixation listesi istiyor. Ham gaze tutarlılık için gerekli.
- **SRS dataset bölümü** İngilizce hazırlandı (iki tablo + yöntem paragrafı), Word hali üretildi.
- **Kararlar:**
  - EMIP lisansı: iki kaynak da gösterilir.
  - Peitek grupları: olduğu gibi kullanılır (Şükrü Hoca).
- **Şablon incelemesi:** CNG491 SRS şablonu incelendi. Tablonun yeri büyük ihtimalle 1.3 Related Work (Burcu, DEC-36).

### 26 Ekim 2026

- Bu klasör açıldı, tüm çalışmalar buraya toplandı.
- Linear bağlandı; atanan işler, Mehmet'in DEC-33 yorumu ve DEC-40 eklendi.
- DEC-29 (1.4.3) yazıldı ve rapora eklendi: Interviewer ve Candidate paragrafları. Linear'da Done, ⏱ 2h.
- DEC-47 (2.3) yazıldı ve rapora eklendi: Burcu'nun 3 metriği düzeltildi (snippet seçme, SUS 75 = B). Linear'da Done, ⏱ 2h.
- DEC-50 (1.4.4) başladı.

### 27 Ekim 2026

- DEC-33: Mehmet'in istediği "AOI level" sütunu eklendi. Peitek'te blok AOI'leri hazır; EMIP ve McChesney'deki token/satır AOI'leri bloklara toplanabilir. Mehmet'e cevap yazıldı, Linear'da Done.
- DEC-50 (1.4.4) rapora taslaktaki haliyle eklendi (5 madde), Linear'da Done.
- DEC-51 (1.4.5) yazıldı: 3 varsayım + 3 bağımlılık. Linear'da Done, ⏱ 1.5h.

## Açık işler

- [ ] EMIP'te expert tanımı: "yüksek" 17 + rastgele 17 mi, 4 yıl kuralı mı? (Sprint 2)
- [ ] Tablonun SRS'teki yerini netleştir; bölümü ve 13 kaynağı Burcu'ya ilet (DEC-36, DEC-34)
- [ ] Busjahn / Al Madi OSF (t5je9) dosya listesini tarayıcıdan kontrol et
- [ ] EMIP ham dosyası ve `emip_metadata.csv` indirilecek (OSF)
- [x] DEC-29, DEC-50, DEC-51: 1.4.3–1.4.5 yazıldı
- [ ] DEC-30: SRS sunumu (27 Ekim)
- [x] DEC-33: tabloya "AOI seviyesi" sütunu eklendi (Mehmet'in yorumu)
- [x] DEC-33 süre yorumu yazıldı (⏱ 4h)
- [ ] DEC-46: veri az olursa ne olur, AI ile veri üretimi
