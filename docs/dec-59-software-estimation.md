# DEC-59 — Software estimation: Function Point çapraz kontrolü

Durum: bitti (8 Kasım 2026, Mehmet). Kod: [experiments/dec-59/fp.py](../experiments/dec-59/fp.py). Ana tahmin: [srs/3-software-estimation.md](srs/3-software-estimation.md).

## Sonuç

- Ana yöntem **analoji** olarak kalıyor (2,81 KSLOC). Function Point yalnızca çapraz kontrol.
- Function Point: **125 UTFP, 133 AFP**. Satıra çevrilince **6,8–7,9 KSLOC**, yani analojinin **2,4–2,8 katı**.
- Fark şuradan geliyor: Function Point sistemin bütün işlevlerini sayıyor. Ama ağır işlerin çoğunu hazır araçlar yapıyor: göz takibi modeli (MediaPipe, L2CS-Net), video görüşmesi ve kayıt (MiroTalk). Function Point bu işi de bizim yazacağımız kod gibi sayıyor.
- İki yöntem de kapasitenin (952 h) üstünde çıkıyor. Karar değişmiyor: önce F1–F6 yapılacak, hazır kod yeniden kullanılacak.
- Sunumda slide değişmiyor. Konu sadece soru gelirse açılacak.

## Yöntem

1. Sayım IFPUG kurallarıyla yapıldı: 5 öğe tipi (EI, EO, EQ, ILF, EIF). Karmaşıklık (low/medium/high) DET/RET/FTR tablolarına göre verildi.
2. Girdi olarak SRS'teki şunlar kullanıldı: F1–F9, ERD'deki 6 tablonun alanları ve UI-1–UI-5 ekranlarındaki alanlar.
3. 14 sistem özelliği (GSC) 0–5 arası puanlandı. Her puan bir SRS gereksinimine bağlandı: PR-02/PR-03 performans, UR-01–03 kullanılabilirlik, kurulum gerektirmeyen tarayıcı, uzaktan adaylar.
4. Satıra çevirme: yeni kodun %34'ü JavaScript (823 SLOC), %66'sı Python (1.602 SLOC). Satır/FP değerleri bu oranla ağırlıklandırıldı.
5. Effort hesabı için SRS 3'teki COCOMO girdilerinin aynısı kullanıldı (Basic organic; COCOMO II EAF 1,458, E 1,121).

## Ölçümler

**Sayım**

| Tip | Öğeler | FP |
|---|---|---|
| ILF (7) | Interviewer, Session, Candidate, CodeStimulus + AOI, Scanpath + sonuç, Dataset, Trending path (F9); hepsi low | 49 |
| EIF (2) | Public dataset ham dosyaları, MiroTalk odası/katılımcılar; low | 10 |
| EI (8) | Oturum aç, oturumu bitir, onay, kalibrasyon (low); kayıt yükle + analiz (high); dataset import, STA ile trending path (medium); kod ekle (low) | 29 |
| EO (5) | Sınıflandırma raporu (high); canlı durum, model değerlendirme (medium); kalibrasyon geri bildirimi, kamera kontrolü (low) | 25 |
| EQ (4) | Oturum listesi, katılan adaylar, kod görünümü, kod listesi; low | 12 |
| **UTFP** | | **125** |

GSC toplamı 41 → VAF = 0,41 + 0,65 = 1,06 → **AFP = 132,5**

**Satır/FP değerleri**

| Kaynak | JavaScript | Python |
|---|---|---|
| Capers Jones (2017), Table 16 | 71,11 | 53,33 |
| QSM tablosu | 47 (ort.), 31–63 | yok |

**Sonuç tablosu**

| Senaryo | Satır/FP | KSLOC | Analojiye oran | Basic COCOMO | COCOMO II |
|---|---|---|---|---|---|
| Analoji (SRS 3) | — | 2,81 | 1× | 1.080 h | 2.075 h |
| FP, JS + Python Jones | 59,4 | 7,87 | 2,8× | 3.181 h | 6.578 h |
| FP, JS QSM + Python Jones | 51,2 | 6,78 | 2,4× | 2.722 h | 5.570 h |

## Sınırlamalar

- Karmaşıklık ve GSC puanları tek bir kişinin sayımı (Mehmet + agent). İkinci bir sayıcıyla kontrol edilmedi.
- Python için QSM'de değer yok. Jones'un tablosu Python'u Java ve C++ ile aynı gruba koyuyor (53,33). Pratikte Python kodu daha kısa olduğu için FP boyutu büyük çıkabilir.
- Sayım SRS taslağına göre yapıldı. Tasarım değişirse sayım da değişir.
- Function Point, video dosyası ve gaze örnekleri gibi geçici verileri saymıyor.

## Todo

- [ ] SRS 3'e (Word) veya final rapora "çapraz kontrol" diye kısa bir paragraf ekle.
- [ ] Sprint sonlarında gerçek saatlerle (`hours.py`) iki tahmini karşılaştır.

## SRS için cümle

As a cross-check, we counted IFPUG Function Points from the SRS functions, data model and screens: 125 unadjusted and 133 adjusted function points, or 6.8–7.9 KSLOC with published language ratios (Jones, 2017). This is 2.4–2.8 times our analogy estimate, because function points also count functionality that existing libraries provide (gaze estimation, video call, recording); both estimates exceed the team capacity and lead to the same scope decision.

## Kaynaklar

1. Jones, C. (2017). *Software Economics and Function Point Metrics: Thirty years of IFPUG Progress* (Version 10.0), Table 16. https://www.ifpug.org/wp-content/uploads/2017/04/IYSM.-Thirty-years-of-IFPUG.-Software-Economics-and-Function-Point-Metrics-Capers-Jones.pdf
2. QSM. *Function Point Languages Table*. https://www.qsm.com/resources/function-point-languages-table
