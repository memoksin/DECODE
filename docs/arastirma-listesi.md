# DECODE — Araştırma Listesi

Projenin gidişatını anlamak için incelenecek konular. Bulgular her maddenin altına not edilir.

Kaynak: [Proposal.md](../marker_out/Proposal/Proposal.md)

## 0. İlk Toplantı Hazırlığı (8 Ekim 2026)

Hocalar STA'nın yazarları (Eraslan, Yesilada). Bu yüzden STA'yı ve [6]'yı iyi bilmek en önemli hazırlık.

### Bilerek girmemiz gerekenler

- [ ] Projeyi tek cümlede anlatabilmek: "Acemi ve deneyimli programcılar için STA ile trending path çıkarıp, webcam ile alınan bir scanpath'i bunlarla kıyaslayarak deneyim tahmini yapmak."
- [ ] Temel terimler: fixation, saccade, scanpath, AOI, trending path
- [ ] STA'nın ana fikri ve adımları ([5]'in özeti yeterli)
- [ ] [6]'daki sınıflandırma mantığı: scanpath iki trending path'ten hangisine daha benzer?
- [ ] [4]: STA kodla zaten kullanılmış. Bizim farkımız: kümeleme değil, **tahmin**
- [ ] [3]'ün ana bulgusu: ikili sınıflandırma, 3 seviyeli sınıflandırmadan daha iyi
- [ ] Projenin iki ayrı parçası var: (a) offline STA modeli, (b) webcam + videokonferans eklentisi
- [ ] Bilinen en büyük risk: webcam ile bakış tahmini kod satırı seviyesinde yeterince doğru olmayabilir

### Ön araştırma (toplantıya kadar, ~3–4 saat)

- [ ] [5] ve [6]'nın özet ve yöntem bölümlerini okumak (~1,5 saat)
- [ ] [4]'ün özetini okumak, hangi veri setini kullandığını not etmek (~30 dk)
- [ ] EMIP veri setine göz atmak: deneyim etiketi var mı? (~30 dk)
- [ ] WebGazer.js demosunu denemek, doğruluğunu gözle görmek (~30 dk)
- [ ] Hangi videokonferans araçlarının eklenti SDK'sı var, kısa liste (~30 dk)

### Toplantıda sorulacaklar

- [ ] Hazır STA kodu/aracı var mı? Kullanabilir miyiz?
- [ ] Önerilen veri seti var mı? [4]'ün verisine erişim mümkün mü?
- [ ] Hangi videokonferans aracı tercih ediliyor? (Zoom, Meet, Teams, Jitsi)
- [ ] Kapsam: gerçek zamanlı mı, oturum sonrası analiz mi yeterli?
- [ ] Kod ekranda nerede? Paylaşılan ekran mı, sabit bir editör mü? (AOI eşlemesini doğrudan etkiler)
- [ ] Kendi kullanıcı çalışmamızı yapacak mıyız? Etik kurul onayı gerekir mi?
- [ ] Teslim tarihleri, ara raporlar, toplantı sıklığı
- [ ] Beklenen çıktı: rapor, makale, demo?

## 1. Literatür (Kilometre taşı 1)

- [ ] [1] Aljehane vd. 2023 — Bilişsel yük ve görsel efor ölçümüyle uzmanlık değerlendirmesi
- [ ] [2] Peitek vd. 2020 — Programcıların okuma sırasını ne belirliyor? (linear vs. story order)
- [ ] [3] Ahsan & Obaidellah 2025 — ML ile acemi programcı yetkinliği; hangi öznitelikler kullanılmış?
- [ ] [4] Ahsan & Obaidellah 2023 — STA ile acemi programcıları kümeleme
- [ ] [5] Eraslan vd. 2016 — STA algoritmasının kendisi (temel makale)
- [ ] [6] Eraslan vd. 2020 — STA ile otizm tespiti; sınıflandırma yöntemi bizim için şablon
- [ ] Deneyime göre geliştirici sınıflandıran diğer çalışmalar (ileri/geri atıf taraması)
- [ ] "Novice" ve "expert" tanımları: hangi ölçütle ayrılıyor? (yıl, test, öz değerlendirme)

## 2. Scanpath Trend Analysis (STA)

- [ ] STA adımları: preliminary stage, first pass, second pass, final stage
- [ ] Hazır STA kodu var mı? (Eraslan'ın GitHub/web aracı)
- [ ] Kaynak kodda AOI nasıl tanımlanır? (satır, token, blok)
- [ ] Scanpath benzerlik ölçütleri: String-edit (Levenshtein), ScanMatch, MultiMatch
- [ ] Bilinmeyen bir scanpath iki trending path ile nasıl karşılaştırılır? Eşik/karar kuralı
- [ ] STA'nın farklı kod parçalarına (farklı stimulus) genellenmesi: her kod parçası için ayrı trending path mi?

## 3. Açık Eye-tracking Veri Setleri (Kilometre taşı 2–3)

- [ ] EMIP veri seti (Eye Movements In Programming)
- [ ] Peitek vd. çalışmalarının açık verisi
- [ ] Ahsan & Obaidellah çalışmalarının verisi paylaşılmış mı?
- [ ] Her veri seti için: katılımcı sayısı, deneyim etiketi, fixation verisi, kod stimulus'u, lisans
- [ ] Ham gaze verisinden fixation ve scanpath üretme (I-VT, I-DT algoritmaları)

## 4. Webcam ile Bakış Tahmini (Kilometre taşı 5)

- [ ] Webcam tabanlı gaze tahmini: WebGazer.js, GazeCapture/iTracker, L2CS-Net, MediaPipe Face Mesh/Iris
- [ ] Gerçekçi doğruluk: webcam ile kaç derece/piksel hata? Satır seviyesinde yeterli mi?
- [ ] Kalibrasyon: uzak katılımcıda nasıl yapılır?
- [ ] Bakış noktasını ekrandaki kod satırına eşleme (karşı tarafın ekran düzeni bilinmeden)
- [ ] Baş hareketi, ışık, gözlük gibi gürültü kaynakları
- [ ] Düşük doğruluk varsa çözüm: AOI'yi satır yerine blok seviyesinde tutmak

## 5. Videokonferans Aracından Video Alma (Kilometre taşı 6)

- [ ] Hedef araç seçimi: Zoom, Google Meet, MS Teams, Jitsi
- [ ] Zoom Apps SDK / Meeting SDK, Raw Data erişimi
- [ ] Google Meet Add-ons SDK ve Media API
- [ ] Teams uygulama/bot API'leri
- [ ] Jitsi (açık kaynak) ile prototip kolaylığı
- [ ] Ekran paylaşımı + kamera akışını aynı anda alma ve senkronlama

## 6. Eklenti Geliştirme (Kilometre taşı 7)

- [ ] Mimari: istemci tarafı (tarayıcı) mı, sunucu tarafı işleme mi?
- [ ] Gerçek zamanlı mı, oturum sonrası analiz mi?
- [ ] Gizlilik ve etik: rıza, KVKK/GDPR, yüz verisinin saklanması

## 7. Değerlendirme ve Doğrulama (Kilometre taşı 8)

- [ ] Metrikler: accuracy, precision, recall, F1, ROC-AUC
- [ ] Doğrulama: leave-one-participant-out, k-fold cross validation
- [ ] Karşılaştırma tabanı: [3]'teki ML sonuçları
- [ ] Webcam verisini gerçek eye-tracker verisiyle kıyaslama (pilot kullanıcı çalışması)
- [ ] Etik kurul onayı gerekiyor mu?
