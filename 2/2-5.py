# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

leiv = float(input("Monta leiviskää? "))
naulat = float(input("Monta naulaa? "))
luodit = float(input("Monta luotia? "))

# muunnetaan leiviskät nauloiksi ja naulat luodeiksi

#    Yksi leiviskä on 20 naulaa.
#    Yksi naula on 32 luotia.
#    Yksi luoti on 13,3 grammaa.

naulat += leiv * 20
luodit += naulat * 32
total = luodit * 13.3

kilo = total // 1000
grammat = total % 1000

print(f"{round(kilo)} kilogrammaa ja {round(grammat, 3)} grammaa")
