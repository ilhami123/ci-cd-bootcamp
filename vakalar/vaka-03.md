# 🌀 Portal 3 — Makinelerin Dili

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 3/10   ║
║  Tür: 8-Bit Binary Çözme              ║
╚════════════════════════════════════════╝
```

Mehmet, bu portalın anahtarını **8 bitlik binary (ikili sayı sistemi)**
ile şifrelemiş. Bilgisayarların dilini çözebilir misin?

---

## Binary Nasıl Çalışır?

Bilgisayarlar sadece 0 ve 1'lerle konuşur. 8 bitlik bir sayıda
her basamak, sağdan sola 2'nin artan kuvvetlerini temsil eder.
Sadece **1** olan basamakların değerlerini topla!

```
Basamak değeri:  128   64   32   16    8    4    2    1
Örnek:             0    0    0    1    0    0    1    1  →  16+2+1 = 19
```

## Harf-Sayı Tablosu

```
A=1   B=2   C=3   D=4   E=5   F=6   G=7   H=8   I=9
J=10  K=11  L=12  M=13  N=14  O=15  P=16  Q=17  R=18
S=19  T=20  U=21  V=22  W=23  X=24  Y=25  Z=26
```

## Şifreli Mesaj

```
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   00000011  00000101  00010011  00000001  00010010  00000101  00010100 ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

Her 8 bitlik grubu onluk sayıya çevir, sonra harf tablosundan
karşılığını bul. 7 grup = 7 harf.

Her grupta sağdan sola basamak değerleri:
```
  128  64  32  16  8  4  2  1
```

Sadece **1** olan basamakların değerlerini topla!

> İpucu: `00000011` → sadece son iki basamak 1 → 2+1 = 3 → Harf tablosunda 3 = C


---

Cevabını `cevaplar.py` dosyasındaki `"vaka3"` anahtarına yaz.
