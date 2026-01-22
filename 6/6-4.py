# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(luvut: list):  # isoin haista ***** funktio
    return sum(luvut)


def main():
    lista = []
    while True:
        i = input("Syötä luku: ")
        if i == "":
            break
        lista.append(int(i))
    print(summa(lista))


main()
