import os
import random
import sys
import time

# ==============================================================================
# 💖 KİŞİSELLEŞTİRME AYARI:
# ==============================================================================
ISIM = "NEHİR"  # <-- Buraya istediğin ismi yazabilirsin

YUKSEKLIK = 36  # Kalbin genel boyutu
YAZMA_HIZI = 0.08  # Daktilo harf hızı

KIRMIZI = "\033[91m"  # Kalbin ve dillerin rengi
ALTIN = "\033[38;2;255;215;0m"  # İsmin altın rengi
SIFIRLA = "\033[0m"


# BURAYA KENDİ LİSTENİ EKLERSİN:
diller = [
    "Seni seviyorum",
    "I love you",
    "Ich liebe dich",
    "Te amo",
    "Je t'aime",
    "Ti amo",
    "Ik hou van jou",
    "Eu te amo",
    "Aishiteru",
    "Saranghae",
    "Wo ai ni",
    "Ngo oi nei",
    "Chan rak khun",
    "Anh yeu em",
    "Aku cinta kamu",
    "Saya cintakan awak",
    "Mahal kita",
    "Chit-te",
    "Bong srolanh oun",
    "Khoi huk jao",
    "Bi chamd khairtai",
    "Main tumse pyaar karta hoon",
    "Mujhe tumse mohabbat hai",
    "Ami tomake bhalobashi",
    "Naan unnai kaadhalikiren",
    "Nenu ninnu premistunnanu",
    "Njan ninne snehikkunnu",
    "Naanu ninnannu preethisuttene",
    "Mi tuzyavar prem karto",
    "Hu tane prem karu chu",
    "Main tainu pyar karda haan",
    "Ma timilai maya garchu",
    "Mama oyata adarei",
    "Uhibbuka",
    "Dooset daram",
    "Ani ohev otach",
    "Men seni sevaman",
    "Men seni zhaqsy koremin",
    "Men seni suyom",
    "Men seni soyyarin",
    "Man turo dust medoram",
    "Min sine yaratam",
    "Mən səni sevirəm",
    "Ya tebya lyublyu",
    "Ya tebe kokhayu",
    "Ya tsyabe kakhayu",
    "Kocham cie",
    "Miluji te",
    "Lubim ta",
    "Szeretlek",
    "Te iubesc",
    "Obicham te",
    "Volim te",
    "Ljubim te",
    "Te sakam",
    "Te dua",
    "S'agapo",
    "Me shen mikvarkhar",
    "Yes kez sirum em",
    "Jag alskar dig",
    "Jeg elsker deg",
    "Jeg elsker dig",
    "Eg elski teg",
    "Eg elska thig",
    "Mina rakastan sinua",
    "Ma armastan sind",
    "Es tevi milu",
    "As tave myliu",
    "T'estimo",
    "Querote",
    "Maite zaitut",
    "Inhobbok",
    "Ta gra agam duit",
    "Tha gaol agam ort",
    "Rwy'n dy garu di",
    "Ech hunn dech gaer",
    "Ek is lief vir jou",
    "Ik hou van je",
    "Te quiero",
    "Ti voglio bene",
    "Nakupenda",
    "Ngiyakuthanda",
    "Ndiyakuthanda",
    "Mo nife re",
    "Ahuru m gi n'anya",
    "Ina son ka",
    "Afekrishalehu",
    "Waan ku jeclahay",
    "Aloha au ia oe",
    "Aroha ahau ki a koe",
    "Ua alofa a'u ia te oe",
    "Au domoni iko",
    "Ua here vau ia oe",
    "Munani",
    "Rohayhu",
    "Mwen renmen w",
    "Ikh hob dikh lib",
    "Mi amas vin",
    "<3",
]



# -------------------------------------------------------------
# 3 SATIRLIK NET VE OKUNAKLI BLOK FONT (Tüm Hatalar Giderildi)
# -------------------------------------------------------------
FONT_BLOK = {
    "A": ("▄▀█", "█▀█", "█ █"),
    "B": ("█▀▄", "█▀▄", "█▄▀"),
    "C": ("█▀▀", "█  ", "█▄▄"),
    "Ç": ("█▀▀", "█  ", "█▄▄"),
    "D": ("█▀▄", "█ █", "█▄▀"),
    "E": ("█▀▀", "█▀▀", "█▄▄"),  # <-- Artık 3 çizgisi de belirgin bir E!
    "F": ("█▀▀", "█▀▀", "█  "),
    "G": ("█▀▀", "█ █", "█▄█"),
    "Ğ": ("█▀▀", "█ █", "█▄█"),
    "H": ("█ █", "█▀█", "█ █"),
    "I": (" █ ", " █ ", " █ "),
    "İ": (" █ ", " █ ", " █ "),
    "J": ("  █", "  █", "█▄█"),
    "K": ("█▄▀", "█▀▄", "█ █"),
    "L": ("█  ", "█  ", "█▄▄"),
    "M": ("█▄█", "█ █", "█ █"),
    "N": ("█▀█", "█ █", "█ █"),
    "O": ("█▀█", "█ █", "█▄█"),
    "Ö": ("█▀█", "█ █", "█▄█"),
    "P": ("█▀█", "█▀▀", "█  "),
    "R": ("█▀█", "█▀▄", "█ █"),
    "S": ("█▀▀", "▀▀█", "█▄▄"),
    "Ş": ("█▀▀", "▀▀█", "█▄▄"),
    "T": ("▀█▀", " █ ", " █ "),
    "U": ("█ █", "█ █", "█▄█"),
    "Ü": ("█ █", "█ █", "█▄█"),
    "V": ("█ █", "█ █", " █ "),
    "Y": ("█ █", " █ ", " █ "),
    "Z": ("▀▀█", " █ ", "█▄▄"),
    "W": ("█ █", "█ █", "█▄█"),
    "X": ("▀▄▀", " █ ", "▀▄▀"),
    "Q": ("█▀█", "█ █", "█▄▀"),
    " ": ("  ", "  ", "  "),
}


def buyuk_isim_uret(isim):
    """Verilen ismi 3 satırlık dev blok harflere dönüştürür"""
    ust = ""
    orta = ""
    alt = ""
    for ch in isim.upper():
        if ch in FONT_BLOK:
            u, m, a = FONT_BLOK[ch]
            ust += u + " "
            orta += m + " "
            alt += a + " "
        else:
            ust += ch + " "
            orta += ch + " "
            alt += ch + " "
    return ust.strip(), orta.strip(), alt.strip()


# -------------------------------------------------------------
# ADIM 1: Kelimeleri Seçen ve Hizalayan Motor
# -------------------------------------------------------------
def segmenti_parcala(genislik):
    if genislik <= 0:
        return []
    if genislik == 1:
        return [("♥", True)]
    if genislik == 2:
        return [("<3", True)]
    if genislik == 3:
        return [("♥ ♥", True)]

    secilenler = []
    kalan_alan = genislik

    while True:
        uygun_adaylar = [
            d
            for d in diller
            if d not in secilenler
            and (len(d) + (1 if secilenler else 0)) <= kalan_alan
        ]
        if not uygun_adaylar:
            uygun_adaylar = [
                d
                for d in diller
                if (len(d) + (1 if secilenler else 0)) <= kalan_alan
            ]
        if not uygun_adaylar:
            break

        secilen = random.choice(uygun_adaylar)
        gerekli = len(secilen) + (1 if secilenler else 0)
        secilenler.append(secilen)
        kalan_alan -= gerekli

    if not secilenler:
        return [("<3".center(genislik), True)]

    harf_toplami = sum(len(k) for k in secilenler)
    toplam_bosluk = genislik - harf_toplami

    if len(secilenler) == 1:
        sol = toplam_bosluk // 2
        sag = toplam_bosluk - sol
        return [(" " * sol, False), (secilenler[0], True), (" " * sag, False)]

    bosluk_araliklari = len(secilenler) - 1
    taban_bosluk = toplam_bosluk // bosluk_araliklari
    ekstra = toplam_bosluk % bosluk_araliklari

    parcalar = []
    for i in range(bosluk_araliklari):
        parcalar.append((secilenler[i], True))
        bosluk_miktari = taban_bosluk + (1 if i < ekstra else 0)
        parcalar.append((" " * bosluk_miktari, False))
    parcalar.append((secilenler[-1], True))

    return parcalar


# -------------------------------------------------------------
# ADIM 2: Kalp Haritasını Çıkar ve İsmi 3 Satır Olarak Merkeze Koy
# -------------------------------------------------------------
dy = 2.4 / YUKSEKLIK
dx = dy / 2.15

x_min, x_max = -1.4, 1.4
adimsayisi = int((x_max - x_min) / dx)

ham_satir_koordinatlari = []
y = 1.3
while y >= -1.05:
    Y = y
    segmentler = []
    icerde = False
    basla = 0

    for i in range(adimsayisi):
        X = x_min + i * dx
        formul = (X**2 + Y**2 - 1) ** 3 - (X**2) * (Y**3)
        if formul <= 0:
            if not icerde:
                basla = i
                icerde = True
        else:
            if icerde:
                segmentler.append((basla, i - 1))
                icerde = False
    if icerde:
        segmentler.append((basla, adimsayisi - 1))

    if segmentler:
        ham_satir_koordinatlari.append(segmentler)
    y -= dy

toplam_satir = len(ham_satir_koordinatlari)
merkez_satir_1 = int(toplam_satir * 0.38)
merkez_satir_2 = merkez_satir_1 + 1
merkez_satir_3 = merkez_satir_1 + 2

isim_ust, isim_orta, isim_alt = buyuk_isim_uret(ISIM)

kalp_haritasi = []
max_kelime_uzunlugu = 0

for s_idx, segmentler in enumerate(ham_satir_koordinatlari):
    satir_parcalari = []
    son_idx = 0

    # Tam merkeze 3 satırlık dev ismi oturtuyoruz
    if (
        s_idx in (merkez_satir_1, merkez_satir_2, merkez_satir_3)
        and len(segmentler) == 1
    ):
        baslangic, bitis = segmentler[0]
        genislik = bitis - baslangic + 1

        if baslangic > son_idx:
            satir_parcalari.append((" " * (baslangic - son_idx), False))

        if s_idx == merkez_satir_1:
            bu_isim_satiri = isim_ust
        elif s_idx == merkez_satir_2:
            bu_isim_satiri = isim_orta
        else:
            bu_isim_satiri = isim_alt

        isim_blok = "  " + bu_isim_satiri + "  "
        blok_len = len(isim_blok)

        if genislik > blok_len + 10:
            sol_kalan = (genislik - blok_len) // 2
            sag_kalan = genislik - blok_len - sol_kalan

            satir_parcalari.extend(segmenti_parcala(sol_kalan))
            satir_parcalari.append((isim_blok, "isim"))
            satir_parcalari.extend(segmenti_parcala(sag_kalan))
        else:
            satir_parcalari.append((bu_isim_satiri.center(genislik), "isim"))

        son_idx = bitis + 1

    else:
        for baslangic, bitis in segmentler:
            if baslangic > son_idx:
                satir_parcalari.append((" " * (baslangic - son_idx), False))
            genislik = bitis - baslangic + 1
            parcalar = segmenti_parcala(genislik)
            satir_parcalari.extend(parcalar)
            son_idx = bitis + 1

    if adimsayisi > son_idx:
        satir_parcalari.append((" " * (adimsayisi - son_idx), False))

    for metin, k_mi in satir_parcalari:
        if k_mi and len(metin) > max_kelime_uzunlugu:
            max_kelime_uzunlugu = len(metin)

    kalp_haritasi.append(satir_parcalari)

# -------------------------------------------------------------
# ADIM 3: Eşzamanlı Daktilo Animasyonu
# -------------------------------------------------------------
os.system("clear")

try:
    sys.stdout.write("\033[?25l")

    for harf_sayisi in range(1, max_kelime_uzunlugu + 1):
        sys.stdout.write("\033[H")

        for satir in kalp_haritasi:
            satir_metni = ""
            for metin, tip in satir:
                if tip:
                    yazilan = metin[:harf_sayisi]
                    bosluk = " " * (len(metin) - len(yazilan))

                    # İsimse ALTIN, değilse KIRMIZI renk seç
                    renk = ALTIN if tip == "isim" else KIRMIZI
                    satir_metni += renk + yazilan + bosluk + SIFIRLA
                else:
                    satir_metni += metin

            sys.stdout.write(satir_metni + "\n")
        sys.stdout.flush()
        time.sleep(YAZMA_HIZI)

finally:
    sys.stdout.write("\033[?25h")
    print()