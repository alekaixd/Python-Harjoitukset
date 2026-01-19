# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

rand = random.randint(1, 10)

while (True):
    i = int(input("Arvaa luku: "))
    if (i > rand):
        print("Luku on pienempi, arvaa uudestaan")
    elif (i < rand):
        print("Luku on suurempi, arvaa uudestaan")
    else:
        print("Arvasit oikein :D")
        break
