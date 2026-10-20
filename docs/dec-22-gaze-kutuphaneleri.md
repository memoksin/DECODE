# DEC-22 — Webcam gaze kütüphaneleri ve doğruluk

Durum: araştırma bitti, test DEC-39'da (20 Ekim 2026). Kod yok.

## Kısıtımız

- Girdi: Meet'ten gelen aday kamerası (720p varsayılan, sıkıştırılmış). Kütüphane kamerayı kendisi açamaz, hazır kare almalı.
- Kalibrasyon: adayın paylaştığı ekrandaki noktalar (bkz. `dec-16-meet-yakalama.md`).

## Adaylar

| Kütüphane | Çalıştığı yer | Hata | Durum |
|---|---|---|---|
| WebGazer.js | Tarayıcı | 3.65–4.17° [1][2] | Elendi: kamerayı kendisi açar, bakımı Şubat 2026'da bitti [3], GPLv3 |
| MediaPipe Face Landmarker + kendi regresyonumuz | Tarayıcı (JS/WASM) | Yayınlanmış rakam yok [4] | Test: video makineden çıkmaz (F8) |
| L2CS-Net | Python (PyTorch) | 3.92° MPIIGaze [5] | Test: MIT [6], hazır kare alır, GPU gerekebilir |
| ETH-XGaze | Python | ~4.5° [7] | Yedek |
| OpenFace 2.0 | C++ | — | Yedek, ticari olmayan lisans [8] |

## Satır mı blok mu?

- ~60 cm'de 1° ≈ 35–45 px. Bir kod satırı ≈ 20 px ≈ 0.5°.
- Webcam hatası 2–4° → hata bir satırın 4–8 katı. Satır seviyesi gerçekçi değil.
- Fang et al. 2026: webcam kod okumada semantik desenleri yakalıyor, token seviyesinde zorlanıyor; offsite gürültü daha yüksek [9].
- Öneri: **kod bloğu AOI'leri** (fonksiyon, döngü, koşul). Ekip + hocalarla netleşecek.

## Sıkıştırma

- Sıkıştırmanın webcam gaze doğruluğuna etkisini ölçen çalışma bulunamadı → DEC-37 bu boşluğu doldurur.
- Kalibrasyon düşük çözünürlükte doğruluğu belirgin artırıyor [10].

## Açık sorular (toplantı)

- AOI blok seviyesinde olsun mu? STA trending path'leri dataset'in AOI'lerine bağlı; dataset satır seviyesindeyse bloklara toplanabilir mi?
- Gaze tarayıcıda mı, yerel Python servisinde mi? → DEC-39 sonucu.
- Mülakat kodu dataset kodundan farklı olacak → AOI'ler kod parçasından bağımsız (semantik bloklar) olmalı. Sonraki sprint: DEC-40.

## Kaynaklar

1. https://jeffhuang.com/papers/WebGazer_IJCAI16.pdf
2. https://studenttheses.uu.nl/handle/20.500.12932/40709
3. https://github.com/brownhci/WebGazer
4. https://developers.google.com/edge/mediapipe/solutions/vision/face_landmarker
5. https://arxiv.org/pdf/2203.03339
6. https://github.com/Ahmednull/L2CS-Net
7. https://arxiv.org/html/2007.15837
8. https://github.com/TadasBaltrusaitis/OpenFace
9. Fang et al. (2026), IEEE TSE. https://doi.org/10.1109/TSE.2026.3651615
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC8347006
