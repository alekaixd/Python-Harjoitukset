# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

x = int(input("Anna Kanta: "))
y = int(input("Anna Korkeus: "))

piiri = 2*x + 2*y
ala = x*y

print(f"piiri = {piiri}\npinta-ala = {ala}")
