# Sude — çalışma klasörü

Rol: Literatür + Veri (`literatur-veri`). Veri hattı (ham gaze → fixation → scanpath), AOI tanımı, dataset'ler, Related Work dataset kısmı.

## Bu klasörde

| Dosya | İçerik |
|---|---|
| [dec-33-dataset-karsilastirma.md](dec-33-dataset-karsilastirma.md) | DEC-33 çalışma notu (Türkçe): 10 veri setinin tam karşılaştırması, doğrulama düzeyi, bulgular, kararlar, kaynaklar |
| [bulgular-emip-sta.md](bulgular-emip-sta.md) | EMIP'te aynı kod, EMIP ile Peitek'te ortak kod, düzeltilmiş EMIP, STA'nın girdi formatı, EMIP deneyim soruları |
| [hoca-yazismalari.md](hoca-yazismalari.md) | Şükrü Hoca'nın uzmanlık ayrımı önerileri, EMIP lisans kararı |
| [DEC-33-related-work-datasets.docx](DEC-33-related-work-datasets.docx) | SRS dataset bölümünün Word hali (rapora yapıştırmak ve hocaya göndermek için) |

SRS bölümünün kendisi ekibin düzenine uygun olarak [docs/srs/related-work-datasets.md](../srs/related-work-datasets.md) içinde (İngilizce, iki tablo, yöntem paragrafı, 13 kaynak).

## Atanan işler (Jira, 24 Ekim 2026)

Güncel takip Linear'da (`CLAUDE.md`); bu liste Jira arşivinden alındı.

| Anahtar | İş | Tahmin | Durum |
|---|---|---|---|
| DEC-27 | 6 proposal makalesini oku | 6h | In Progress |
| DEC-28 | Yeni tarama: göz takibiyle deneyim sınıflandırma + Yeliz Hoca'nın makalesi ve atıfları | 6h | To Do |
| DEC-29 | SRS 1.4.3–1.4.5 User characteristics, limitations, assumptions | 2h | To Do |
| DEC-30 | SRS sunumu (11 slayt), son tarih 27 Ekim | 3h | To Do |
| DEC-33 | Public eye-tracking dataset listesi + karşılaştırma tablosu | 4h | Taslak hazır, PR bekliyor |
| DEC-46 | Veri az olursa: birleştirme kriterleri ve AI ile veri üretme | — | To Do |

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
- Linear bilgileri: connector bağlandıktan sonra eklenecek.

## Açık işler

- [ ] EMIP'te expert tanımı: "yüksek" 17 + rastgele 17 mi, 4 yıl kuralı mı? (Sprint 2)
- [ ] Tablonun SRS'teki yerini netleştir; bölümü ve 13 kaynağı Burcu'ya ilet (DEC-36, DEC-34)
- [ ] Busjahn / Al Madi OSF (t5je9) dosya listesini tarayıcıdan kontrol et
- [ ] EMIP ham dosyası ve `emip_metadata.csv` indirilecek (OSF)
- [ ] DEC-29: 1.4.3–1.4.5 taslağı (1.2 Scope'taki limitasyonlarla çakışmasın; kullanıcılar: Interviewer, Candidate)
- [ ] DEC-30: SRS sunumu (27 Ekim)
- [ ] DEC-33 bitince süre yorumu: `⏱ Xh — not`
- [ ] DEC-46: veri az olursa ne olur, AI ile veri üretimi
