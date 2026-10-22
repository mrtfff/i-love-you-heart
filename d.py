diller = [
    # --- Senin listen ---
    "Seni seviyorum",          # Türkçe
    "I love you",              # İngilizce
    "Ich liebe dich",          # Almanca
    "Te amo",                  # İspanyolca
    "Je t'aime",               # Fransızca
    "Ti amo",                  # İtalyanca
    "Ik hou van jou",          # Felemenkçe
    "Eu te amo",               # Portekizce
    "Aishiteru",               # Japonca
    "Saranghae",               # Korece

    # --- Doğu ve Güneydoğu Asya ---
    "Wo ai ni",                # Çince (Mandarin)
    "Ngo oi nei",              # Kantonca
    "Chan rak khun",           # Tayca
    "Anh yeu em",              # Vietnamca
    "Aku cinta kamu",          # Endonezce
    "Saya cintakan awak",      # Malayca
    "Mahal kita",              # Filipince
    "Chit-te",                 # Birmanca
    "Bong srolanh oun",        # Kmerce
    "Khoi huk jao",            # Laoca
    "Bi chamd khairtai",       # Moğolca

    # --- Güney Asya ---
    "Main tumse pyaar karta hoon",        # Hintçe
    "Mujhe tumse mohabbat hai",           # Urduca
    "Ami tomake bhalobashi",              # Bengalce
    "Naan unnai kaadhalikiren",           # Tamilce
    "Nenu ninnu premistunnanu",           # Telugu
    "Njan ninne snehikkunnu",             # Malayalamca
    "Naanu ninnannu preethisuttene",      # Kannadaca
    "Mi tuzyavar prem karto",             # Marathice
    "Hu tane prem karu chu",              # Gujaratça
    "Main tainu pyar karda haan",         # Pencapça
    "Ma timilai maya garchu",             # Nepalce
    "Mama oyata adarei",                  # Sinhalaca

    # --- Orta Doğu ve Orta Asya ---
    "Uhibbuka",                # Arapça
    "Dooset daram",            # Farsça
    "Ani ohev otach",          # İbranice
    "Men seni sevaman",        # Özbekçe
    "Men seni zhaqsy koremin", # Kazakça
    "Men seni suyom",          # Kırgızca
    "Men seni soyyarin",       # Türkmence
    "Man turo dust medoram",   # Tacikçe
    "Min sine yaratam",        # Tatarca
    "Mən səni sevirəm",        # Azerbaycanca

    # --- Doğu Avrupa ve Balkanlar ---
    "Ya tebya lyublyu",        # Rusça
    "Ya tebe kokhayu",         # Ukraynaca
    "Ya tsyabe kakhayu",       # Belarusça
    "Kocham cie",              # Lehçe
    "Miluji te",               # Çekçe
    "Lubim ta",                # Slovakça
    "Szeretlek",               # Macarca
    "Te iubesc",               # Romence
    "Obicham te",              # Bulgarca
    "Volim te",                # Sırpça / Hırvatça / Boşnakça
    "Ljubim te",               # Slovence
    "Te sakam",                # Makedonca
    "Te dua",                  # Arnavutça
    "S'agapo",                 # Yunanca
    "Me shen mikvarkhar",      # Gürcüce
    "Yes kez sirum em",        # Ermenice

    # --- Kuzey Avrupa ve Baltıklar ---
    "Jag alskar dig",          # İsveççe
    "Jeg elsker deg",          # Norveççe
    "Jeg elsker dig",          # Danca
    "Eg elski teg",            # Faroece
    "Eg elska thig",           # İzlandaca
    "Mina rakastan sinua",     # Fince
    "Ma armastan sind",        # Estonca
    "Es tevi milu",            # Letonca
    "As tave myliu",           # Litvanca

    # --- Batı ve Güney Avrupa ---
    "T'estimo",                # Katalanca
    "Querote",                 # Galiçyaca
    "Maite zaitut",            # Baskça
    "Inhobbok",                # Maltaca
    "Ta gra agam duit",        # İrlandaca
    "Tha gaol agam ort",       # İskoç Gaelcesi
    "Rwy'n dy garu di",        # Galce
    "Ech hunn dech gaer",      # Lüksemburgca
    "Ek is lief vir jou",      # Afrikaanca
    "Ik hou van je",           # Flamanca
    "Te quiero",               # İspanyolca (günlük)
    "Ti voglio bene",          # İtalyanca (sevgi)

    # --- Afrika ---
    "Nakupenda",               # Svahili
    "Ngiyakuthanda",           # Zuluca
    "Ndiyakuthanda",           # Xhosaca
    "Mo nife re",              # Yorubaca
    "Ahuru m gi n'anya",       # Igbo
    "Ina son ka",              # Hausaca
    "Afekrishalehu",           # Amharca
    "Waan ku jeclahay",        # Somalice

    # --- Okyanusya ---
    "Aloha au ia oe",          # Hawaii dili
    "Aroha ahau ki a koe",     # Maori dili
    "Ua alofa a'u ia te oe",   # Samoa dili
    "Au domoni iko",           # Fiji dili
    "Ua here vau ia oe",       # Tahiti dili

    # --- Amerika ---
    "Munani",                  # Keçuaca
    "Rohayhu",                 # Guarani
    "Mwen renmen w",           # Haiti Kreyolu

    # --- Diğer ---
    "Ikh hob dikh lib",        # Yidiş
    "Mi amas vin",             # Esperanto
    "Te amo (Latin)",          # Latince
    "<3",                      # Evrensel :)
]

kisa_kelimeler = {4: "Love", 2: "Ai", 1: "♥"}

kelime_idx = 0


def satiri_doldur(genislik):
    """Verilen genişliğe kelimeleri ASLA BÖLMEDEN tam sığdıran fonksiyon"""
    global kelime_idx

    if genislik <= 0:
        return ""
    if genislik in kisa_kelimeler:
        return kisa_kelimeler[genislik]
    if genislik < 4:
        return "♥" * genislik

    secilenler = []
    toplam_harf = 0

    while True:
        aday = diller[kelime_idx % len(diller)]
        gerekli_alan = len(aday) + (1 if secilenler else 0)

        if toplam_harf + gerekli_alan <= genislik:
            secilenler.append(aday)
            toplam_harf += gerekli_alan
            kelime_idx += 1
        else:
            break

    if not secilenler:
        for k in sorted(diller, key=len):
            if len(k) <= genislik:
                secilenler.append(k)
                break
        if not secilenler:
            return "♥" * genislik

    harf_sayisi = sum(len(k) for k in secilenler)
    kalan_bosluk = genislik - harf_sayisi

    if len(secilenler) == 1:
        sol = kalan_bosluk // 2
        sag = kalan_bosluk - sol
        return ("♥" * sol) + secilenler[0] + ("♥" * sag)

    bosluk_araliklari = len(secilenler) - 1
    taban_bosluk = kalan_bosluk // bosluk_araliklari
    fazlalik = kalan_bosluk % bosluk_araliklari

    sonuc = ""
    for i in range(bosluk_araliklari):
        sonuc += secilenler[i]
        sonuc += " " * (taban_bosluk + (1 if i < fazlalik else 0))
    sonuc += secilenler[-1]

    return sonuc


for y in range(13, -12, -1):
    Y = y * 0.1
    satir = ""

    segmentler = []  # [(baslangic, bitis), ...]
    icerde = False
    basla = 0

    for x in range(-33, 34):
        X = x * 0.038
        formul = (X**2 + Y**2 - 1) ** 3 - (X**2) * (Y**3)

        if formul <= 0:
            if not icerde:
                basla = x
                icerde = True
        else:
            if icerde:
                segmentler.append((basla, x - 1))
                icerde = False
    if icerde:
        segmentler.append((basla, 33))

    if not segmentler:
        continue

    son_x = -33
    for baslangic, bitis in segmentler:
        satir += " " * (baslangic - son_x)
        genislik = bitis - baslangic + 1
        satir += satiri_doldur(genislik)
        son_x = bitis + 1

    print(satir)