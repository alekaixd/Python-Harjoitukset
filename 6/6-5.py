# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def karsi(lista: list):
    newlist = []
    for n in lista:
        if n % 2 == 0:
            newlist.append(n)
    return newlist


def main():
    lista = [1, 5, 7, 4, 9, 3, 2, 13]
    print(karsi(lista))


main()
