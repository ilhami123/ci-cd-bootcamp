# 🌀 Portal 8 — Mors Sinyalleri

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 8/10   ║
║  Tür: Mors Kodu + Parazit Ayıklama    ║
╚════════════════════════════════════════╝
```

Serhat, bu portalın anahtarını **Mors koduyla** göndermiş.
Ama sinyal yolda parazite uğramış — gerçek mesajı gürültüden
ayırmalısın!

---

## Mors Kodu Nedir?

Mors kodu, harfleri **kısa (.)** ve **uzun (-)** sinyallerle ifade eder.

## Mors Alfabesi

```
╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗
║ A  .- ║ B -...║ C -.-.║ D -.. ║ E .   ║ F ..-.║
╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣
║ G --. ║ H ....║ I ..  ║ J .---║ K -.- ║ L .-..║
╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣
║ M --  ║ N -.  ║ O --- ║ P .--.║ Q --.-║ R .-. ║
╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣
║ S ... ║ T -   ║ U ..- ║ V ...-║ W .-- ║ X -..-║
╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣
║ Y -.--║ Z --..║       ║       ║       ║       ║
╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝
```

## Parazitli Sinyal

Serhat'ın sinyali başka bir kaynakla karışmış. 12 sinyal grubu
numaralı olarak geldi:

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   #1:  .-       #2:  -..      #3:  .-.      #4:  --.                ║
║   #5:  .-       #6:  ..-      #7:  -.--     #8:  -.                 ║
║   #9:  ..       #10: .-.      #11: ...      #12: --                 ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
```

## Görev

Serhat'ın notu: *"İki farklı sinyal iç içe geçmiş. Tek numaralı
sinyaller (#1, #3, #5, #7, #9, #11) gerçek mesajı oluşturur.
Çift numaralı sinyalleri (#2, #4, #6, #8, #10, #12) yoksay — parazit!"*

**Adım adım:**
1. Sadece TEK numaralı sinyalleri al
2. Her birini Mors tablosunda çöz

```
#1:  .-    → Tabloda bul → ?
#3:  .-.   → Tabloda bul → ?
#5:  .-    → Tabloda bul → ?
#7:  -.--  → Tabloda bul → ?
#9:  ..    → Tabloda bul → ?
#11: ...   → Tabloda bul → ?
```

> İpucu: `.-` tabloda hangi harfe karşılık geliyor?

**Not:** Türkçe özel karakterleri (Ş, İ, Ü vb.) yazarken endişelenme,
sistem otomatik olarak dönüştürür. Standart harflerle yazabilirsin!

---

Cevabını `cevaplar.py` dosyasındaki `"vaka8"` anahtarına yaz.
