# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

airports = {}
action = " "

while action != "":
    action = input("Syötä tai hae lentokenttä (s/h): ")
    if action == "s":
        icao = input("Syötä lentokentän ICAO-koodi: ")
        nimi = input("Syötä lentokentän nimi: ")
        airports[icao] = nimi
        print(f"Lentokenttä {nimi} on tallennettu koodilla {icao}!")
    elif action == "h":
        icao = input("Hae lentokentän ICAO-koodi: ")
        if icao in airports:
            print(airports[icao])
        else:
            print("Lentokenttää ei löydetty")
