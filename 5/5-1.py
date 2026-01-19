# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

i = int(input("Arpakuutioiden lukumäärä: "))
luvut = []

for n in range(i):
    luku = random.randint(1, 6)
    # print(luku)
    luvut.append(luku)

print(sum(luvut))
