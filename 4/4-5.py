# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).

yritykset = 0

while yritykset < 5:
    usr = input("Käyttäjätunnus: ")
    passwd = input("Salasana: ")

    if (usr == "python" and passwd == "rules"):
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")
    yritykset += 1
