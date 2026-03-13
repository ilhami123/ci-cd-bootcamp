# 🌀 Portal 9 — Mantık Kapısı

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 9/10   ║
║  Tür: Mantık ve Çoklu Eleme           ║
╚════════════════════════════════════════╝
```

Bu portalın anahtarını **10 muhafızdan** biri koruyor.
5 koşulu uygulayarak doğru muhafızı bul!

---

## 10 Muhafız

```
╔═══════════╦═══════════╦═══════╦═══════╦════════╦════════╗
║  Muhafız  ║  Element  ║  Güç  ║  Yaş  ║Seviye  ║ Bölge  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  REHBER   ║  Su       ║   8   ║  100  ║   3    ║ Kuzey  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  LİDER    ║  Ateş     ║   5   ║  200  ║   5    ║ Güney  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  USTA     ║  Toprak   ║  10   ║   50  ║   2    ║ Doğu   ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  KAPTAN   ║  Hava     ║   3   ║  300  ║   4    ║ Batı   ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  MENTOR   ║  Işık     ║   7   ║  250  ║   3    ║ Kuzey  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  HOCA     ║  Gölge    ║   6   ║  180  ║   1    ║ Güney  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  ŞÖVALYE  ║  Buz      ║   9   ║  150  ║   5    ║ Doğu   ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  KAŞIF    ║  Yıldırım ║   4   ║   90  ║   2    ║ Batı   ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  KOMUTAN  ║  Rüzgar   ║   8   ║  220  ║   4    ║ Kuzey  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  SAVAŞÇI  ║  Lav      ║   7   ║  175  ║   3    ║ Güney  ║
╚═══════════╩═══════════╩═══════╩═══════╩════════╩════════╝
```

## Koşullar

```
📌 Koşul 1: Doğru muhafızın gücü 6'dan büyüktür.
📌 Koşul 2: Doğru muhafızın yaşı 200'den küçüktür.
📌 Koşul 3: Doğru muhafızın seviyesi 5 değildir.
📌 Koşul 4: Doğru muhafızın bölgesi Kuzey veya Güney'dir.
📌 Koşul 5: Doğru muhafızın adı 7 harften kısadır.
```

Tüm koşulları sırasıyla uygula. Geriye kalan tek
muhafızın adı, portalın anahtarıdır.

---

Cevabını `cevaplar.py` dosyasındaki `"vaka9"` anahtarına yaz.
