"""
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

    LUX on parvekkeellinen hytti yläkannella.
    A on ikkunallinen hytti autokannen yläpuolella.
    B on ikkunaton hytti autokannen yläpuolella.
    C on ikkunaton hytti autokannen alapuolella.

Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
"""

lippu = input("Mikä hyttiluokka? ").lower()

if (lippu == "lux"):
    print("LUX on parvekkeellinen hytti yläkannella.")
elif (lippu == "a"):
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif (lippu == "b"):
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif (lippu == "c"):
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
