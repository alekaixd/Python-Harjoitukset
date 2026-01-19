# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random


def noppa(tahkot: int):
    rand = random.randint(1, tahkot)
    print(rand)
    return rand


d = int(input("Monta tahkoa nopassa? "))

while True:
    if (noppa(d) == d):
        break
