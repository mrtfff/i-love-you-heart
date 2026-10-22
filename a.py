diller = [
    "Seni seviyorum",  
    "I love you",  
    "Te amo",  
    "Je t'aime",  
    "Ich liebe dich",  # Almanca
    "Ti amo",  
    "Eu te amo",  # Portekizce
    "Ik hou van jou",  # Flemenkçe
    "Aishiteru",  # Japonca (Latin harfleriyle)
    "Saranghae",  # Korece (Latin harfleriyle)
]

# Kelimeleri aralarına birer boşluk koyarak devasa tek bir metin şeridi yapıyoruz
metin = " ".join(diller) + " "
metin_uzunlugu = len(metin)

# 2. Kalbi Çizdireceğimiz Koordinat Sistemi
# Y ekseni: Kalbin tepesinden (1.3) ucuna (-1.1) doğru yukarıdan aşağı iner
# X ekseni: Kalbin solundan (-1.2) sağına (1.2) doğru soldan sağa gider

char_index = 0  # Metnimizdeki hangi harfte olduğumuzu tutan sayaç

for y in range(14, -12, -1):
    satir = ""
    Y = y * 0.1  # Y eksenini matematiksel ölçeğe çeviriyoruz

    for x in range(-30, 31):
        X = x * 0.04  # X eksenini matematiksel ölçeğe çeviriyoruz

        # Meşhur Kalp Formülü: (x² + y² - 1)³ - x² * y³ <= 0
        formul = (X**2 + Y**2 - 1) ** 3 - (X**2) * (Y**3)

        if formul <= 0:
            # Nokta kalbin İÇİNDEYSE: Sıradaki harfi al ve sayacı 1 ilerlet
            satir += metin[char_index % metin_uzunlugu]
            char_index += 1
        else:
            # Nokta kalbin DIŞINDAYSA: Boşluk bas
            satir += " "

    print(satir)