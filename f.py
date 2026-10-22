import os
import sys
import time


YUKSEKLIK = 36 
HIZ = 0.1  
KIRMIZI = "\033[91m"
SIFIRLA = "\033[0m"

# Kelime Havuzumuz
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

kelime_idx = 0


def satiri_doldur(genislik):
    """Kelimeleri bölmeden ve delik bırakmadan dolduran fonksiyon"""
    global kelime_idx

    if genislik <= 0:
        return ""
    if genislik == 1:
        return "♥"
    if genislik == 2:
        return "<3"
    if genislik == 3:
        return "♥ ♥"

    secilenler = []
    kalan_alan = genislik
    sys.stdout.write("\033[31m")
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
        return "<3".center(genislik)

    harf_toplami = sum(len(k) for k in secilenler)
    toplam_bosluk = genislik - harf_toplami

    if len(secilenler) == 1:
        return secilenler[0].center(genislik)

    bosluk_araliklari = len(secilenler) - 1
    taban_bosluk = toplam_bosluk // bosluk_araliklari
    ekstra = toplam_bosluk % bosluk_araliklari

    sonuc = ""
    for i in range(bosluk_araliklari):
        sonuc += secilenler[i]
        sonuc += " " * (taban_bosluk + (1 if i < ekstra else 0))
    sonuc += secilenler[-1]

    return sonuc


#
dy = 2.4 / YUKSEKLIK
dx = dy / 2.15

x_min, x_max = -1.4, 1.4
adimsayisi = int((x_max - x_min) / dx)

kalp_matrisi = []

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
        satir = ""
        son_idx = 0
        for baslangic, bitis in segmentler:
            satir += " " * (baslangic - son_idx)
            genislik = bitis - baslangic + 1
            satir += satiri_doldur(genislik)
            son_idx = bitis + 1

        satir += " " * (adimsayisi - son_idx)
        kalp_matrisi.append(satir)

    y -= dy


os.system("clear")
toplam_sutun = adimsayisi

try:
    sys.stdout.write("\033[?25l")

    for sutun in range(1, toplam_sutun + 1):
        sys.stdout.write("\033[H")

        for satir in kalp_matrisi:
            sys.stdout.write(satir[:sutun] + "\n")

        sys.stdout.flush()
        time.sleep(HIZ)

finally:
    sys.stdout.write("\033[?25h")
    print()