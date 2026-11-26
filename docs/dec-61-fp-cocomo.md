# DEC-61 — COCOMO'yu Function Point boyutuyla yeniden yap

Durum: hesap bitti (26 Kasım 2026, Mehmet + agent). Hazır kodun sayılıp sayılmayacağı **hocaya sunumdan sonra sorulacak**; o zamana kadar iki senaryo da raporda.

## Sonuç

- Yalnızca slayttaki yöntemler: FP → ATFP → LOC → **Basic COCOMO**, **Jones First-Order**; ikinci yöntem **analoji**. COCOMO II ve reuse modeli çıkarıldı (slaytta yok).
- Hazır kod sayılırsa: 125 UTFP → 132,5 ATFP → 6,78 KDSI → Basic COCOMO **2.722 h**, Jones ortalama **3.077 h**.
- Hazır kod sayılmazsa: 97 UTFP → 102,8 ATFP → 5,26 KDSI → Basic COCOMO **2.086 h**, Jones ortalama **2.219 h**.
- Analoji: MiroTalk sayılırsa 1.258 h, sayılmazsa 925 h.
- Kapasite 952 h. FP tahminleri kapasitenin 2–3 katı; analoji yaklaşık 1 katı.

## Yöntem

- FP sayımı DEC-59'dan aynen (`experiments/dec-59/fp.py`): 125 UTFP, VAF 1,06.
- Hazır kodun yaptığı öğeler (28 UTFP): MiroTalk odası (EIF 5), kayıt yükle + analiz (EI 6), canlı durum (EO 5), kamera kontrolü (EO 4), dataset import (EI 4), STA ile trending path (EI 4).
- LOC/FP: JavaScript 47 (QSM, slayt 41). Python QSM'de yok → Jones (2017) Table 16: **53,33**. Dil payları analojiden (%34 JS, %66 Python) → ağırlıklı 51,18 LOC/FP.
- Jones sınıfı: Business (0,41 / 0,43 / 0,46).
- 152 h/PM: Boehm (1981).
- Hesap: `docs/srs/estimation.py` (slayt 47 örneği ve Boehm 32 KDSI örneği ile kendini kontrol eder).

## Ölçümler

| Yöntem | Hazır kod sayılır | Hazır kod sayılmaz |
|---|---|---|
| Basic COCOMO | 17,9 PM, 2.722 h, 7,5 ay | 13,7 PM, 2.086 h, 6,8 ay |
| Jones en iyi (0,41) | 15,1 PM, 2.295 h, 7,4 ay | 11,1 PM, 1.680 h, 6,7 ay |
| Jones ortalama (0,43) | 20,2 PM, 3.077 h, 8,2 ay | 14,6 PM, 2.219 h, 7,3 ay |
| Jones en kötü (0,46) | 31,4 PM, 4.777 h, 9,5 ay | 22,1 PM, 3.366 h, 8,4 ay |
| Analoji (MiroTalk sayılır / sayılmaz) | 3.251 SLOC, 1.258 h | 2.425 SLOC, 925 h |

Kapasite: 4 × 28 hafta × 8,5 h = 952 h (6,3 PM).

## Python değeri nereden geliyor

- Slayttaki kaynakların (slayt 40–41 tablosu, QSM, KIT/Prechelt 2000) hiçbirinde Python yok.
- Jones (2017), Appendix B, Table 16: 79 dil için 1.000 FP'lik uygulamanın KLOC'u. Python satırı 53,33 KLOC → **53,33 LOC/FP**.
- Aynı tabloda Java da 53,33, JavaScript 71,11, Ruby 45,71, Perl 35,56.

## Sınırlamalar

- Sayım tek kişi (Mehmet + agent); ikinci sayıcı yok.
- Python değeri slayt dışı bir kaynaktan (Jones 2017); JavaScript QSM'den. İki kaynak karışık.
- Jones'un tablosunda Python = Java; Python için ayrı ölçüm olmayabilir.
- Jones sınıfı (Business) yoruma açık.
- Hesap makineye bağlı değil (deterministik formüller).

## Todo

- [x] Slayt dışı yöntemleri çıkar (COCOMO II, reuse modeli).
- [x] İki senaryo: hazır kod sayılır / sayılmaz.
- [x] SRS 3 taslağı (`docs/srs/3-software-estimation.md`) ve `estimation.py` güncellendi.
- [ ] Hocaya sunumdan sonra sor: hazır kodun FP'si sayılsın mı?
- [ ] SDD/SRS Google Doc'a aktarılacaksa Memo karar verir.

## Sunum için 10 saniyelik cevap

"İki senaryo: hazır kod sayılırsa 2.700 saat, sayılmazsa 2.100 saat. Kapasitemiz 950 saat; bu yüzden hazır kodu kullanıyoruz ve önce ana akışı yapıyoruz."

## SRS için cümle

"We estimated size with IFPUG Function Points (125 UTFP, 132.5 ATFP) and converted it to code with 47 LOC/FP for JavaScript (QSM) and 53.33 LOC/FP for Python (Jones, 2017); Basic COCOMO gives 2,722 h with the ready code counted and 2,086 h without it, against a team capacity of 952 h."

## Kaynaklar

1. CNG491 Lecture 3, Software Estimation (ODTÜClass, Week-4), slaytlar 39–50.
2. Boehm, B. W. (1981). *Software engineering economics*. Prentice Hall.
3. QSM. *Function Point Languages Table* (Version 5.0). https://www.qsm.com/resources/function-point-languages-table
4. Jones, C. (2017). *Software Economics and Function Point Metrics: Thirty years of IFPUG Progress* (Version 10.0, 14 Nisan 2017), Appendix B, Table 16. Namcook Analytics. https://www.ifpug.org/wp-content/uploads/2017/04/IYSM.-Thirty-years-of-IFPUG.-Software-Economics-and-Function-Point-Metrics-Capers-Jones.pdf
