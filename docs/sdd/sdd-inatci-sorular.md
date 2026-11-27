# SDD: inatçı hoca soruları

Sunum ve okuma için hazırlık. Cevaplar en fazla 10 saniye.

## 5.2 Sprint 2

**S: Burndown neden tam sıfırda bitiyor? Bu kadar düzgün olur mu?**
C: Sprint 2'ye aldığımız 23 işin hepsini teslimden önce bitirdik. Uzun dönem işleri Sprint 2'ye almadık. Saatler yaklaşık.

**S: Uzun dönem işler (gaze test, 3×3 grid, STA, string matching, kalibrasyon UI, demo) ne zaman yapılacak?**
C: Başlama kararı verdiğimiz sprint'e yazıyoruz. Bu dönem iki sprint kaldı: Sprint 3 ya da Sprint 4. Örnek: 3×3 grid'e Sprint 3'te başlarsak Sprint 3 backlog'una girer.

## Tur 1 (27 Kasım)

Tipler: **[R]** raporda cevabı var · **[E]** ekibe soruldu · **[H]** "henüz ölçmedik / bu dönemin konusu değil"

**S1 [E] Novice/experienced sınırı neye göre?**
C: Dataset hangi ölçütle ayırmışsa onu kullanıyoruz; buna bağlıyız. (Ölçüt Sude'ye soruldu, DEC-76.)

**S2 [R] STA tek developer için geçerli mi?**
C: Bu, projenin araştırma sorusu. Tasarım bunu test edebilecek şekilde kuruldu.

**S3 [R] Yanlış sınıflandırırsa ne olur?**
C: DECODE sadece destek. Karar her zaman interviewer'da. (SDD Intro, stakeholders paragrafı.)

**S4 [E] Class diyagramı ile sequence lifeline'ları aynı mı?**
C: Sude'ye soruldu (DEC-76): sequence metotları hangi sınıfta.

**S5 [R] Okumanın bitişini kim belirliyor?**
C: Interviewer'ın End düğmesi. Developer'ın ne zaman bittiğini değil, analiz penceresini interviewer'ın kapatmasını esas alıyoruz. Dataset'lerde de görev sonu katılımcının sinyali.

**S6 [H] Kalibrasyon eşiği kaç?**
C: Henüz seçmedik. Önce gerçek testler lazım: hangi noktada kalibrasyon bozuluyor, kaç denemede hata en aza iniyor. (DEC-39, Sprint 3.)

**S7 [iç cevap, raporda yok] Onay yarıda geri çekilirse?**
C: Onay her zaman geri çekilebilir (GDPR md. 7(3)). Developer durdurursa oturum iptal olur, yerel kayıt silinir, sonuç saklanmaz. Ayrıntılı akış ileriki sprintte tasarlanacak.

**S8 [R] Ne saklanıyor, ne siliniyor?**
C: Video analizden sonra silinir. Gaze noktaları, scanpath ve sonuç modeli geliştirmek için saklanır; developer bunu onay metninde kabul eder. (SDD Intro.)

**S9 [R] Neden Meet/Zoom değil, neden MiroTalk fork'u?**
C: Meet Media API yeni projelere kapalı ve Meet bant genişliği düşünce çözünürlüğü düşürüyor (DEC-16). Açık kaynak bir platform gerekti, MiroTalk SFU'yu seçtik. Fork, DECODE ekranlarını (onay, kalibrasyon, kod görünümü, kayıt) MiroTalk istemcisine eklemek için. Hocalar da onayladı. Zoom için kaynağımız yok, söylemiyoruz.

**S10 [H] Sonuç makineye bağımlı mı?**
C: Minimum gereksinimler SRS'te: 720p, 30 fps (DEC-45), ağ gecikmesi < 200 ms (PR-02). Doğruluk kaybını henüz ölçmedik (DEC-62, Sprint 3).

**S11 [H] Yükleme yarıda kesilirse? Kod dışına bakış?**
C: Yerel kaydın sebebi WebRTC sıkıştırması. Yükleme hatası ve kod dışı bakışlar bu dönemin konusu değil: şu an 3×3 grid ile erken prototip yapıyoruz, kod blokları tanımlanınca (gelecek dönem) ele alınacak.

**S12 [E] Gantt tarihleri neye dayanıyor, kritik yol ne?**
C: Burcu'ya soruldu (DEC-78).

**S13 [R] Tahmin ile gerçek saat farkı?**
C: Saatler yaklaşık; önceki sprintlerden öğrenerek tahmin ettik ve bu sprintte toplamda tuttu. Haftalık dağılım farklı, burndown'da ideal ve gerçek çizgi bunu gösteriyor.

**S14 [R] Kim ne yaptı?**
C: 5.2.1 Backlog tablosunun Owner sütunu.

**S15 [R] Sprint 1 iyileştirmeleri uygulandı mı?**
C: Retro'daki Sprint 1 eylemleri tablosu.
