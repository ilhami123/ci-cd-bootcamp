# 🌀 Portal 1 — Hoşgeldin Portalı

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 1/10   ║
║  Tür: Polybius Izgarası               ║
╚════════════════════════════════════════╝
```

Gülşah, ilk portala bir hoşgeldin mesajı bırakmış. Ama mesajı
antik bir şifreleme yöntemiyle — **Polybius Izgarası** ile gizlemiş!

---

## Polybius Izgarası Nedir?

Antik Yunanlı tarihçi Polybius tarafından icat edilen bu yöntemde,
her harf bir **satır-sütun çifti** ile temsil edilir. İlk basamak
satırı, ikinci basamak sütunu gösterir.

```
        1     2     3     4     5
      ┌─────┬─────┬─────┬─────┬─────┐
  1   │  A  │  B  │  C  │  D  │  E  │
      ├─────┼─────┼─────┼─────┼─────┤
  2   │  F  │  G  │  H  │  I  │  J  │
      ├─────┼─────┼─────┼─────┼─────┤
  3   │  K  │  L  │  M  │  N  │  O  │
      ├─────┼─────┼─────┼─────┼─────┤
  4   │  P  │  R  │  S  │  T  │  U  │
      ├─────┼─────┼─────┼─────┼─────┤
  5   │  V  │  Y  │  Z  │  Ö  │  Ü  │
      └─────┴─────┴─────┴─────┴─────┘
```

> Örnek: **22** → Satır 2, Sütun 2 → **G**

## Şifreli Mesaj

Gülşah'ın bıraktığı şifreli koordinatlar:

```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║         33   15   42   23   11   12   11             ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

## Görev

Her iki basamaklı sayıyı Polybius Izgarası'nda çöz.
İlk basamak **satır**, ikinci basamak **sütun** numarasıdır.

```
33 → Satır ?, Sütun ? → ?
15 → Satır ?, Sütun ? → ?
42 → Satır ?, Sütun ? → ?
23 → Satır ?, Sütun ? → ?
11 → Satır ?, Sütun ? → ?
12 → Satır ?, Sütun ? → ?
11 → Satır ?, Sütun ? → ?
```

7 sayı = 7 harf. Birleştirdiğinde Gülşah'ın hoşgeldin mesajını bulacaksın!

> İpucu: 33 → Satır 3, Sütun 3 → Izgarada bu hücrede hangi harf var?

---

Cevabını `cevaplar.py` dosyasındaki `"vaka1"` anahtarına yaz.

> `cevaplar.py` dosyasına tıkla → sağ üstteki **kalem (✏️) ikonuna** bas → cevabını yaz → **Commit changes** butonuna tıkla.
