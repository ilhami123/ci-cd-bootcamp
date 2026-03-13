import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cevaplar import cevaplar

# ╔══════════════════════════════════════════════════════════╗
# ║  🌀 NEXUS PORTAL SERÜVENİ — TEST DOSYASI               ║
# ║                                                          ║
# ║  ⚠️  BU DOSYAYI DEĞİŞTİRMEYİN!                         ║
# ║  📝  Sadece cevaplar.py dosyasını düzenleyin.            ║
# ║                                                          ║
# ║  Her doğru cevap, Core Crew'un mesajından bir kelime     ║
# ║  açar.                                                   ║
# ╚══════════════════════════════════════════════════════════╝


def n(s):
    """Türkçe karakterleri normalize eden yardımcı fonksiyon"""
    return (
        str(s)
        .replace("İ", "i")
        .replace("Ş", "s")
        .replace("Ç", "c")
        .replace("Ğ", "g")
        .replace("Ü", "u")
        .replace("Ö", "o")
        .lower()
        .replace("ş", "s")
        .replace("ç", "c")
        .replace("ğ", "g")
        .replace("ü", "u")
        .replace("ö", "o")
        .replace("ı", "i")
        .strip()
    )


# ─────────────────────────────────────
# 🌀 PORTAL 1 — Hoşgeldin Portalı
# ─────────────────────────────────────
class TestPortal1HosgeldinPortali:
    def test_polybius_cozuldu_mu(self):
        assert n(cevaplar["vaka1"]) == "merhaba"
        print('\n    🌀 Portal 1 açıldı! Gizli kelime: "Her"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 2 — Sayı Matrisi
# ─────────────────────────────────────
class TestPortal2SayiMatrisi:
    def test_matris_islem_cozuldu_mu(self):
        assert n(cevaplar["vaka2"]) == "alku"
        print('\n    🌀 Portal 2 açıldı! Gizli kelime: "büyük"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 3 — Makinelerin Dili
# ─────────────────────────────────────
class TestPortal3MakinelerinDili:
    def test_8bit_binary_cozuldu_mu(self):
        assert n(cevaplar["vaka3"]) == "cesaret"
        print('\n    🌀 Portal 3 açıldı! Gizli kelime: "miras"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 4 — Gizli Portal
# ─────────────────────────────────────
class TestPortal4GizliPortal:
    def test_gizli_dosya_bulundu_mu(self):
        assert n(cevaplar["vaka4"]) == "evren"
        print('\n    🌀 Portal 4 açıldı! Gizli kelime: "cesur"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 5 — Koordinat Haritası
# ─────────────────────────────────────
class TestPortal5KoordinatHaritasi:
    def test_yol_izleme_cozuldu_mu(self):
        assert n(cevaplar["vaka5"]) == "rota"
        print('\n    🌀 Portal 5 açıldı! Gizli kelime: "bir"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 6 — İrem'in Şifre Kasası
# ─────────────────────────────────────
class TestPortal6IreminSifreKasasi:
    def test_vigenere_cozuldu_mu(self):
        assert n(cevaplar["vaka6"]) == "anahtar"
        print('\n    🌀 Portal 6 açıldı! Gizli kelime: "adımla"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 7 — Şiirin Portalı
# ─────────────────────────────────────
class TestPortal7SiirinPortali:
    def test_filtreli_akrostis_cozuldu_mu(self):
        assert n(cevaplar["vaka7"]) == "labirent"
        print('\n    🌀 Portal 7 açıldı! Gizli kelime: "başlar"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 8 — Mors Sinyalleri
# ─────────────────────────────────────
class TestPortal8MorsSinyalleri:
    def test_parazitli_mors_cozuldu_mu(self):
        assert n(cevaplar["vaka8"]) == "arayis"
        print('\n    🌀 Portal 8 açıldı! Gizli kelime: "NEXUS"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 9 — Mantık Kapısı
# ─────────────────────────────────────
class TestPortal9MantikKapisi:
    def test_coklu_eleme_cozuldu_mu(self):
        assert n(cevaplar["vaka9"]) == "rehber"
        print('\n    🌀 Portal 9 açıldı! Gizli kelime: "sizinle"\n')


# ─────────────────────────────────────
# 🌀 PORTAL 10 — Son Portal
# ─────────────────────────────────────
class TestPortal10SonPortal:
    def test_meta_bulmaca_cozuldu_mu(self):
        assert n(cevaplar["vaka10"]) == "maceralar"

        print("\n")
        print("    ╔════════════════════════════════════════════════════════════╗")
        print("    ║                                                            ║")
        print("    ║   🎉 TEBRİKLER! TÜM PORTALLARI AÇTIN!                     ║")
        print("    ║                                                            ║")
        print('    ║   Core Crew\'un Gizli Mesajı:                               ║')
        print('    ║   "Her büyük miras cesur bir adımla başlar,               ║')
        print('    ║    NEXUS sizinle büyür."                                   ║')
        print("    ║                                                            ║")
        print("    ║   🌟 Core Crew'un aradığı yeni koruyucular... SİZSİNİZ!   ║")
        print("    ║                                                            ║")
        print("    ║   🚀 Pipeline yeşil! Siten deploy ediliyor...              ║")
        print("    ╚════════════════════════════════════════════════════════════╝")
        print("\n")
