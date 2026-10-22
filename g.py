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
import os
import sys
import time

# ==============================================================================
# AYARLAR & LİSTE
# ==============================================================================
YUKSEKLIK = 36  # Kalp boyutu
YAZMA_HIZI = 0.1  # Daktilo harf hızı (0.05 hızlı, 0.1 yavaş)

# ANSI Kırmızı ve Sıfırlama Kodları
KIRMIZI = "\033[91m"
SIFIRLA = "\033[0m"

# BURAYA KENDİ BULDUĞUN UZUN LİSTEYİ YAPIŞTIRABİLİRSİN:


kelime_idx = 0


# -------------------------------------------------------------
# ADIM 1: Segmentleri Parçalara (Tokens) Ayıran Fonksiyon
# -------------------------------------------------------------
def segmenti_parcala(genislik):
    """Metni birleşik string yapmak yerine [(metin, kelime_mi)] listesi döner"""
    global kelime_idx

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
        bulundu = False
        for i in range(len(diller)):
            aday_idx = (kelime_idx + i) % len(diller)
            aday = diller[aday_idx]
            gerekli = len(aday) + (1 if secilenler else 0)

            if gerekli <= kalan_alan:
                secilenler.append(aday)
                kalan_alan -= gerekli
                kelime_idx = aday_idx + 1
                bulundu = True
                break
        if not bulundu:
            break

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
        parcalar.append((secilenler[i], True))  # Bu bir kelime, harf harf yazılacak
        bosluk_miktari = taban_bosluk + (1 if i < ekstra else 0)
        parcalar.append((" " * bosluk_miktari, False))  # Bu sabit boşluk
    parcalar.append((secilenler[-1], True))

    return parcalar


# -------------------------------------------------------------
# ADIM 2: Kalp Haritasını Parçalar Halinde Çıkarıyoruz
# -------------------------------------------------------------
dy = 2.4 / YUKSEKLIK
dx = dy / 2.15

x_min, x_max = -1.4, 1.4
adimsayisi = int((x_max - x_min) / dx)

kalp_haritasi = []  # Her satırın parçalarını tutacak
max_kelime_uzunlugu = 0

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
        satir_parcalari = []
        son_idx = 0
        for baslangic, bitis in segmentler:
            if baslangic > son_idx:
                satir_parcalari.append((" " * (baslangic - son_idx), False))

            genislik = bitis - baslangic + 1
            parcalar = segmenti_parcala(genislik)
            satir_parcalari.extend(parcalar)

            # En uzun kelimeyi buluyoruz ki animasyonun kaç adım süreceğini bilelim
            for metin, kelime_mi in parcalar:
                if kelime_mi and len(metin) > max_kelime_uzunlugu:
                    max_kelime_uzunlugu = len(metin)

            son_idx = bitis + 1

        if adimsayisi > son_idx:
            satir_parcalari.append((" " * (adimsayisi - son_idx), False))

        kalp_haritasi.append(satir_parcalari)

    y -= dy

# -------------------------------------------------------------
# ADIM 3: Eşzamanlı (Simültane) Daktilo Animasyonu
# -------------------------------------------------------------
os.system("clear")

try:
    sys.stdout.write("\033[?25l")  # İmleci gizle

    # Harf harf (1. harf, 2. harf...) bütün kelimeleri aynı anda ilerletiyoruz
    for harf_sayisi in range(1, max_kelime_uzunlugu + 1):
        sys.stdout.write("\033[H")  # Ekranın en sol üstüne git

        for satir in kalp_haritasi:
            satir_metni = ""
            for metin, kelime_mi in satir:
                if kelime_mi:
                    # O ana kadar yazılan harfler
                    yazilan = metin[:harf_sayisi]
                    # Şekil bozulmasın diye henüz yazılmayanların yerine konan hayalet boşluklar
                    bosluk = " " * (len(metin) - len(yazilan))
                    satir_metni += yazilan + bosluk
                else:
                    satir_metni += metin

            # Kırmızı renkle ekrana çizdir
            sys.stdout.write(KIRMIZI + satir_metni + SIFIRLA + "\n")

        sys.stdout.flush()
        time.sleep(YAZMA_HIZI)

finally:
    sys.stdout.write("\033[?25h")  # İmleci geri getir
    print()