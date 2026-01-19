# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []

for i in range(5):
    kaupunki = input("Syötä kaupunki: ")
    kaupungit.append(kaupunki)

# näin?
# for n in kaupungit:
#     for j in n:
#         print(j)

# vai näin?
for n in kaupungit:
    print(n)
