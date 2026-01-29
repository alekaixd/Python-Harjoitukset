# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = {}

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    if nimi not in nimet:
        nimet[nimi] = 0
        print("Uusi nimi")
    else:
        nimet[nimi] += 1
        print("Aiemmin syötetty")

for n in nimet:
    print(n)
