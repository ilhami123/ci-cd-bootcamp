# 🌀 Portal 6 — İrem'in Şifre Kasası

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 6/10   ║
║  Tür: Vigenère Şifresi                ║
╚════════════════════════════════════════╝
```

İrem, NEXUS'un şifre uzmanı olarak bu portalın anahtarını
**Vigenère şifresi** ile korumuş. Sezar şifresinin çok daha güçlü
bir versiyonu olan bu yöntemi çözebilir misin?

---

## Vigenère Şifresi Nedir?

Sezar şifresinde her harf **aynı sayı** kadar kaydırılır. Vigenère'de
ise her harf **farklı miktarda** kaydırılır — kaydırma miktarını bir
**anahtar kelime** belirler!

**Şifreleme:** Anahtar harfin alfabedeki sırası kadar ileri kaydır.
**Çözme:** Anahtar harfin alfabedeki sırası kadar **geri** kaydır.

> A=0, B=1, C=2, ... N=13, ... Z=25

## Anahtar Kelime

```
╔══════════════════════════════════╗
║   Anahtar: N E X U S             ║
║   (Tekrarlı: N E X U S N E)     ║
╚══════════════════════════════════╝
```

## Şifreli Mesaj

```
╔══════════════════════════════════════╗
║                                      ║
║       N  R  X  B  L  N  V            ║
║                                      ║
╚══════════════════════════════════════╝
```

## Çözme Tablosu

Aşağıdaki tabloda **anahtar harfin satırını** bul, o satırda
**şifreli harfi** ara, **sütun başlığı** orijinal harfi verir:

```
    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
N:  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M
E:  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D
X:  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W
U:  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T
S:  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
```

## Görev

Her şifreli harfi anahtar harfiyle eşle, sonra tablodan çöz:

```
Pozisyon   Şifreli   Anahtar   → Tabloda satır bul, şifreli harfi ara → Orijinal
───────────────────────────────────────────────────────────────────────────────
   1.         N         N       → N satırında N'yi bul → sütun başlığı = ?
   2.         R         E       → E satırında R'yi bul → sütun başlığı = ?
   3.         X         X       → X satırında X'i bul → sütun başlığı = ?
   4.         B         U       → U satırında B'yi bul → sütun başlığı = ?
   5.         L         S       → S satırında L'yi bul → sütun başlığı = ?
   6.         N         N       → N satırında N'yi bul → sütun başlığı = ?
   7.         V         E       → E satırında V'yi bul → sütun başlığı = ?
```

> İpucu: N satırında N harfini bul → sütun başlığına bak → A

---

Cevabını `cevaplar.py` dosyasındaki `"vaka6"` anahtarına yaz.
