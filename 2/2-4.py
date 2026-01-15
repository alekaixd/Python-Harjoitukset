# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

a = int(input("Anna luku 1: "))
b = int(input("Anna luku 2: "))
c = int(input("Anna luku 3: "))

sum = a + b + c
tulo = a * b * c
avg = sum / 3

print(f"sum = {sum}\ntulo = {tulo}\navg = {avg}")
