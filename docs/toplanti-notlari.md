# Toplantı Notları

## Toplantı 1 — 7 Ekim 2026 (hocalarla)

Sonraki: **21 Ekim 2026, 13:00** (hocalarla, 15 günde bir). Ekip içi: haftada bir.

### Kararlar

- Repo **public** olur. Doğrudan push yalnızca seçili contributor'lara açık, diğerleri PR ile katkı verir. PR'lar review ister (branch protection). Hocalar böylece erişir.
- LaTeX ve BibTeX projeye dahil.
- Agile çalışılır.
- Literatür taraması ana başlangıç noktası. Makaleler ekip içinde bölüşülür (aşağıda).

### Todo (21 Ekim'e kadar)

- [ ] Ortak Google Drive/Doc aç, hocaları ekle (rapor yazımı)
- [ ] Repoyu public yap, branch protection kur (PR + review zorunlu), hocaları ekle (Şükrü Hoca)
- [ ] Proje yönetim aracı kararı: Trello / Jira / GitHub Projects (araştırma aşağıda)
- [ ] Literatür taraması + karşılaştırma tablosu taslağı
- [ ] Public dataset listesi
- [ ] Kaynakları BibTeX olarak topla (DOI / online kütüphane export)
- [ ] Use case diyagramı taslağı
- [ ] Rol dağılımı: herkes toplantıya rolüyle gelir

### Hocasız toplantı için tartışma

- **Overleaf mı, başka bir LaTeX engine mi?** Hoca premium hesabıyla destek verebilir. Görüş: gereksiz. LaTeX'i elle yazmayacağız, iyi bir engine yeterli. Karar bekliyor.

### Literatür bölüşümü

Sahip sütununu doldurun.

| # | Kaynak | Sahip |
|---|--------|-------|
| 1 | Aljehane vd. 2023, bilişsel yük ve uzmanlık (ETRA) | |
| 2 | Peitek vd. 2020, okuma sırası (ICPC) | |
| 3 | Ahsan & Obaidellah 2025, ML ile yetkinlik (TOCE) | |
| 4 | Ahsan & Obaidellah 2023, STA ile kümeleme (ETRA) | |
| 5 | Eraslan vd. 2016, STA algoritması (ACM TWEB) | |
| 6 | Eraslan vd. 2020, STA ile otizm tespiti (W4A) | |
| 7 | Ek tarama: webcam tabanlı gaze tahmini (WebGazer vb.) ve doğruluk | |
| 8 | Ek tarama: public dataset'ler (EMIP vb.) | |

Her makale için çıkarılacak: kullanılan dil/framework, algoritma, veri seti, var/yok özellikleri, bizden farkı. Çıktı karşılaştırma tablosuna ve SRS Related Work'e girer.

### Proje yönetim aracı: Trello vs Jira vs GitHub Projects (ücretsiz plan, 2026)

Ekip 4 kişi, hocalarla 6. Karar ekiple verilecek.

| | Trello Free | Jira Free | GitHub Projects |
|---|---|---|---|
| Kullanıcı | 10 collaborator, 11+ olursa board'lar salt okunur | 10 kullanıcı | Sınırsız (public repo) |
| Limit | 10 board / workspace | Sınırsız proje ve issue | Sınırsız |
| Görünümler | Kanban | Scrum + Kanban, backlog, timeline | Board, tablo, roadmap, iterasyon |
| Otomasyon | ~250 run/ay (kaynaklar çelişiyor) | 100 run/ay | Dahili workflow'lar + Actions |
| Eksikler | Sprint yok | Herkes admin, audit log yok, 120 gün hareketsizlikte site kapanır | Rapor derinliği Jira'dan az |
| Öğrenci indirimi | Yok, yalnızca kurumlara %50 | Yok, yalnızca kurumlara | Gerek yok, ücretsiz |

Öneri: **GitHub Projects**. Repo zaten GitHub'da: issue, PR ve board aynı yerde, hocalar ek hesap açmadan görür. Alternatif: **Jira Free**, daha güçlü sprint ve rapor ister ve ikinci bir araç kabul ederseniz. Trello'da sprint yok, ele alınmadı. Rakamlar üçüncü taraf sitelerden; kurulumdan önce resmi sayfalardan doğrula.

Kaynaklar: [Atlassian: Free Jira plan](https://support.atlassian.com/jira-cloud-administration/docs/what-is-the-free-jira-cloud-plan/), [ONES Jira free 2026](https://ones.com/blog/jira-task-management-free-plan-what-you-actually-get-in-2026/), [CostBench Trello](https://costbench.com/software/project-management/trello/free-plan/), [Atlassian Trello limitleri](https://www.atlassian.com/ja/blog/trello-new-collaborator-limits), [Atlassian Community eğitim fiyatı](https://community.atlassian.com/forums/Trello-questions/Trello-pricing-for-education-institutions/qaq-p/2654889), [CostBench GitHub free](https://costbench.com/software/developer-tools/github/free-plan), [GitHub blog](https://github.blog/developer-skills/github/github-team-or-free-how-to-choose-the-right-plan)

### Notlar (olduğu gibi, sonraki toplantıda incelenecek)

**SRS / SDD**
- Literatürle paralel başlanır. Use case diyagramıyla başla; basit olması yanlış değil, projenin ne olacağını göstermeli.
- Use case'de ürünün nasıl çalışacağı belirlenir (kullanıcı video analizini aktifleştirir vb.).
- Constraint'ler tanımlanır (ör. webcam şu kalitede olmalı).
- Software architecture çıkarılır.
- Literatür taramasının SRS'te ayrı puanlaması var.

**Teknik araştırma**
- Google Meet extension nasıl yapılır, mimarisi ne olur.
- Google Meet API ile video nasıl çekilir (en basitinden). Alternatifler değerlendirilecek, Zoom'a da bakılacak.
- Göz takibi: feature'lar ve kütüphaneler ayrı araştırılır.
- Sonraki adım: videodaki gözü takip edip nereye baktığını bulmak.
- Kalibrasyon için kullanıcıdan belirli bir yere bakması istenebilir.
- Sapma (error rate) ve limitasyonlar olacak. Sapma ne kadar azsa o kadar iyi.

**Dönem sonu**
- Hedef parçalara bölünür, rol dağılımı yapılır. Toplantılara bu rolle gelinir (sorumluluk paylaşımı).
- Dönem sonunda working prototype çıkmalı. Kusursuz olması gerekmez, kabaca gösterilebilmeli.
- Parçalar ayrı çalışmalı ve birbirine entegre olmalı. **Entegrasyon yoksa puan yok.** Tek parçanın mükemmel olması yetmez.
