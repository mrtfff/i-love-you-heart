import os
import random
import sys
import time

# ==============================================================================
# AYARLAR:
# ==============================================================================
BPM = 60  # Kalp Atış Hızı
YUKSEKLIK = 34  # Kalbin ana boyutu
YAZMA_HIZI = 0.07  # İlk daktilo hızı

# Tek ve Sabit Renk
KIRMIZI = "\033[91m"
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
# ADIM 1: Kelimeleri Seçen ve Hizalayan Motor
# -------------------------------------------------------------
def segmenti_parcala(genislik, rnd):
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

        secilen = rnd.choice(uygun_adaylar)
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
# ADIM 2: Belli Boyutta Bir Kalp Matrisi Üreten Fonksiyon
# -------------------------------------------------------------
def kalp_olustur(h, tuval_satir, tuval_sutun, seed):
    rnd = random.Random(seed)
    dy = 2.4 / h
    dx = dy / 2.15

    x_min, x_max = -1.4, 1.4
    adimsayisi = int((x_max - x_min) / dx)

    ham_satirlar = []
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
                parcalar = segmenti_parcala(genislik, rnd)
                satir_parcalari.extend(parcalar)
                son_idx = bitis + 1

            if adimsayisi > son_idx:
                satir_parcalari.append((" " * (adimsayisi - son_idx), False))

            ham_satirlar.append(satir_parcalari)
        y -= dy

    # Kalbi tuvalin merkezine oturt
    fark_y = tuval_satir - len(ham_satirlar)
    ust_bosluk = fark_y // 2
    alt_bosluk = fark_y - ust_bosluk

    hazir_matris = []
    for _ in range(ust_bosluk):
        hazir_matris.append([(" " * tuval_sutun, False)])

    for satir in ham_satirlar:
        mevcut_genislik = sum(len(m) for m, _ in satir)
        fark_x = tuval_sutun - mevcut_genislik
        sol_pad = fark_x // 2
        sag_pad = fark_x - sol_pad

        yeni_satir = []
        if sol_pad > 0:
            yeni_satir.append((" " * sol_pad, False))
        yeni_satir.extend(satir)
        if sag_pad > 0:
            yeni_satir.append((" " * sag_pad, False))

        hazir_matris.append(yeni_satir)

    for _ in range(alt_bosluk):
        hazir_matris.append([(" " * tuval_sutun, False)])

    return hazir_matris


# -------------------------------------------------------------
# ADIM 3: 3 Nabız Boyutu (Aynı Kelime Dizilimiyle)
# -------------------------------------------------------------
SEFER_TOHUMU = random.randint(1, 100000)

MAX_Y = YUKSEKLIK + 3
MAX_X = int(MAX_Y * 2.3)

kalp_normal = kalp_olustur(YUKSEKLIK, MAX_Y, MAX_X, SEFER_TOHUMU)
kalp_orta = kalp_olustur(YUKSEKLIK + 1, MAX_Y, MAX_X, SEFER_TOHUMU)
kalp_buyuk = kalp_olustur(YUKSEKLIK + 3, MAX_Y, MAX_X, SEFER_TOHUMU)

# -------------------------------------------------------------
# ADIM 4: Başlangıç Daktilo Animasyonu
# -------------------------------------------------------------
os.system("clear")

max_kelime_len = max(
    len(m) for satir in kalp_normal for m, k_mi in satir if k_mi
)

try:
    sys.stdout.write("\033[?25l")  # İmleci gizle

    for t in range(1, max_kelime_len + 1):
        sys.stdout.write("\033[H")
        for satir in kalp_normal:
            satir_str = ""
            for metin, k_mi in satir:
                if k_mi:
                    yazilan = metin[:t]
                    satir_str += yazilan + (" " * (len(metin) - len(yazilan)))
                else:
                    satir_str += metin
            sys.stdout.write(KIRMIZI + satir_str + SIFIRLA + "\n")
        sys.stdout.flush()
        time.sleep(YAZMA_HIZI)

    time.sleep(0.4)

    # ---------------------------------------------------------
    # ADIM 5: Tek Renkli Lub-Dub Kalp Atışı
    # ---------------------------------------------------------
    periyot = 60.0 / BPM
    t_lub = periyot * 0.14
    t_ara = periyot * 0.08
    t_dub = periyot * 0.12
    t_dinlenme = periyot * 0.66

    def ekrana_bas(matris):
        sys.stdout.write("\033[H")
        for satir in matris:
            satir_str = "".join(m for m, _ in satir)
            sys.stdout.write(KIRMIZI + satir_str + SIFIRLA + "\n")
        sys.stdout.flush()

    while True:
        # 1. LUB! (Büyük Atış)
        ekrana_bas(kalp_buyuk)
        time.sleep(t_lub)

        # 2. Ara gevşeme
        ekrana_bas(kalp_normal)
        time.sleep(t_ara)

        # 3. DUB! (Küçük Atış)
        ekrana_bas(kalp_orta)
        time.sleep(t_dub)

        # 4. Dinlenme
        ekrana_bas(kalp_normal)
        time.sleep(t_dinlenme)

finally:
    sys.stdout.write("\033[?25h")  # İmleci geri getir
    print()