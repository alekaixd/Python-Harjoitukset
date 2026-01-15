"""
Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:

    kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
    nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
"""
import random

lock3 = ""
lock4 = ""

x = 0
while x < 3:
    rand = random.randint(0, 9)
    lock3 += str(rand)
    x += 1


x = 0
while x < 4:
    rand = random.randint(1, 6)
    lock4 += str(rand)
    x += 1

print(lock3)
print(lock4)
