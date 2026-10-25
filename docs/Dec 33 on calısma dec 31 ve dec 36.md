## Proposal makalelerinin özeti:

A ljehane et al. (2023) [ETRA]: Göz hareketleriyle bilişsel yük (cognitive load) ve uzmanlık düzeyi ölçümü. Deneyim sınıflandırmasında metrik bazlı referanstır.

Peitek et al. (2020) [ICPC]: Programcıların kod okuma sırası (okuma akışı / visual effort) analizi. Kod üzerindeki bakış sırasının (sequential gaze) modellenmesi için temel oluşturur.

Ahsan & Obaidellah (2025/2026) [TOCE]: Makine öğrenmesiyle programcı yetkinliğini sınıflandırma. İkili sınıflandırmanın (novice vs. experienced) 3 seviyeli sınıflandırmaya göre daha yüksek doğruluk verdiğini ortaya koymuştur.

A hsan & Obaidellah (2023) [ETRA]: Kod anlama görevlerinde Scanpath Trend Analysis (STA) ile acemi programcıların kümelenmesi.

E raslan, Yesilada & Harper (2016) [TWEB]: Web sayfaları üzerinde Scanpath Trend Analysis (STA) metodolojisinin kurucu makalesi.

E raslan et al. (2020) [W4A]: STA kullanılarak grup sınıflandırması (Otizm spektrumu - kontrol grubu). DECODE'un trending path karşılaştırma mantığı doğrudan bu yönteme dayanır.

related work için benzer uygulamaların olduğu makaleleri kullanacağız. karşılaştırma tablosu

için de aynı şekilde.

proposal daki yöntemler genellikle yüksek donanımlı cihazlara dayanmaktadır (Tobii, SMI) decode projesinde ise Google meet Zoom vb extension lar kullanacağız bu nedenle:

## WEBCAM / EYETRACKING YAPAN MAKALELER

## Investigating the Feasibility of Conducting Webcam-Based Eye-Tracking Studies in Code Comprehension

- Yazarlar: Sonuçlarda yazar listesi yok (Vanderbilt VALIANT grubu haberi). Doğrula.

- Yıl/Yayın: 2026, IEEE Transactions on Software Engineering

- Özet: Webcam tabanlı göz izleyiciyi, kod anlama görevlerinde araştırma sınıfı ekran izleyiciyle karşılaştırıyor. Webcam anlamsal okuma örüntülerini makul yakalıyor ama token düzeyinde zorlanıyor, katılımcılar kalibrasyonda zorluk yaşamış. [URL 🔗](https://www.vanderbilt.edu/valiant/2026/02/25/investigating-the-feasibility-of-conducting-webcam-based-eye-tracking-studies-in-code-comprehension)

- Projeye bağı: Webcam ile kod okuma izlemenin sınırlarını gösteriyor. SRS’te sınırlılıklar (1.4.4) ve risk için doğrudan kaynak.

Sadece fizibilite ölçüyor, deneyim sınıflandırması yok. Biz webcam verisiyle sınıflandırıyoruz.


- Link: https://www.vanderbilt.edu/valiant/2026/02/25/investigating-the-feasibility-of-conducting- webcam-based-eye-tracking-studies-in-code-comprehension [URL 🔗](https://www.vanderbilt.edu/valiant/2026/02/25/investigating-the-feasibility-of-conducting-webcam-based-eye-tracking-studies-in-code-comprehension)

## Towards Automatic Identification of Novices on the Web Using Eye Tracking

- Yazarlar: Martin Mokrý (ortak yazarlar sonuçta yok, doğrula)

- Yıl/Yayın: 2018, IIT.SRC

- Özet: Fiksasyon, sakkad, göz bebeği boyutu ve kafa mesafesinden özellik çıkarıp makine öğrenmesi modeline veriyor. E-ticaret alanında toplam 72 katılımcıyla iki çalışma yapılmış. linkedin [URL 🔗](https://sk.linkedin.com/in/martin-mokry)

- Projeye bağı: Eye-tracking ile acemi/uzman ayırımı.

Farkımız: web alanı ve özellik tabanlı ML, biz kod okuma ve STA.

- Link: kaynak göster) https://sk.linkedin.com/in/martin-mokry (LinkedIn profili, asıl makaleyi bulup onu

## Bewertung Maschinelle Lernalgorithmen für die Güte von Programmierkenntnissen

- Yazarlar: Christian Hackenbeck (danışman: Wolfgang Fuhl)

- Yıl/Yayın: 2020, Tübingen Üniversitesi, bitirme tezi (Almanca)

- Özet: Eye-tracking verisiyle makine öğrenmesinin, programlama becerisinde acemi ve uzmanı ayırıp ayıramayacağını inceliyor. uni-tuebingen

- Projeye bağı: Aynı problem, ML yaklaşımı. Tez ve Almanca olduğu için SRS’te zayıf kaynak, arka plan için.

- Link: https://www.hci.uni-tuebingen.de/assets/pdf/publications/B.Sc.ChristianHackenbeck.pdf

## W ebGazer: Scalable Webcam Eye Tracking Using User Interactions (IJCAI 2016)

- Yazarlar: Alexandra Papoutsaki et al.

- Özet: Standart RGB web kamerası kullanarak (yani dizüstü ve mobil cihazlardaki webcam ler ile) tarayıcı içinde gerçek zamanlı göz takibi gerçekleştiren JavaScript kütüphanesidir. Kullanıcının fare tıklamalarını arka planda kalibrasyon verisi olarak kullanır. Sıradan webcam’lerle çalışan, açık kaynaklı, tarayıcı tabanlı bir göz izleyici. Kendi kendini kalibre eden bir mimarisi var, bunu kullanıcı etkileşimlerini izleyerek yapıyor.

- Projeyle Bağı: DECODE'un video konferans / tarayıcı eklentisi (Chrome Extension) mimarisi için temel referanstır. –İrem ile benzer Genel web sayfaları için, kod okuma ve deneyim tahmini yok. Bizim altyapı adayımız.

- [Bağlantı:https://dl.acm.org/doi/10.5555/3061053.3061156](https://dl.acm.org/doi/10.5555/3061053.3061156)


## E ye Tracking for Everyone (CVPR 2016)

- Yazarlar: Kyle Krafka, Aditya Khosla, Petr Kellnhofer, Wojciech Matusik, Antonio Torralba et al. (MIT)

- Özet: Derin öğrenme (iTracker CNN) kullanarak standart mobil ve web kameralarından bakış koordinatı kestirimi yapar. Bu makale ile birlikte büyük ölçekli GazeCapture veri seti sunulmuştur.

- Projeyle Bağı: Özel kızılötesi donanım olmadan sadece video karesinden bakış yönü tahmin etmenin doğruluğu ve hata sınırları (error margin) için literatür standardıdır.

- Bağlantı:https://ieeexplore.ieee.org/document/7780608 [URL 🔗](https://ieeexplore.ieee.org/document/7780608)

## Deep Semantic Gaze Embedding and Scanpath Comparison for Expertise Classification During OPT Viewing

- Yazarlar: Nora Castner, Thomas C. Kübler, Juliane Richter, Thérése Eder, Fabian Hüttig, Constanze Keutel, Enkelejda Kasneci

- Yıl/Yayın: 2020, ETRA ‘20 (Article 18)

- DOI: 10.1145/3379155.3391320

- Özet: Başlığa göre scanpath karşılaştırması ve gaze embedding ile uzmanlık sınıflandırması yapıyor, alan diş panoramik röntgeni (OPT) okuma. Özet metnine bakmadım, sadece künyeyi gördüm, okurken doğrula.

- Projeye bağı: Scanpath benzerliğiyle uzman/acemi ayırma fikrimizle aynı mantık, ama kod değil görüntü okuma.

- [Link: https://publikationen.uni-tuebingen.de/xmlui/handle/10900/116437?show=full](https://publikationen.uni-tuebingen.de/xmlui/handle/10900/116437?show=full)

## O penFace 2.0: Facial Behavior Analysis Toolkit (IEEE FG 2018)

- Yazarlar: Tadas Baltrušaitis, Amir Zadeh, Yao Chong Lim, Louis-Philippe Morency

- Özet: Standart web kamerası akışlarından yüz landmark'ları, kafa pozu ve bakış yönünü (gaze estimation) gerçek zamanlı ve yüksek doğrulukla çıkaran açık kaynaklı bir araçtır.

- Projeyle Bağı: Video konferans (Zoom/Meet) görüşmesi esnasında kameradan bakış vektörünü yakalamak için doğrudan kullanılabilecek temel bilgisayarla görme altyapısıdır.

- Bağlantı: https://dl.acm.org/doi/10.1109/FG.2018.00019 github openface: https://github.com/TadasBaltrusaitis/OpenFace?hl=tr-TR [URL 🔗](https://github.com/TadasBaltrusaitis/OpenFace?hl=tr-TR)

## A ccelerating Eye Movement Research via Accurate and Affordable Smartphone Eye Tracking (Nature Communications 2020)

- Yazarlar: Nachiappan Valliappan, Na Dai, Ethan Steinberg, Vidhya Navalpakkam et al. (Google Research)


- Özet: Günlük cihazların kameralarıyla göz takibi yaparak fiksasyon ve okuma güçlüklerini (reading comprehension difficulty) tespit etmiştir.

- Projeyle Bağı: Tüketici kameralarıyla yapılan uzaktan göz takibinin okuma anlama analizinde geçerli sonuçlar üretebileceğini kanıtlar.

- Bağlantı: Nature Communications DOI: https://www.nature.com/articles/s41467-020-18360-5

## Webcam-based Eye-Tracking to Measure Visual Expertise of Medical Students During Online Histology Training

- Yazarlar: Markus Missler ve diğerleri (tam liste sonuçta yok, doğrula)

- Yıl/Yayın: 2023, GMS Journal for Medical Education

- Özet: Webcam göz takibi veri kalitesini yeterli bulmuş (ortalama doğruluk 115,7 piksel). Düşük ve yüksek performansı ayırt edip edemediğini araştırıyor. egms [URL 🔗](https://www.egms.de/static/en/journals/zma/2023-40/zma001642.shtml)

- Projeye bağı: Webcam ile uzmanlık ölçümüne dair kanıt, ama alan kod değil.

- [Link: https://www.egms.de/static/en/journals/zma/2023-40/zma001642.shtml](https://www.egms.de/static/en/journals/zma/2023-40/zma001642.shtml)

## LookAtChat: Visualizing Gaze Awareness for Remote Small-Group Conversations

- Yazarlar: Zhenyi He ve 2 yazar (isimleri sonuçta yok, doğrula)

- Yıl/Yayın: 2021 (arXiv:2107.06265)

- Özet: Sıradan webcam’lerle gerçek zamanlı göz takibi yaparak kimin kime baktığını gösteren web tabanlı videokonferans sistemi. Göz takibi modülü WebGazer.js ile çalışıyor. arxivruofeidu [URL 🔗](https://ruofeidu.com/papers/He_LookAtChat-VisualizingGazeAwarenessForRemoteSmall-GroupConversations_2021.pdf)

- Projeye bağı: Videokonferans ortamında webcam gazının uygulanmış örneği. Farkımız: o, göz teması görselleştiriyor, biz kod okuma ve deneyim sınıflandırması yapıyoruz.

- [Link: https://arxiv.org/abs/2107.06265v1](https://arxiv.org/abs/2107.06265v1)

her bir makale için dil/framework , algoritma, veri seti, özellikler ile alakalı not tut

## Dataset bakarken buldugum buraya dahil edilebilecek makaleler:

## 1. EMIP: The Eye Movements in Programming Dataset

- Yazarlar: Roman Bednarik, Teresa Busjahn, Agostino Gibaldi, Alireza Ahadi, Maria Bielikova, Martha Crosby, Kai Essig, Fabian Fagerholm, Ahmad Jbara, Raymond Lister, Pavel Orlov, James Paterson, Bonita Sharif, Teemu Sirkiä, Jan Stelovsky, Jozef Tvarozek, Hana Vrzakova, Ian van der Linde

- Yıl/Yayın: 2020, Science of Computer Programming, cilt 198, 102520

- DOI: 10.1016/j.scico.2020.102520


- Özet: İki kod anlama görevi sırasında 216 programcının göz hareketlerini içeren büyük bir veri seti. Veriler programlama uzmanlığına (hiç deneyimsizden yükseğe) ve diğer demografik özelliklere göre gruplanmış. Sekiz ülkede on bir araştırma ekibinin ortak çalışmasıyla, aynı göz izleme cihazı ve yazılımıyla toplanmış. anglia [URL 🔗](https://arro.anglia.ac.uk/id/eprint/705904)

- Projeye bağı: Ana dataset adayımız. Deneyim seviyesi etiketli, büyük ve CC-BY 4.0 lisanslı, OSF’ten indirilebilir. Kızılötesi cihazla toplandığı için webcam verisinden farklı, bu SRS’te varsayım olarak yazılmalı. “Aynı kodu herkes mi okudu” ve AOI dosyaları hâlâ doğrulanacak. osf [URL 🔗](https://osf.io/53kts)

- Link: Veri: https://osf.io/53kts, makale (kabul edilmiş sürüm): https://par.nsf.gov/servlets/purl/10251907 [URL 🔗](https://osf.io/53kts)

## 2. Correlates of Programmer Efficacy and Their Link to Experience: A Combined EEG and Eye-Tracking Study

- Yazarlar: Norman Peitek, Annabelle Bergum, Maurice Rekrut, Jonas Mucke, Matthias Nadig, Chris Parnin, Janet Siegmund, Sven Apel

- Yıl/Yayın: 2022, ESEC/FSE ‘22 (Singapur), 12 sayfa

- DOI: 10.1145/3540250.3549084

- Özet: 37 katılımcıyla EEG ve göz takibi kullanılarak yapılan kontrollü deney. Katılımcılar 32 Java kod parçasını anlamaya çalışıyor. Verimliliği (doğru çözülen görev / dakika) deneyim ölçüleriyle ilişkilendiriyorlar. Yüksek verimli programcılar kodu daha hedefli, daha düşük bilişsel yükle okuyor. Yıl gibi yaygın deneyim ölçüleri verimliliği iyi tahmin etmiyor, kendini akranlarla kıyaslama daha iyi tahmin ediyor.

- Projeye bağı: Yedek dataset. Herkes aynı 32 snippet’i okuyor, AOI’ler hazır, Tobii Pro Fusion (250 Hz) ile kaydedilmiş. Hazır acemi/uzman etiketi yok, grupları biz oluşturmalıyız. Ayrıca “yıl bazlı deneyim etiketi güvenilir değil” bulgusu SRS’teki etiketleme riskine kaynak olur. Yazarlar teknik mülakat bağlamına da değiniyor.

- Link: DOI: https://doi.org/10.1145/3540250.3549084, veri: https://osf.io/4hjbd, replikasyon paketi: https://github.com/brains-on-code/NoviceVsExpert [URL 🔗](https://doi.org/10.1145/3540250.3549084)

- 3. Eye Movements in Code Reading: Relaxing the Linear Order

- Yazarlar: Teresa Busjahn, Roman Bednarik, Andrew Begel, Martha E. Crosby, James H. Paterson, Carsten Schulte, Bonita Sharif, Sascha Tamm

- Yıl/Yayın: 2015, IEEE 23rd International Conference on Program Comprehension (ICPC), s. 255–265

- DOI: 10.1109/ICPC.2015.36

- Özet: Acemi ve uzman programcıların doğal metin ve kaynak kod okurken göz hareketlerini karşılaştırıyor, okuma doğrusallığı için ölçütler geliştiriyor. Acemiler kodu doğal metne göre daha az doğrusal okuyor, uzmanlar ise acemilerden bile daha az doğrusal okuyor. vanderbilt [URL 🔗](https://huang.isis.vanderbilt.edu/cs8395-f23/paper/linear-order-eye.pdf)

- Projeye bağı: Longitudinal Java dataset’in asıl kaynağı (Al Madi’nin yeniden analiz ettiği veri). Acemi/uzman okuma farkının temel çalışması, bizim “bakış dizisinden deneyim tahmini” fikrimizin dayanağı. Proposal’daki Peitek (2020) bu çalışmanın replikasyonu.


- Method kısmında katılımcı, kod parçaları ve uzmanların aynı programları okuyup okumadığı doğrulanmalı.

- Link: kaydı: https://research.fi/en/results/publication/0008151715) https://huang.isis.vanderbilt.edu/cs8395-f23/paper/linear-order-eye.pdf (kaynakça

## 4. From Novice to Expert: Analysis of Token Level Effects in a Longitudinal Eye Tracking Study

- Yazarlar: Naser Al Madi, Cole S. Peterson, Bonita Sharif, Jonathan I. Maletic

- Yıl/Yayın: 2021, IEEE/ACM 29th International Conference on Program Comprehension (ICPC), s. 172–183

- DOI: IEEE Xplore sayfasından al (sayfada Cite This var, ben DOI’sini görmedim)

- Özet: Mevcut bir uzunlamasına veri setini (20 katılımcı: 14 acemi, 6 deneyimli profesyonel) yeniden analiz ediyor. Token sıklığı ve uzunluğunun göz hareketine etkisini ve acemilerin bunu bir Java dersi boyunca nasıl edindiğini inceliyor. Göz hareketi özellikleriyle Random Forest modeli kurup acemileri uzmanlardan %72 doğrulukla ayırıyor. nsf [URL 🔗](https://par.nsf.gov/search/author:%22Maletic,%20Jonathan%20I.%22)

- Projeye bağı: Göz verisiyle acemi/uzman ikili sınıflandırması yapıyor, bizim işe en yakın çalışma. Fark: token düzeyi 8 metrik + Random Forest, biz scanpath düzeyinde STA kullanıyoruz. Kendileri de “gerçek zamanlı IDE eklentisi için daha çok adım var” diyor. Hem Related Work hem dataset (Longitudinal Java) için kaynak.

- Link: https://par.nsf.gov/biblio/10267218, replikasyon paketi: https://osf.io/t5je9 [URL 🔗](https://par.nsf.gov/biblio/10267218)

- 5. Can We Predict Stressful Technical Interview Settings Through Eye-Tracking?

- Yazarlar: Mahnaz Behroozi, Chris Parnin

- Yıl/Yayın: 2018, EMIP ‘18: Workshop on Eye Movements in Programming (Varşova), makale no. 3, 5 sayfa

- DOI: 10.1145/3216723.3216729 (bu DOI’yi bir Unpaywall linkinden çıkardım, doğrula)

- Özet: Teknik mülakatlarda beyaz tahtada problem çözerken bilişsel yük ve stresi ölçmek için göz takibi kullanılıyor, ama mülakat ortamının özelliklerinin göz hareketi ölçümlerini ne kadar etkilediğine dair ampirik bir çalışma yok. 11 katılımcının göz hareketlerini iki mülakat ortamında (beyaz tahta ve kâğıt) analiz ediyorlar. Önceki çalışmada ortamlar arasında göz hareketi farkı gözlemişler, burada tek tek göz hareketi olaylarını inceleyip sınıflandırıcıları eğitiyor ve kendi bildirdikleri stresi tahmin etmeye çalışıyorlar. Sonuç cümlesini görmedim, makaleden doğrula. unpaywallnsf [URL 🔗](https://unpaywall.org/10.1145%2F3216723.3216729)

- Projeye bağı: Göz takibi + teknik mülakat + makine öğrenmesiyle tahmin, yani mülakat senaryomuza yakın. Farklar: hedef deneyim değil stres, çok küçük örneklem (11), yüz yüze mülakat, uzaktan/webcam değil. Aynı ekibin ICSE 2018 NIER makalesi Dazed: Measuring the Cognitive Load of Solving Technical Interview Problems at the Whiteboard da kafaya takılan göz izleyici ve bilgisayarlı görü kullanarak beyaz tahtada bilişsel yük ölçüyor. İstersen bunu da yan kaynak olarak ekleyebilirsin. microsoft [URL 🔗](https://www.microsoft.com/en-us/research/?p=617622)

- Link: https://par.nsf.gov/biblio/10085744


bura için ek not:

- EMIP için daha önce senin dokümanında yazan ACM linki (10.1145/3379157.3390511) dataset makalesinin DOI’si değil, yukarıdaki DOI’yi kullan.

- Al Madi’nin DOI’sini ve Behroozi’nin DOI’sini .bib dosyasına koymadan önce doğrula.

- Busjahn (2015) ile Al Madi (2021) arasındaki bağı tabloda açıkça yaz: Al Madi, Busjahn’ın topladığı veriyi yeniden analiz ediyor. Dataset sütununda ikisine de atıf gerekir.

her kaynak için doi ve bibtex kaydını bir .bib dosyasında topla

## TICARI / BENZERI URUNLER (Makale yok sadece benzer urunlerden bahsediyo)

## Xobin EyeGazer

- Yazar/Şirket: Xobin

- Özet: Webcam’den yüz landmark tespitiyle bakış yönünü gerçek zamanlı izliyor, ekran dışı bakışı işaretliyor. xobin

- Projeye bağı: Amacı hile tespiti. Bizimki deneyim sınıflandırması.

- Link: https://xobin.com/?p=92253 [URL 🔗](https://xobin.com/?p=92253)

## RightPerson

- Yazar/Şirket: RightPerson (2026'da kurulmuş startup)

- Özet: Teknik mülakatlar için AI mülakat bütünlüğü platformu: göz takibi, ses enjeksiyonu tespiti, kod intihal analizi. startuphub [URL 🔗](https://www.startuphub.ai/startups/rightperson.md)

- Projeye bağı: Teknik mülakat bağlamında göz takibi kullanıyor, ama sınıflandırma değil bütünlük kontrolü.

- [Link: https://www.startuphub.ai/startups/rightperson.md](https://www.startuphub.ai/startups/rightperson.md)

## EyeSpy (Innopolis University capstone)

- Yazarlar: Innopolis capstone ekibi (isimler sonuçta yok)

- Özet: Açık kaynak PyTorch gaze-estimation modeliyle uzaktan sınav ve mülakatlarda bakışı izleyen, gizlilik odaklı MacOS uygulaması. Kullanıcı ekrana bakmıyorsa alarm veriyor. innopolis [URL 🔗](https://capstone.innopolis.university/docs/2024/eyespy/week1/)

- Projeye bağı: Açık kaynak gaze-estimation modeli kullanımı bizim teknik seçeneklere ışık tutar. Amaç yine hile önleme.


- [Link: https://capstone.innopolis.university/docs/2024/eyespy/week1/](https://capstone.innopolis.university/docs/2024/eyespy/week1/)

## Videokonferans bağlamı

- 8. He vd. (2021): LookAtChat. Sıradan webcam’lerle gerçek zamanlı göz takibi yapan, web tabanlı bir videokonferans sistemi. Göz takibi modülü WebGazer.js ile çalışıyor. Webcam gazını videokonferansa entegre eden en yakın örnek. arxivruofeidu [URL 🔗](https://ruofeidu.com/papers/He_LookAtChat-VisualizingGazeAwarenessForRemoteSmall-GroupConversations_2021.pdf)

- 9. Hawaii Zoom çalışması (Discovery Research on Attention, Gender and Distraction Effects). Katılımcıların Zoom toplantılarında nereye baktığını göz takibiyle inceliyor. Düşük öncelikli, arka plan için. hawaii [URL 🔗](https://scholarspace.manoa.hawaii.edu/items/b2bff6d9-1284-4dd2-a3c4-9f54e4d15851)

## EYETRACKING DATASET LISTESI

Dataset

EMIP (Bednarik vd., 2020,

216 programcı, farklı deneyim seviyeleri, iki kod anlama görevi, aynı cihazla toplanmış. Lisans: CC-BY 4.0, OSF’te indirilebilir (osf.io/53kts).Python, Java ve Scala kod anlama görevleri sırasındaki göz hareketleri (fiksasyonlar, sakadlar, kod AOI koordinatları ve

Sci. Comput. Program. 198, DOI: 10.1016/j.scico.2020.102520) https://dl.acm.org/doi/abs/10. [URL 🔗](https://dl.acm.org/doi/abs/10.1145/3379157.3390511)

[1145/3379157.3390511](https://dl.acm.org/doi/abs/10.1145/3379157.3390511)

## İçerik

Bizim için

En güçlü aday. Deneyim etiketi var, Aljehane vd. de bunu kullanmış. Aljehane makalesi bunu mevcut en büyük açık eye-tracking verisi olarak anıyor.


geliştiricilerin deneyim seviyeleri

Novice vs Expert (EEG + eye-tracking)

Farklı deneyim seviyelerindeki

İkinci aday. Deneyim etiketi var.

ithub.com/brains-on-code/No programcıların kod anlama

viceVsExpert

sırasındaki ham EEG ve göz takibi verisi, CC-BY 4.0. Replikasyon paketi: github.com/brains-on-code/N oviceVsExpert

Longitudinal Java course 20 acemi ve deneyimli kod Küçük, ama acemi→uzman

dataset

okuyucu, acemilerin Java dersi boyunca takibi.

geçişi var. Erişim linkini makalede aramak gerek.

EyeTrans reproduction package (Zenodo, 2024)

Kod anlama göz takibi çalışmasından ham veri ve işleme scriptleri.

Deneyim etiketi var mı belirsiz, kontrol et.

yslexia & code layout dataset (ETRA ‘21) n

30 katılımcı (14 disleksili, 16 Deneyim sınıflandırması için

kontrol), üç küçük Java programı.

uygun değil, listede “değerlendirildi, elendi” olarak geçebilir.

GazeCapture Dataset (MIT) Günlük cihaz kameralarından Kod okuma verisi içermez;

(webcam, telefon, tablet) toplanmış yaklaşık 1.500

web kamerasından bakış yönü tahmini yapan

katılımcıya ve 2.5 milyondan bilgisayarla görme fazla video karesine ait bakış modellerinin doğruluğunu test

koordinatı veri seti.

etmek için kullanılır.


MPIIGaze / MPIIFaceGaze (Max Planck Institute) https://www.mpi-inf.mpg.de/d epartments/computer-vision-a nd-machine-learning/researc h/gaze-based-human-comput er-interaction/appearance-ba sed-gaze-estimation-in-the-wi ld [URL 🔗](https://www.mpi-inf.mpg.de/departments/computer-vision-and-machine-learning/research/gaze-based-human-computer-interaction/appearance-based-gaze-estimation-in-the-wild)

Standart laptop web kameraları ile günlük çalışma ortamında kaydedilmiş 214.000'den fazla görüntü ve

Farklı aydınlatma ve kafa pozisyonlarında webcam tabanlı bakış takibi algoritmalarının performansını değerlendirmek için

bakış açısı verisi.

benchmark veri setidir.

## DATASET TABLOSU

## Dataset Katılım Deneyi Ham Aynı kod mu? Lisans Ciha Link Durum cı m gaze etiketi verisi zaman) (x, y, z

EMIP (Bednar ik vd.,

216 program cı

aday

n

notuna var, herkes

2020) (Aljehan deneyi göre var aynısını

e vd.

CC-BY Kızıl osf.io Ana [URL 🔗](http://osf.io/53kts)

Var, seviyeli (hiç

Doküma ? (iki kod

anlama görevi 4.0

ötesi /53kt [URL 🔗](http://osf.io/53kts)

, büyü k

[s](http://osf.io/53kts)

msizden (fiksasy


207'sini kullanmı ş)

yüksek on,

okumuş

olası lıkla SMI (201 5 bası n duyu rusu ndan çıkar ım, doğr

deneyi sakkad, olabilir) mliye) AOI

koordin atları). İndirip doğrula

ula)

Novice 37 (39 Acemi/ Ham Evet, aynı CC-BY Tobii https: İkinci [URL 🔗](https://github.com/brains-on-code/NoviceVsExpert)

vs

davet uzman veri var havuz. Herkes 4.0

Pro

[//gith](https://github.com/brains-on-code/NoviceVsExpert)

aday

Expert edilmiş, etiketi (EEG + aynı 32 Java

Fusi ub.co on, m/br [URL 🔗](https://github.com/brains-on-code/NoviceVsExpert)

(EEG + 1 kişi yok. göz)

snippet’ini görüyor, sıra pseudo-rastgel e. Ama 60 dakika sınırı yüzünden sadece 17 / 37 kişi hepsini bitirmiş. Her snippet’i yaklaşık 29-36 kişi görmüş

eye)

yarıda Bunun bırakmı yerine ş, 1 kişi “efficacy

250 Hz, ekra

ains- on-c ode/ [URL 🔗](https://github.com/brains-on-code/NoviceVsExpert)

verisi çok fazla aykırı

” (doğru çözülen görev sayısı /

na Novi mont ceVs e Expe [URL 🔗](https://github.com/brains-on-code/NoviceVsExpert)

(EE G de

rt Ham [URL 🔗](https://github.com/brains-on-code/NoviceVsExpert)

değer dakika) içerdiği ölçülmü

kayd veri:o [URL 🔗](http://osf.io/4hjbd)

için

ş,

edil

[sf.io/](http://osf.io/4hjbd)

çıkarılm ayrıca

miş) 4hjbd [URL 🔗](http://osf.io/4hjbd)

ış)

49 ölçümlü k deneyi m anketi var (yıl, kendini değerle ndirme, bilinen dil sayısı vb.)


Longitu dinal Java course

20: 14 Var

?

? Acemiler her Var,

SMI datas Küçük

acemi (acemi / Makale modülden

deneyi token sonra 3

(hiç

program mli).

düzeyin program

token RED et:,os ama düzeyin -m, f.io/t5 deneyi

de

uzak je9 m etiketi

lama Proposa de

okuyor (4-28 AOI’ler tan maka net,

deneyi l’daki fiksasyo satır, ikisi

mi yok, ikili çoğu

n

sözde kod),

EyeCod (rem le: yedek

e ile

ote) par.n aday [URL 🔗](http://par.nsf.gov/biblio/10267218)

sınıflan verisiyle zorluk modül eşlenmi izleyi sf.go [URL 🔗](http://par.nsf.gov/biblio/10267218)

üniversit dırmayl çalışıyor modül artıyor. ş

e

a birebir ama

Uzmanların

öğrenci uyuşuyo ham (x, hangi

si) + 6 deneyi mli profesy onel (5-28 yıl deneyi m)

r

y)

programları

verinin okuduğu paylaşılı belirtilmemiş.

p

Busjahn

paylaşıl makalesinden madığın doğrula ı yazmıyo r. OSF paketin e bak

EyeTra ? ns reprod uction packag e

?

İşlenme ? miş ham göz takibi verisi var AMA dosyala r “interme diate” (ara aşama) ve “prelimi nary” (ön

?

ci,

[v/bibl](http://par.nsf.gov/biblio/10267218)

120 io/10 Hz 2672 [URL 🔗](http://par.nsf.gov/biblio/10267218)

18 maka le: https: //ieee xplor e.iee e.org /docu ment /946 [URL 🔗](https://ieeexplore.ieee.org/document/9462965)

[2965](https://ieeexplore.ieee.org/document/9462965)

? zeno düşük [URL 🔗](http://zenodo.org/records/10684985)

do.or oncelik [URL 🔗](http://zenodo.org/records/10684985)

g/rec ords/ 1068 [URL 🔗](http://zenodo.org/records/10684985)

deneyi m etiketine

4985 bakama [URL 🔗](http://zenodo.org/records/10684985)

dım. ama amac farklıVer i, gözün insan dikkatini bir nöral kod özetlem e

modelin


çalışma ). Yani temizlen miş, nihai bir veri seti değil.ick le dosyala rı ve Jupyter noteboo k’lar var. Bunları işlemek, EMIP’in düz CSV yapısın a göre daha çok zaman

alır.

Dyslexi 30 (14 Sınıflan

Üç küçük Java

a & code , 16

disleksili dırma Var. Her programı,

e (EyeTra ns) aktarma k için toplanm ış. Deneyi m sınıflan dırması için tasarlan mamış, dolayısı yla deneyi m etiketi tutarlı bir şekilde toplanm ış olmaya

bilir.

Elendi

Var. Satır

Tobii pure. (deneyi X3-1 ulster m etiketi [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

etiketi katılımcı farklı düzen

layout kontrol), yok.

için

kombinasyonl bazlı 20 .ac.u yok [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

(ETRA bilgisay Gruplar Tobii arıyla COK

‘21)

ar

disleksi/ Pro

AOI’ler (120 k/en/ ama [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

KUCUK KOD ve üç Hz), publi ankette [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

bilimleri kontrol. Lab’den AMA lisans Ama tsv: öğrencil katılımcı zaman

AOI

ortal catio n [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

eri -

anketin damgas

karşılaşt de yaş, ı, göz

ırma

program konumu

yapılaca lama

(x, y),

k

deneyi fiksasyo

m)

“deneyi mi gibi n/sakka

mli”

bilgiler d tipi ve toplanm süresi,

yapılan ama ns/ef cıkarıla dırması doğr a96d bılır. (strict, ulam 3a-9 veri [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

forgivin a g,

36f-4 amacı [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

doğr a1d- cok [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

maximu uluğ b928 farklı. [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

u

-c7b leride [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

0,58 6253 STA [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

°

949c pipeline’ [URL 🔗](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

[b](http://pure.ulster.ac.uk/en/publications/efa96d3a-936f-4a1d-b928-c7b6253949cb)

ını


grup

ış

AOI isabetle

kurarke n önce bu veriyle denem e yapmak (scanpa th üret, AOI dizisine çevir) EMIP’in büyük ve karmaşı k dosyala rıyla uğraşm adan önce iyi bir ısınma

eksik. (parti

cipant ri. _data. tsv), yani deneyi m bilgisi dolaylı olarak var, sadece hazır acemi/u zman etiketi

değil

olabilir.

GazeCa ~1.500 Yok Webca Yok (kod verisi ?

Telef githu Gaze on/ta b.co model

pture (MIT)

m/telefo yok) n video kareleri + bakış koordin atı

doğrulu

blet m/C

kam SAIL ğu için, erası Visio STA için

n/Ga uygun zeCa değil

pture

MPIIGa ? (15 Yok

Lapt mpi-i Gaze op nf.m model

Laptop Yok webcam görüntül eri + bakış açısı

?

ze /

olduğun

MPIIFa u ceGaze hatırlıyo

doğrulu

web pg.d

cam e ğu için,

rum, doğrula)

(linki STA için

n

uygun

dokü değil man

notu


nda var)

son iki satır icin:programlama verisi içermiyor. STA için değil, webcam gaze modellerinin doğruluğunu test etmek için.

datasetr bakarken buldugun makaleleri de related work icin ekleyebilirsin.

| DATASET OZET TABLOSU: |   |   |
| --- | --- | --- |
| Sıra | Dataset | Durum |
| 1 | EMIP | Ana aday, hâlâ OSF’te |
|   |   | doğrulanacak |
| 2 | Peitek (2022) | Yedek, aynı 32 snippet, etiket |
|   |   | bizim oluşturacağımız |
| 3 | Longitudinal Java | İkili etiket hazır ama 20 kişi, |
|   |   | uzmanlar farklı koşulda |
| 4 | EyeTrans | Düşük öncelik, |
|   |   | participant.csv kontrol |
|   |   | edilecek |
| 5 | Dyslexia & layout | Elendi, pipeline testi için |
|   |   | yedek |

## PROPOSAL 6 MAKALE

Kaynak Dil/Framewo Algoritma

rk

Veri seti

Özellikler Bizden farkı


Aljehane vd. ? (2023)

Metrik bazlı EMIP (207 Fiksasyon Sınıflandırma

uzmanlık analizi

geliştirici)

sayısı, toplam fiksasyon süresi, satır sayısı, göz

modeli değil, metrik analizi. Kızılötesi veri

bebeği çapı

Peitek vd. (2020)

?

Okuma sırası ? analizi

Bakış sırası Uzmanlık

(sequential gaze)

sınıflandırma sı yok

Ahsan & Obaidellah (2025/26)

?

Makine öğrenmesi, ikili vs 3 seviyeli

?

?

ML tabanlı, biz STA tabanlı

Ahsan & Obaidellah (2023)

?

STA ile kümeleme

?

Scanpath

Sadece acemileri kümeliyor, uzman/acemi sınıflandırma

sı yok

Eraslan vd. ? (2016)

STA (kurucu Web sayfaları Scanpath,

Web alanı, kod değil

makale)

AOI dizisi

Eraslan vd. ? (2020)

STA ile grup ? (otizm / sınıflandırma kontrol) sı

Scanpath

Alan otizm tespiti, ama yöntem bizimkiyle

aynı


## EK MAKALELER

## Kaynak Dil/Framewo Algoritma rk Veri seti Özellikler Bizden farkı

Webcam-Ba ? Hangi

Webcam izleyiciyi araştırma sınıfı ekran izleyiciyle karşılaştırıyor , bireyler arası farkları yakalayıp yakalamadığı na bakıyor.

sed

webcam

Eye-Trackin izleyicisi

yok

g in Code

kullanıldığı

Comprehens özette yok ion (TSE, 2026) https://ieeexp lore.ieee.org/ document/11 329486/ [URL 🔗](https://ieeexplore.ieee.org/document/11329486/)

bilişsel örüntüler. Katılımcılar kalibrasyon ve göreve başlamakta

zorlanmış.

Mokrý (2018), Identificatio n of Novices on the Web

?

makine öğrenmesi

bebeği boyutu ve kafa mesafesi.

modeli. Hangi e-ticaret model olduğu alanı. ?

kullanıyoruz

Hackenbeck ? (2020), Bewertung Maschinelle Lernalgorith men… (tez, Almanca)

Makine öğrenmesi

ile çeşitli

algoritmaların görevler

ın

programlama kaydedilmiş katılımcıların zayıf kaynak

bilgisi için

değerlendiril İçindekiler mesi. Hangi kısmında

algoritmalar ? EyeTribe adı için ayırt edici

geçiyor, doğrula. Katılımcı sayısı ?

WebGazer JavaScript, Herhangi bir Büyük bir Göz

(Papoutsaki tarayıcı

vd., IJCAI 2016)

? Katılımcı

Anlamsal

Fizibilite çalışması,

sayısı özette okuma

örüntüleri ve deneyim token düzeyi sınıflandırma

sı ya da STA yok

Özelliklerden İki çalışmada Fiksasyon, Web alanı,

toplam 72 katılımcı,

sakkad, göz özellik tabanlı

ML. Biz kod okuma ve STA

Eye tracker ? Özetin

ML tabanlı, kızılötesi/özel

görünen

sırasında

kısmına göre cihaz. Tez bazı özellikler olduğu için

veri.

uzmanlığı birbirine çok yakın olduğu

olmamış görünüyor, doğrula

göz algılama uzak kütüphanesiyl çevrimiçi e birleşebilen çalışma ve

içinde çalışıyor

Sadece bakış

görüntüsünde noktası

n çıkarılan özellikler,

veriyor. Kod okuma,


pupil detector küçük bir yüz

tıklama/imleç scanpath ve

ve kullanıcı yüze çalışma. etkileşimi

sınıflandırma yok. Altyapı adayımız

etkileşimleriyl Katılımcı

(kendi kendini kalibre etmek için)

e bilgilendirilen regresyon tabanlı gaze

sayıları ?

estimator.

Eye

? Doğrula

iTracker (CNN)

GazeCapture Yüz ve göz Sadece bakış

Tracking for (derin Everyone öğrenme (Krafka vd., çatısı) CVPR 2016)

: senin

görüntüleri

tahmini,

dokümana (hangi girdiler programlama göre yaklaşık kullanıldığı ?) ya da

1.500 katılımcı, 2,5 milyondan fazla kare

sınıflandırma yok. Hata payı için

referans

Castner vd. (2020), Scanpath Comparison

?

Başlığa göre ? Alan diş

?

Yöntem fikri

derin anlamsal bakış gömmesi (deep semantic gaze embedding) ve scanpath karşılaştırma

panoramik röntgeni okuma, katılımcı sayısı ?

çok yakın (scanpath ile uzman/acemi ayırma), ama alan kod değil ve veri kızılötesi olabilir (doğrula)

for Expertise Classificatio n (OPT)

(ETRA ‘20)

sı. Ayrıntı ?

## OpenFace 2.0

(Baltrušaitis doğrula)

vd., FG 2018)

C++ (GitHub deposundan

Yüz landmark ? Makale

Yüz

Bir araç,

tespiti ve takibi, kafa pozu ve bakış kestirimi. Modeller ? (CE-CLM olduğunu hatırlıyorum,

araç tanıtımı landmark’ları, sınıflandırma

kafa pozu, bakış yönü vektörü

yok. Zoom/Meet’te

n bakış vektörü çıkarmak için aday

doğrula)


Valliappan ? vd. (2020), Smartphone Eye Tracking (Nature Comm.)

? Telefon kamerasıyla bakış tahmini, model türünü doğrula

?

Fiksasyon, Telefon, kod

okuma güçlüğü

okuma yok, deneyim

göstergeleri sınıflandırma

(senin

sı yok.

dokümana Tüketici

göre)

kamerasının okuma analizi için geçerli olduğuna

kanıt

Missler vd. ? (2023), Webcam Eye-Trackin g, Visual Expertise (GMS J Med Educ)

? Webcam Tıp

Göz verisi

Alan histoloji, kod değil. Webcam ile uzmanlık ölçümüne destek

izleyicinin

öğrencileri, doğruluğu

veri kalitesini, çevrimiçi

(ortalama 115,7 px), göz metrikleri, performans.

uzmanlık

histoloji

değişimlerini eğitimi.

yakalama geçerliliğini ve düşük/yüksek performansı ayırt etme güvenilirliğini

Katılımcı sayısı ?

inceliyor.

LookAtChat Web tabanlı. WebGazer.js 5 katılımcıyla Kimin kime Göz teması

(He vd., 2021)

Göz takibi modülü WebGazer.js ile çalışıyor.

tabanlı bakış formatif

baktığı, gaze görselleştirm

hedefi tanıma görüşmeler, yönü,

e amaçlı. Kod okuma, scanpath ve deneyim sınıflandırma

sistem

uzamsal

değerlendirm ipuçları esinin katılımcı sayısı ?

sı yok

bulunmus olan ticari urunler tabloya dahil edilmemistir

datasetlenden gelen makalelerle devam:

## Kaynak Dil/Framewo Algoritma rk Veri seti Özellikler Bizden farkı


Bednarik vd. Dataset (2020), EMIP makalesi.

Yok, veri seti 216 sunuyor.

Fiksasyon, Sınıflandırma

programcı, iki sakkad, AOI yok, sadece

Görevler

Sınıflandırma kod anlama koordinatları, veri sağlıyor.

Java, Python, ya da analiz görevi, 11

deneyim

Kızılötesi

Scala (senin algoritması ekip, 8 ülke, seviyesi ve cihaz. Biz bu

dokümandaki önermiyor nota göre, doğrula). Analiz aracı ?

aynı cihaz ve demografik veriden STA

yazılımla

bilgiler (senin ile trending

## Peitek vd. (2022),

Java (32 snippet).

toplanmış. dokümandaki path

Cihaz büyük nota göre, olasılıkla SMI dosyalardan

(basın duyurusunda n çıkarım,

doğrula)

doğrula)

çıkaracağız

Fiksasyon/sa 37 katılımcı, İlk ve toplam Korelasyon

kkad ayırma: 32 Java

fiksasyon

## Correlates Deney: of Programmer Analiz: Efficacy

PsychoPy. Spearman Pro Fusion atlama / tek / ve scanpath

korelasyonu. 250 Hz + 64 çoklu

Python (Jupyter), EEG için

Matlab/EEGL gücü analizi,

ab

I2MC.

snippet, Tobii süresi,

analizi, sınıflandırma

EEG:

kanallı EEG. fiksasyon

karşılaştırma sı yok. EEG

theta/alpha Veri OSF’te olasılığı, kod içeriyor.

oranı, bant

elemanı kapsamı, EEG bant gücü. Verimlilik = doğru görev /

ICA ile artefakt temizleme. Sınıflandırm a modeli yok

Busjahn vd. Java kaynak Okuma

(2015), Eye Movements in Code

kod + doğal doğrusallığı uzman

metin.

ölçütleri

Framework ? (hikâye

Reading

sırası, yürütme sırası), istatistiksel

dakika

Acemi ve

Bakışın ileri/geri

programcılar. hareketlerine

Al Madi’ye

dayalı

göre 20 kişi doğrusallık gösteriyor. (14 acemi + 6 ölçütleri, kod Scanpath

uzman,

Etiket olarak yıl değil verimlilik kullanıyor

Sınıflandırma yok, sadece okuma biçimi farkını

elemanı bazlı trend analizi

doğrula). SMI bakış

yok. Kızılötesi

karşılaştırma. RED-m 120 dağılımı ? Sınıflandırma Hz (Al

yok

Madi’den)

## Al Madi vd. Java.

Random

20 katılımcı Sekiz metrik: Token bazlı

## (2021), From Kullanılan ML Forest, 10 (14 acemi, 6 uzunluğa

sınıflandırma


## Novice to Expert

kütüphanesi ? (makalede [41] numaralı kaynak, kontrol et). AOI eşleme: EyeCode (token düzeyi)

katlı çapraz doğrulama, min-max normalizasyo nu, %70/%30 tabakalı bölme. İstatistik: Wilcoxon, Friedman, Dunn, Kruskal-Walli

uzman), 1403 token örneği (yaklaşık %40 uzman, %60 acemi). SMI RED-m 120 Hz, replikasyon paketi

göre normalize ilk fiksasyon, tek fiksasyon, bakış süresi, toplam süre ve dört olasılık (fiksasyon, tek fiksasyon, iki+ fiksasyon, atlama). Ek olarak token sıklığı ve uzunluğu. Sonuç: doğruluk %72,3, kesinlik %77, duyarlılık %75,4, F1

ve özellik tabanlı ML. Biz kişinin scanpath’ini STA trending path’leriyle karşılaştırıyor uz. Veri küçük, kızılötesi, gerçek

osf.io/t5je9

zamanlı değil

s

%76,2

## Behroozi & Parnin (2018), Can We Predict Stressful Technical Interview Settings Through Eye-Trackin g?

Beyaz tahta ve kâğıt üzerinde mülakat problemi.

Tek tek göz hareketi olaylarını analiz edip sınıflandırıcıl ar eğitiyor. Hangi sınıflandırıcıl ar olduğu ? (makaleden

11 katılımcı, iki mülakat ortamı (beyaz tahta ve kâğıt). Cihaz

Göz hareketi ölçümleri (hangileri ? makaleden bak). Etiket: kendi bildirdikleri

Hedef deneyim değil stres. Çok küçük örneklem, yüz yüze mülakat, uzaktan/webc am yok. Scanpath ya

Framework ?

?

stres

bak)

da STA yok

[EMIP: The](https://arro.anglia.ac.uk/id/eprint/705904)

[eye](https://arro.anglia.ac.uk/id/eprint/705904)

[movements](https://arro.anglia.ac.uk/id/eprint/705904)

[in](https://arro.anglia.ac.uk/id/eprint/705904)

[programming](https://arro.anglia.ac.uk/id/eprint/705904)

[dataset +2](https://arro.anglia.ac.uk/id/eprint/705904)


## TUM MAKALELERIN TABLO OZET

Sıra

Webcam kod anlama fizibilitesi (TSE 2026)

1

Makale

Neden

Kullanım

Webcam + kod okuma, risk ve sınırlılıklar için en doğrudan kaynak

Related Work, SRS 1.4.4

Al Madi vd. (2021) Göz verisiyle

2

Related Work, dataset

acemi/uzman sınıflandırması (%72,3), aynı zamanda dataset kaynağı

EMIP (Bednarik vd., Ana dataset adayı 2020)

3

Dataset

Castner vd. (2020) Scanpath

4

Related Work

benzerliğiyle uzmanlık sınıflandırması, yöntem fikri aynı

WebGazer (2016)

5

Altyapı adayı, İrem’in Teknik, Related Work alanıyla kesişiyor

Ford vd., uzaktan teknik mülakat

6

Mülakat senaryomuza en yakın akademik dayanak, pozisyon makalesi

Motivasyon, Related Work

Behroozi & Parnin Göz takibi + mülakat Related Work

7

(2018)

\+ tahmin, ama hedef

stres


Peitek vd. (2022)

8

Yedek dataset, mülakat üzerine tartışma

Dataset

LookAtChat (2021) Videokonferansta

9

Related Work (zayıf bağ)

webcam gazı

Busjahn vd. (2015) Acemi/uzman okuma Dataset, arka plan

10

farkı, Longitudinal Java’nın kaynağı

OpenFace 2.0

11

Videodan bakış çıkarma aracı

Teknik (İrem ile ortak)

Missler vd. (2023) Webcam ile uzmanlık Related Work (yedek)

12

ölçümü, ama alan histoloji

Eye Tracking for Everyone (2016)

13

Webcam bakış tahmininin hata sınırları

Teknik

Valliappan vd. (2020)

14

Tüketici kamerasıyla Teknik, arka plan okuma analizi

Mokrý (2018)

15

Acemi tespiti, ama Yedek web alanı ve asıl makale yerine LinkedIn linki var

Ortin vd. (2020)

16

Kod AST’sinden uzmanlık sınıflandırma, göz verisi yok

Arka plan (tek satır)

Hiring is Broken (2019)

17

Mülakat motivasyonu SRS 1.2'de tek cümle

Hackenbeck (2020) Tez, Almanca, özetin Yedek

18

görünen kısmı sınırlı

Hawaii Zoom çalışması

19

Zoom’da bakış davranışı, bizim problemle ilgisi zayıf

Yedek
