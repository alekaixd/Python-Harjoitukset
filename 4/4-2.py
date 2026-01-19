# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän. Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while (True):
    i = float(input("Anna tuumat: "))
    if (i < 0):
        break
    print(i * 2.54)
