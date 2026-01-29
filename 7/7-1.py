# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenAjat = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausi = int(input("Syötä kuukausi (1 - 12): "))

if kuukausi > 12 or kuukausi < 1:
    print("Väärä syötä")
elif kuukausi >= 12 or kuukausi <= 2:
    print(vuodenAjat[0])
elif kuukausi >= 9:
    print(vuodenAjat[3])
elif kuukausi >= 6:
    print(vuodenAjat[2])
else:
    print(vuodenAjat[1])


# en ihan tajunnut että minkälaisen rakenteen tehtävä halusi että teen
