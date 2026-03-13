# 🌀 Portal 5 — Koordinat Haritası

```
╔════════════════════════════════════════╗
║  NEXUS Portal Sistemi — Portal 5/10   ║
║  Tür: Yol İzleme                      ║
╚════════════════════════════════════════╝
```

Nigina, bu portalın anahtarını bir **harf haritasının** içine gizlemiş.
Ama bu sefer tek tek koordinat aramak yetmez — bir **yol** izleyerek
harfleri toplamalısın!

---

## Portal Haritası (6×8)

```
         Sütun-1   Sütun-2   Sütun-3   Sütun-4   Sütun-5   Sütun-6   Sütun-7   Sütun-8
        ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
Satır-1 │    K    │    Ş    │    P    │    R    │    G    │    İ    │    M    │    N    │
        ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Satır-2 │    D    │    L    │    A    │    V    │    Ü    │    H    │    B    │    Ç    │
        ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Satır-3 │    Y    │    E    │    T    │    O    │    F    │    S    │    Z    │    U    │
        ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Satır-4 │    Ö    │    C    │    A    │    N    │    J    │    R    │    İ    │    W    │
        ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Satır-5 │    S    │    T    │    K    │    D    │    L    │    M    │    H    │    O    │
        ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
Satır-6 │    B    │    G    │    E    │    Ş    │    P    │    V    │    A    │    F    │
        └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
```

## Görev

Başlangıç noktası: **Satır-1, Sütun-1** (bu hücredeki harfi ALMA,
sadece başlangıç pozisyonun).

Nigina'nın yol tarifi:

```
Adım 1: Başlangıçtan SAĞA 3 adım git → Vardığın hücredeki harfi yaz
Adım 2: Oradan AŞAĞI 2 adım git    → Vardığın hücredeki harfi yaz
Adım 3: Oradan SOLA 1 adım git      → Vardığın hücredeki harfi yaz
Adım 4: Oradan AŞAĞI 1 adım git     → Vardığın hücredeki harfi yaz
```

4 adım = 4 harf. Birleştirdiğinde portalın anahtarını bulacaksın!

> İpucu: Başlangıç (1,1). Sağa 3 adım → (1,4). Haritada Satır-1,
> Sütun-4'te hangi harf var?

---

Cevabını `cevaplar.py` dosyasındaki `"vaka5"` anahtarına yaz.
