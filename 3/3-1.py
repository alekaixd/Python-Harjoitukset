"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.
"""

pituus = int(input("Kuhan pituus: "))

if (pituus < 37):
    print(f"Laske kuha takaisin. Antaa sen kasvaa vielä {
          37 - pituus} senttiä.")
else:
    print("Kuha on OK!")
