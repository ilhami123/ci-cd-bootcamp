# 🌀 Portal 6 — İrem'in Şifre Kasası

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 6/10   ║
║  Tür: Vigenère Şifresi                ║
╚════════════════════════════════════════╝
```

İrem, NEXUS'un şifre uzmanı olarak bu portalın anahtarını
**Vigenère şifresi** ile korumuş.

---

## Vigenère Şifresi Nasıl Çalışır?

Sezar şifresinde her harf aynı sayı kadar kaydırılır. Vigenère'de
ise her harf **farklı miktarda** kaydırılır — kaydırma miktarını bir
**anahtar kelime** belirler.

Çözmek için: Tabloda **anahtar harfin satırını** bul, o satırda
**şifreli harfi** ara, **sütun başlığı** orijinal harfi verir.

## Anahtar Kelime

```
╔══════════════════════════════════════╗
║   Anahtar: N E X U S                ║
║   (Tekrarlı: N E X U S N E)        ║
╚══════════════════════════════════════╝
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

```
    A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
N:  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M
E:  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  A  B  C  D
X:  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W
U:  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T
S:  S  T  U  V  W  X  Y  Z  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R
```

Her şifreli harfi sırasıyla anahtar harfiyle eşle, sonra tablodan çöz.
7 harf = 7 pozisyon.

---

Cevabını `cevaplar.py` dosyasındaki `"vaka6"` anahtarına yaz.
