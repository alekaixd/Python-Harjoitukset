# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math


def LaskeHinta(halkaisija: float, hinta: float):
    r = (halkaisija/100)/2
    ala = math.pi * (r**2)
    hintaSuhde = hinta/ala
    return round(hintaSuhde, 2)


pizzat = []


def main():
    for n in range(2):
        halk = float(input(f"Syötä pizzan {n + 1} halkaisija: "))
        hint = float(input(f"Syötä pizzan {n + 1} hinta: "))

        pizzat.append((halk, hint, n + 1))

    alin = pizzat[0]
    for pizza in pizzat:
        print(f"{LaskeHinta(pizza[0], pizza[1])} €/m^2")
        if LaskeHinta(pizza[0], pizza[1]) < LaskeHinta(alin[0], alin[1]):
            alin = pizza

    print(f"Paras hintalaatusuhde oli pizzassa {alin[2]}")


main()
