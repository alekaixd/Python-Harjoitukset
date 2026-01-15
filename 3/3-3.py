"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

    Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

"""

sukupuoli = input("Syötä biologinen sukupuoli (m/n): ")
hemoglob = int(input("Syötä hemoglobiini g/l: "))

if (sukupuoli == "m"):
    if (hemoglob < 134):
        print("Hemoglobiini on alhainen")
    elif (hemoglob > 195):
        print("Hemoglobiini on korkea")
    else:
        print("hemoglobiini on normaali")

elif (sukupuoli == "n"):

    if (hemoglob < 117):
        print("Hemoglobiini on alhainen")
    elif (hemoglob > 175):
        print("Hemoglobiini on korkea")
    else:
        print("hemoglobiini on normaali")
else:
    print("error: väärä sukupuoli")  # !!!!
