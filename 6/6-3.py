"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

    Yksi gallona on 3,785 litraa.
"""


def litroiksi(galloona: int):
    return galloona * 3.785


def main():
    while True:
        i = int(input("Syötä bensiini gallonoina: "))
        if i < 0:
            break
        print(f"{i} galloonaa on {litroiksi(i)} litraa")


main()
