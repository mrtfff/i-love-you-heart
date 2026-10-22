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
        # Kalbin solundaki dış boşluk
        satir += " " * (baslangic - son_x)
        # Kalbin içi
        genislik = bitis - baslangic + 1
        satir += satiri_doldur(genislik)
        son_x = bitis + 1

    print(satir)