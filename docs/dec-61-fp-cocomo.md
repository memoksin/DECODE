# DEC-61 — COCOMO'yu Function Point boyutuyla yeniden yap

Durum: duraklatıldı (24 Kasım 2026, Mehmet + agent). Hocaya sorulacak: hazır kodun FP'yi şişirmesi nasıl ele alınsın?

## Sonuç

- Ders slaytları (CNG491 Lecture 3, Software Estimation) yalnızca şu yolu işliyor: FP → ATFP → LOC = ATFP × language unit size (QSM/KIT tablosu) → **Basic COCOMO**; ayrıca **Jones First-Order**.
- Slaytlarda **reuse modeli yok, COCOMO II yok**. COCOMO seviyeleri (Basic/Intermediate/Advanced) yalnızca adıyla geçiyor (slayt 42).
- Hocalar slaytta olmayan yöntem istemiyor. SRS 3 şu an COCOMO II ve MiroTalk için reuse modeli kullanıyor; ikisi de slaytta yok.
- Hangi düzeltme seçilirse seçilsin FP tabanlı tahmin kapasitenin (952 h) üstünde.

## Yöntem

- Slayt metni `.pptx`'ten çıkarıldı, "reuse/adapt/COTS/existing/modif/ESLOC/equivalent" arandı: eşleşme yok.
- FP sayımı DEC-59'dan aynen (125 UTFP, VAF 1,06, 133 ATFP; `experiments/dec-59/fp.py`).
- Hazır kodun yaptığı öğeler (28 UTFP): MiroTalk odası (EIF 5), kayıt yükle + analiz (EI 6), canlı durum (EO 5), kamera kontrolü (EO 4), dataset import (EI 4), STA ile trending path (EI 4).

## Ölçümler

**Düzeltme seçenekleri** (JS QSM 47 / Jones 71,11; Python Jones 53,33; COCOMO II girdileri SRS 3.4 ile aynı)

| Seçenek | UTFP | KSLOC | Basic COCOMO | COCOMO II |
|---|---|---|---|---|
| Düzeltme yok | 125 | 6,78–7,87 | 2.722–3.181 h | 5.570–6.578 h |
| Reuse modeli (28 × AAM 0,466) | 110 | 5,97–6,92 | 2.382–2.783 h | 4.829–5.702 h |
| Hazır kodun öğeleri sayılmaz | 97 | 5,26–6,10 | 2.086–2.437 h | 4.192–4.950 h |

**Jones First-Order (slayt 48–49), 133 ATFP, 152 h/PM**

| Class exponent | Effort | Takvim |
|---|---|---|
| 0,41 | 15,1 PM, 2.295 h | 7,4 ay |
| 0,43 | 20,2 PM, 3.077 h | 8,2 ay |
| 0,45 | 27,1 PM, 4.125 h | 9,0 ay |
| 0,46 | 31,4 PM, 4.777 h | 9,5 ay |

Kapasite: 952 h (SRS 3.5).

## Sınırlamalar

- Sayım tek kişi (Mehmet + agent); ikinci sayıcı yok.
- QSM'de Python değeri yok; Python için Jones (53,33) kullanıldı.
- Jones class exponent seçimi (systems/business/shrink-wrap, best/average/worst) yoruma açık.
- Hesap makineye bağlı değil (deterministik formüller).

## Todo

- [ ] Hocaya sor: düzeltme yok mu, yoksa reuse düzeltmesine izin var mı?
- [ ] Cevaba göre SRS 3 ve `docs/srs/estimation.py` güncellenecek; analoji ikinci yöntem olarak tabloda kalacak.
- [ ] Sunum için 10 saniyelik cevap.

## SRS için cümle

Hoca cevabından sonra yazılacak.

## Kaynaklar

1. CNG491 Lecture 3, Software Estimation (ODTÜClass, Week-4), slaytlar 32–49.
2. Jones, C. (2017). *Software Economics and Function Point Metrics: Thirty years of IFPUG Progress* (Version 10.0), Table 16.
3. QSM. *Function Point Languages Table*. https://www.qsm.com/resources/function-point-languages-table
