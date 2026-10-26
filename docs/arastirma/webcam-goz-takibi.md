# Webcam ile Göz Takibi — Araştırma Notları

Jira: [DEC-22](https://decode2026.atlassian.net/browse/DEC-22) (epik: DEC-7 Teknik Araştırma)

Kapsam: Webcam tabanlı göz takibi kütüphaneleri ve feature'ları, doğruluk ve sapma (error rate), limitasyonlar, kalibrasyon, bakış noktasını kod satırına eşleme.

İlgili sorular: [Araştırma listesi, bölüm 4](../arastirma-listesi.md#4-webcam-ile-bakış-tahmini-kilometre-taşı-5)

## 1. Kütüphaneler ve Feature'lar

| Kütüphane | Nerede çalışır | Çıktı | Kalibrasyon | Raporlanan doğruluk | Lisans | Bakım durumu |
|---|---|---|---|---|---|---|
| WebGazer.js | | | | | | |
| MediaPipe Face Mesh / Iris | | | | | | |
| L2CS-Net | | | | | | |
| GazeCapture / iTracker | | | | | | |
| OpenFace 2.0 | | | | | | |

Notlar:

## 2. Doğruluk ve Limitasyonlar

- Raporlanan hata değerleri (derece / piksel / cm):
- Satır seviyesinde yeterli mi?
  - Kaba ön hesap (doğrulanacak): 60 cm mesafede 1° ≈ 1 cm ≈ 35–40 px (24" 1080p ekran). Bir kod satırı ≈ 20 px. 4° hata ≈ 7–8 satır.
- Gürültü kaynakları: baş hareketi, ışık, gözlük
- Videokonferans görüntüsünün etkisi (sıkıştırma, düşük çözünürlük, düşük FPS):

## 3. Kalibrasyon

- Noktalı kalibrasyon (kullanıcıdan belirli noktalara bakmasını istemek):
- Örtük kalibrasyon (WebGazer'daki gibi tıklamalarla):
- Hareketli hedef takibi (smooth pursuit):
- Uzaktaki katılımcıda kalibrasyon nasıl yapılır?

## 4. Bakış Noktasını Kod Satırına Eşleme

- Ham gaze verisinden fixation çıkarma (I-DT, I-VT):
- Fixation'ları AOI'lere (satır / blok) atama:
- Dikey kayma düzeltme (vertical drift correction):
- Karşı tarafın ekran düzeni bilinmeden eşleme:

## 5. Mimari Seçenekler

- Adayın tarayıcısında çalışan takip (ör. WebGazer):
- Videokonferanstan gelen görüntüyü işleme (ör. L2CS-Net, MediaPipe):

## 6. Öneri ve Riskler

## Kaynaklar
