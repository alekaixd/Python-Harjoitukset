# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.


luvut = []

while (True):
    i = input("Anna luku: ")
    if (i == ""):
        break
    luvut.append(int(i))

print(f"{sorted(luvut)[0]}, {sorted(luvut)[len(luvut) - 1]}")
