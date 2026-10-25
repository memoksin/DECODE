# **DEC 36 TASLAK - SRS 1.3 Related Work & Comparison Table** 

# 1.3 Related Work 

In the literature, studies examining programmers' code comprehension processes and expertise levels predominantly rely on specialized infrared eye-tracking hardware (e.g., Tobii, SMI). Al Madi et al. (2021) re-analyzed eye-tracking data previously collected by Busjahn et al. (2015), employing 8 token-level eye-movement metrics to distinguish novice programmers from experts with 72.3% accuracy using a Random Forest classifier. However, this approach evaluates token-level aggregate statistics rather than modeling sequential scanpaths, and it depends strictly on high-cost infrared equipment. Investigating the feasibility of consumer-grade RGB webcams for code comprehension tasks, recent empirical findings (IEEE TSE, 2026) show that webcams capture semantic line-level reading patterns reasonably well but struggle at the fine-grained token level and exhibit calibration sensitivities. 

For web-based remote gaze tracking, Papoutsaki et al. (2016) developed WebGazer.js, which enables zero-installation client-side gaze estimation within standard web browsers using user interactions (e.g., mouse clicks) for continuous self-calibration. Despite its flexibility, WebGazer.js provides raw gaze coordinates without intrinsic mechanisms for code comprehension or expertise prediction. Addressing expertise modeling via gaze trajectory similarity, Castner et al. (2020) demonstrated deep semantic gaze embedding and scanpath comparison methods to classify expertise in medical image reading. Additionally, Scanpath Trend Analysis (STA), introduced by Eraslan et al. (2016, 2020), establishes an algorithmic methodology to identify dominant, sequential visual search patterns across user cohorts. DECODE addresses these limitations by eliminating proprietary infrared hardware in remote interview contexts. Using standard RGB webcam feeds captured directly via WebRTC, the system maps gaze trajectories onto syntactic Area of Interest (AOI) code blocks and applies STA to classify candidate proficiency objectively and near-real-time. 

|**Study /**<br>**Source**<br>**(Kaynak)**|**Languag**<br>**e /**<br>**Framew**<br>**ork**<br>**(Dil/Fra**<br>**mework)**|**Algorith**<br>**m**<br>**(Algorit**<br>**ma)**|**Dataset**<br>**&**<br>**Hardwar**<br>**e (Veri**<br>**Seti &**<br>**Donanım**<br>**)**|**Features**<br>**&**<br>**Metrics**<br>**(Özellikl**<br>**er)**|**Strength**<br>**s (Güçlü**<br>**Yönleri)**|**Weakne**<br>**sses**<br>**(Zayıf**<br>**Yönleri)**|**Different**<br>**iation**<br>**from**<br>**DECODE**<br>**(Bizden**<br>**Farkı)**|
|---|---|---|---|---|---|---|---|
|Al Madi<br>et al.<br>(2021)|Java,<br>EyeCode|Random<br>Forest<br>(10-fold<br>cross-vali<br>dation),<br>Wilcoxon<br>tests|Longitudi<br>nal Java<br>dataset<br>(20<br>participa<br>nts: 14<br>novice, 6<br>expert),<br>SMI<br>RED-m<br>120 Hz|8<br>token-lev<br>el metrics<br>(first<br>fixation<br>duration,<br>total<br>time,<br>regressio<br>n,<br>skipping<br>probabilit<br>y)|Token<br>düzeyind<br>e nesnel<br>metriklerl<br>e %72,3<br>ikili<br>sınıflandı<br>rma<br>başarısı<br>sağlamas<br>ı.|Küçük<br>örneklem<br>boyutu<br>(n=20);<br>özel ve<br>pahalı<br>donanım<br>a bağımlı<br>olması.|Token<br>düzeyind<br>e özellik<br>tabanlı<br>klasik<br>makine<br>öğrenme<br>si<br>kullanır;<br>scanpath<br>trendlerin<br>i (STA)<br>modelle<br>mez.|



|Castner<br>et al.<br>(2020)|Python,<br>PyTorch|Deep<br>semantic<br>gaze<br>embeddi<br>ng,<br>scanpath<br>comparis|Panorami<br>c dental<br>radiograp<br>hs<br>(OPT),<br>research-<br>grade|Scanpath<br>similarity<br>scores,<br>deep<br>visual<br>attention<br>embeddi|Sıralı<br>görsel<br>arama<br>davranışı<br>nı ve<br>uzman-a<br>cemi|Kod<br>sözdizimi<br>içermem<br>esi; statik<br>iki<br>boyutlu<br>medikal|Yöntem<br>yaklaşımı<br>DECODE<br>ile<br>benzerdir<br>ancak<br>kaynak|
|---|---|---|---|---|---|---|---|
|||on|eye<br>tracker|ngs|scanpath<br>sapmalar<br>ını derin<br>öğrenme<br>yle|görüntüle<br>rle sınırlı<br>olması.|kod<br>okuma<br>yerine<br>medikal<br>görüntü|
||||||başarıyla<br>yakalama<br>sı.||analizine<br>odaklanır<br>.|



|WebGaz<br>er|JavaScri<br>pt|Pupil<br>detector,|Crowdso<br>urced|Client-sid<br>e|Ek<br>yazılım|Bakış<br>açısı|Yalnızca<br>ekrandak|
|---|---|---|---|---|---|---|---|
|(Papouts<br>aki et al.,<br>2016)|(In-brows<br>er)|interactio<br>n-informe<br>d Ridge<br>Regressi<br>on|large-sca<br>le web<br>interactio<br>ns,<br>standard<br>RGB<br>webcam|self-calibr<br>ation via<br>mouse<br>clicks/cur<br>sor,<br>continuo<br>us (x, y)<br>gaze<br>coordinat|veya özel<br>donanım<br>gerektirm<br>eden<br>sıradan<br>web<br>kamerası<br>yla<br>tarayıcıd|hatasının<br>(100–150<br>px)<br>yüksek<br>olması;<br>aydınlat<br>ma ve<br>baş<br>hareketle|i anlık<br>koordinat<br>ı kestirir;<br>kod<br>analizi,<br>bilişsel<br>yük veya<br>uzmanlık<br>sınıflandı|
|||||es|a<br>çalışabil<br>mesi.|rine<br>hassasiy<br>eti.|rması<br>yapmaz.|



|Webcam<br>Code<br>Study<br>(TSE,<br>2026)|Python,<br>Web-bas<br>ed client|Appeara<br>nce-base<br>d CNN<br>gaze<br>estimatio<br>n, spatial<br>fixation<br>filtering|Code<br>compreh<br>ension<br>task<br>cohort,<br>commerc<br>ial<br>webcam<br>vs.<br>high-end<br>eye<br>tracker|Macro<br>semantic<br>reading<br>patterns,<br>token-lev<br>el<br>resolutio<br>n<br>threshold<br>s|Standart<br>web<br>kamerası<br>nın kod<br>okuma<br>görevleri<br>ndeki<br>makro<br>geçerliliği<br>ni ve<br>sınırlarını<br>deneysel<br>olarak<br>ortaya<br>koyması.|Katılımcıl<br>arın<br>kalibrasy<br>onda<br>zorlanma<br>sı; token<br>seviyesin<br>de<br>yüksek<br>hata<br>oranları<br>ve düşük<br>çözünürl<br>ük.|Yalnızca<br>donanım<br>fizibilite<br>çalışması<br>dır;<br>uzmanlık<br>sınıflandı<br>rma<br>modeli<br>veya STA<br>boru hattı<br>barındırm<br>az.|
|---|---|---|---|---|---|---|---|
|Behroozi<br>& Parnin<br>(2018)|Python /<br>Machine<br>learning<br>framewor<br>ks|Eye-mov<br>ement<br>event<br>analysis,<br>supervise<br>d<br>classifier<br>s|11<br>participa<br>nts<br>across<br>two<br>technical<br>interview<br>settings<br>(whitebo|Fixation<br>durations<br>, saccade<br>frequenc<br>y,<br>self-repor<br>ted|Teknik<br>mülakat<br>ortamınd<br>aki<br>bilişsel<br>yük ve<br>fizyolojik<br>stresi<br>gerçek|Örnekle<br>min çok<br>küçük<br>olması<br>(n=11);<br>giyilebilir<br>özel<br>donanım|Hedef<br>değişkeni<br>deneyim<br>düzeyi<br>değil<br>strestir;<br>yüz yüze<br>mülakata<br>odaklanır|



|ard vs.|stress|senaryod|gerektirm|, uzaktan|
|---|---|---|---|---|
|paper),|levels|a|esi.|webcam|
|wearable||modelle||ve STA|
|eye||mesi.||içermez.|
|tracker|||||



DECODE JavaScri WebRTC Standard Dynamic Ek Web Web (Propose pt / capture + RGB line-block donanım kamerası kamerası d Node.js, Syntactic Webcam, AOI sız kaynaklı ndan System) Python AOI WebRTC sequenc çalışması açısal gelen mapping (MiroTalk es, , uzaktan hata payı bakışı + SFU), cohort mülakat (2.0°–3.5 satır/blok Scanpath EMIP trending platformu °) ve AOI'leri Trend benchma path na ortam ve STA Analysis rk similarity, gömülü ışığı ile (STA) dataset cognitive olması, hassasiy işleyerek load sıralı kod eti. nesnel metrics okuma aday akışını kıdem modelle sınıflandı mesi. rması üretir. 

## **NASIL HAZIRLANDI VE YAPILMASI GEREKEN DÜZENLEMELER:** 

Sütunların Kaynağı ve Eşleşme Mantığı PDF dec 33 36 31 de bulunan taslak 

Study / Source (Kaynak): PDF'in 16, 17 ve 20. sayfalarındaki Kaynak sütunudur. Çalışmanın adını ve yazarlarını içerir. 

Language / Framework (Dil/Framework): PDF'in 16, 17 ve 20. sayfalarındaki Dil/Framework sütunudur. Modelin, deneyin veya platformun yazıldığı programlama dilini ve kütüphaneleri belirtir. 

Algorithm (Algoritma): PDF'in 16, 17 ve 20. sayfalarındaki Algoritma sütunudur. Çalışmada kullanılan sınıflandırıcı, kestirim yöntemi veya analiz algoritmasını gösterir. 

Dataset & Hardware (Veri Seti & Donanım): PDF'in Veri seti sütunu ile donanım notlarının birleşimidir. Kaç katılımcı olduğu, hangi kod parçalarının okunduğu ve kullanılan göz izleme cihazı yer alır. 

Features & Metrics (Özellikler): PDF'in 16, 17 ve 20. sayfalarındaki Özellikler sütunudur. Çıkarılan fiksasyon, sakkad, bilişsel yük veya kod elemanı metriklerini içerir. 

Strengths (Güçlü Yönleri - Yeni Eklenen): CNG491 SRS şablonunun "1.3 Related Work" bölümündeki zorunlu kural gereğidir. İncelenen çalışmanın literatüre sunduğu en belirgin katkı, yüksek doğruluk oranı veya pratik üstünlüğüdür. Weaknesses (Zayıf Yönleri - Yeni Eklenen): Yine SRS şablonunun zorunlu kıldığı sütundur. Çalışmanın donanım pahalılığı, küçük örneklem boyutu, kalibrasyon zorluğu veya düşük çözünürlük gibi sınırlarını belirtir. 

Differentiation from DECODE (Bizden Farkı): PDF'in 16, 17 ve 20. sayfalarındaki Bizden farkı sütunudur. DECODE'un bu çalışmadan hangi teknik yaklaşımla (webcam, STA, gerçek zamanlı mülakat vb.) ayrıldığını gösterir. 

ek sutun eklenmesi gerekicek mi kontrol et text leri tekrar duzenle format vb srs e gecirilmedi 

