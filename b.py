# Terminal ekran genişliği
GENISLIK = 46

kalp = [
    ("Te amo".center(16) + " " * 6 + "Ti amo".center(16)).center(GENISLIK),
    ("Je t'aime".center(18) + " " * 2 + "Aishiteru".center(18)).center(
        GENISLIK
    ),
    ("Ich liebe dich" + "   ♥   " + "Ik hou van jou").center(GENISLIK),
    ("Seni seviyorum" + "  ♥  " + "I love you").center(GENISLIK),
    ("Eu te amo" + " ♥ " + "Ti amo").center(GENISLIK),
    "Seni seviyorum".center(GENISLIK),
    "I love you".center(GENISLIK),
    "Te amo".center(GENISLIK),
    "Love".center(GENISLIK),
    "Ai".center(GENISLIK),
    "♥".center(GENISLIK),
]

# Kalbi ekrana yazdırıyoruz
for satir in kalp:
    print(satir)