# DEC-16 — Meet'ten video yakalama ve extension mimarisi

Durum: araştırma bitti, elle test bekliyor (20 Ekim 2026). Kod yok.

## Kararlar

- Platform: **Google Meet**.
- Extension yalnızca **görüşmecinin** Chrome'unda çalışır. Adayda kurulum yok.
- Video yolu: **C (DOM `<video>`)**. Elle testte olmazsa **B (tabCapture)**.
- Kalibrasyon: aday DECODE'un **kalibrasyon sayfasını** link ile açar ve ekranını paylaşır. Extension noktaları paylaşılan ekran akışında görür.

## Video yolları

| Yol | Nasıl | Durum |
|---|---|---|
| A. Meet Media API | Google'ın resmi gerçek zamanlı medya API'si | Kapalı: yeni kayıt alınmıyor, host onayı gerekli, şifreli toplantıda çalışmaz [1] |
| B. `tabCapture` | Kullanıcı extension'a tıklar, Meet sekmesi yakalanır, aday kutusu kırpılır | Resmi ve belgeli [2]. Kırpma Meet düzenine bağlı, çözünürlük ekranla sınırlı |
| C. DOM `<video>` | Content script Meet'in `<video>` öğelerini canvas'a çizer | En basit, her akış kendi çözünürlüğünde. Doğrulanmadı |

Meet bir SFU ve "virtual media streams" kullanır; bir akış her zaman aynı kişiye ait değildir [1]. Bu yüzden `RTCPeerConnection`'a kanca atmak yerine ekrandaki kutuyu (C) okumak daha güvenli.

## Akış

1. Görüşmeci extension'dan oturumu başlatır.
2. Aday kalibrasyon linkini açar, ekranını paylaşır, noktalara bakar.
3. Extension iki akışı okur: adayın kamerası + paylaşılan ekran.
4. Kalibrasyon: ekran akışındaki nokta konumu ↔ kameradaki göz. Koordinatlar adayın ekranına göre.
5. Aday kodu aynı paylaşımda okur. Bakış noktaları kod satırlarına (AOI) eşlenir.
6. Scanpath → STA trending path'leri ile karşılaştırma → sonuç görüşmecinin ekranında.

## Kalite (DEC-37 girdisi)

- Kamera varsayılanı 720p. Bant genişliği düşükse Meet çözünürlüğü düşürür. 1080p yalnızca kayıt açıkken ya da kişi büyük ekranda pinlenmişse [3].
- Alıcının elindeki tek ayar: adayı pinlemek.
- Ekran paylaşımı çözünürlüğü ve 2 kişilik çağrıda fps: ölçülmedi.

## Riskler

- Meet DOM'u değişirse C kırılır → B'ye düş.
- Sıkıştırma göz bölgesini bozar → DEC-37.
- Chrome Web Store "Limited Use" kuralı: veri yalnızca beyan edilen amaç için, aktarım yok [4]. Ham video saklamıyoruz (F8).

## Elle test (sonraki iş)

- 2 cihazlı Meet çağrısı (bilgisayar = görüşmeci, telefon/2. hesap = aday).
- C: `<video>` pikselleri okunabiliyor mu, çözünürlük, fps, pin etkisi.
- Ekran paylaşımı akışı ayrı `<video>` olarak geliyor mu.

## Açık sorular

- Rıza (UC-02) da kalibrasyon sayfasında mı alınsın?
- Analiz gerçek zamanlı mı, oturum sonrası mı?

## Kaynaklar

1. https://developers.google.com/workspace/meet/media-api/guides/overview
2. https://developer.chrome.com/docs/extensions/reference/api/tabCapture
3. https://workspaceupdates.googleblog.com/2024/06/google-meet-full-hd-meeting-recordings-and-more-devices.html
4. https://developer.chrome.com/docs/webstore/program-policies/limited-use
