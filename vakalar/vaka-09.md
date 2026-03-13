# 🌀 Portal 9 — Mantık Kapısı

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 9/10   ║
║  Tür: Mantık ve Çoklu Eleme           ║
╚════════════════════════════════════════╝
```

Son portalın anahtarını **10 muhafızdan** biri koruyor. 5 ipucunu
sırasıyla uygulayarak doğru muhafızı bulabilir misin?

---

## 10 Muhafız

```
╔═══════════╦═══════════╦═══════╦═══════╦════════╦════════╗
║  Muhafız  ║  Element  ║  Güç  ║  Yaş  ║Seviye  ║ Bölge  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  REHBER   ║  Su       ║   8   ║  100  ║   3    ║ Kuzey  ║
╠═══════════╬═══════════╬═══════╬═══════╬════════╬════════╣
║  LIDER    ║  Ateş     ║   5   ║  200  ║   5    ║ Güney  ║
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

## İpuçları

Core Crew şu notları bırakmış:

```
📌 İpucu 1: "Doğru muhafızın gücü 6'dan büyüktür."

📌 İpucu 2: "Doğru muhafızın yaşı 200'den küçüktür."

📌 İpucu 3: "Doğru muhafızın seviyesi 5 değildir."

📌 İpucu 4: "Doğru muhafızın bölgesi Kuzey veya Güney'dir."

📌 İpucu 5: "Doğru muhafızın adı 7 harften kısadır."
```

## Görev

Her ipucunu sırasıyla uygulayarak muhafızları ele:

**Adım 1:** Güç > 6 olanlar kimler? (Diğerlerini ele!)
**Adım 2:** Kalanlardan yaşı < 200 olanlar?
**Adım 3:** Kalanlardan seviyesi 5 olmayanlar?
**Adım 4:** Kalanlardan bölgesi Kuzey veya Güney olanlar?
**Adım 5:** Kalanlardan adı 7 harften kısa olanlar?

Geriye kalan tek muhafızın adı, portalın anahtarıdır!

> İpucu: İlk elemeden sonra 6 muhafız kalır.
> SAVAŞÇI = 7 harf, REHBER = 6 harf...

---

Cevabını `cevaplar.py` dosyasındaki `"vaka9"` anahtarına yaz.
