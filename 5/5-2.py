# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
luvut = []

while (True):
    i = input("Syötä luku: ")
    if (i == ""):
        break
    luvut.append(int(i))
luvut.sort(reverse=True)

for n in luvut:
    print(n)
