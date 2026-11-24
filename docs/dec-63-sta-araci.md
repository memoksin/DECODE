# DEC-63 — STA aracını indir ve örnek girdiyle çalıştır

Durum: araç çalışıyor (24 Kasım 2026, Mehmet + agent). Yalnızca **sentetik** girdiyle denendi.

## Sonuç

- Kullanılacak araç: **STA-DS**, `sta-ds/sta-ds-custom-participantbased.py` (Python 3) [1]. Ek paket gerekmiyor (yalnızca stdlib).
- Girdi doğrudan AOI dizisi: katılımcı, fixation süresi, AOI numarası. DEC-66'nın çıktısı (katılımcı başına AOI + süre) bu biçime kolayca çevrilir.
- Çıktı: trending path (ör. `AEHEDI`) + tolerance level + trending path'in bireysel dizilere benzerlik yüzdesi (string edit distance).
- Aynı dosyada `computeSimilarity` var: bir diziyi bir trending path'le karşılaştırıyor. DEC-68 (string matching) bunu kullanabilir.
- Eski `STA.py` Python 2; ham (x, y) gaze + AOI dikdörtgenleri alıyor. Bizim için gerekmiyor.

## Yöntem

1. Repo klonlandı: `https://github.com/SukruEraslan/sta`, commit `8c3939e` (21 Ekim 2025). Klon yerel (`local/`, git-ignored).
2. Elle iki grup dizi yazıldı, 3×3 grid, AOI `A`–`I` (satır satır). Her grupta 4 katılımcı. **Gerçek veri değil.**
   - novice: satır satır okuma, tekrarlarla (`ABCDEFGHI`, `ABCADEFGHI`, `ABDEFEGHI`, `ABCDEFGHGI`)
   - experienced: imza → ana mantık → dönüş (`AEHEI`, `AEHI`, `ADEHI`, `AEHEHI`)
   - Süreler yapay: sırayla 200/250/300 ms.
3. Çalıştırma (`experiments/dec-63/`):
   ```
   python3 make_synthetic.py
   python3 run_sta.py <sta-repo>/sta-ds/sta-ds-custom-participantbased.py synthetic_novice.tsv
   ```
   `run_sta.py` upstream script'i modül olarak yükler; yalnızca veri dosyasını ve AOI adlarını değiştirir (upstream, başka bir çalışmanın hemşirelik AOI adlarını basıyor). Algoritma değişmedi. Tolerance level 0.50–0.99 arasında optimize edilir (upstream varsayılanı).

## Ölçümler

| Grup | Trending path | Tolerance | Benzerlik medyan / min / max (%) |
|---|---|---|---|
| novice (sentetik) | `ABDEFGAHEGI` | 0.99 | 63.64 / 54.55 / 72.73 |
| experienced (sentetik) | `AEHEDI` | 0.50 | 75.00 / 50.00 / 83.33 |

Ham çıktı: `experiments/dec-63/out_novice.txt`, `out_experienced.txt`.

Novice path'inde `A` iki kez ve `C` yok. Neden:
- STA aynı AOI'ye tekrar bakışları ayrı örnek sayar (`A1`, `A2`) ve örnekleri toplam süreye göre numaralar. N2'de iki `A` aynı süredeydi (200 ms); ilk bakış `A2`, tekrar `A1` oldu.
- Tolerance 0.90 ve üstünde `C` (4 kişiden 3'ünde) birinci geçişte elenir. 0.50–0.75'te `C` geri gelir: `ABDCEFGAHEIG`, benzerlik 58.3.
- Yani hata değil, STA'nın tasarımı + yapay süreler + 4 kişilik küçük örnek.

Donanım/yazılım: Apple M4 Max, macOS 27.2.1, Python 3.15.2. Süre ölçülmedi (anında bitiyor).

## Sınırlamalar

- Sonuçlar sentetik; deneyim farkı veya sınıflandırma doğruluğu hakkında bir şey söylemez.
- Makineye bağlı değil: saf Python, rastgelelik yok, aynı girdi aynı çıktıyı verir.
- Girdi kısıtları (kaynak koddan): dosyanın ilk satırı başlık; en az 25 sütun; sondaki boş satır hataya yol açar; AOI numarası 0–25 (harf `A`–`Z`), negatif değer atlanır; 13 ve 14 numaralı AOI birleştirilir (upstream çalışmaya özgü — bizim veride kaldırılmalı).
- Gerçek süreler ve daha çok katılımcı tekrar-ziyaret etkisini değiştirir; gerçek veride tekrar bakılmalı.

## Todo

- [ ] DEC-66 çıktısını bu girdi biçimine çeviren küçük dönüştürücü (DEC-67 sahibi karar verir).
- [ ] 13→14 AOI birleştirme satırı bizim veride devre dışı kalmalı.
- [ ] DEC-68: `computeSimilarity` / `getStringEditDistance` doğrudan kullanılabilir mi, bakılacak.

## SRS için cümle

> Trending paths are produced with the participant-based STA-DS implementation of Scanpath Trend Analysis [1], which takes each participant's sequence of AOIs with fixation durations and returns the trending path with an optimised tolerance level.

## Kaynaklar

1. Eraslan, S. (2025). *STA: Scanpath trend analysis* [Computer software]. GitHub. https://github.com/SukruEraslan/sta (commit 8c3939e, 21 Oct 2025)
2. Eraslan, S., Yesilada, Y., & Harper, S. (2016). Scanpath trend analysis on web pages: Clustering eye tracking data. *ACM Transactions on the Web, 10*(4), Article 20. https://doi.org/10.1145/2970818
3. Eraslan, S., Yesilada, Y., & Harper, S. (2017). Trend analysis in eye tracking scanpaths with a tolerance. *Proceedings of EICS 2017*. ACM.
