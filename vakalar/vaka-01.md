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

## Polybius Izgarası

Her harf bir **satır-sütun çifti** ile temsil edilir.
İlk basamak satırı, ikinci basamak sütunu gösterir.

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

## Şifreli Mesaj

```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║         33   15   42   23   11   12   11             ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
```

7 sayı = 7 harf. Izgaradan çöz ve birleştir.

---

Cevabını `cevaplar.py` dosyasındaki `"vaka1"` anahtarına yaz.
