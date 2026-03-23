import random


class Auto:
    def __init__(self, rekkari, huippuNopeus: int):
        self.rekisteritunnus = rekkari
        self.huippuNopeus = huippuNopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

    def accelerate(self, muutos: int):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippuNopeus:
            self.nopeus = self.huippuNopeus

    def kulje(self, aika: float):
        self.kuljettuMatka += self.nopeus * aika


def Main():
    autot = []
    for i in range(10):
        autot.append(Auto(f"ABC-{i + 1}", random.randint(100, 200)))

    ongoing = True
    while ongoing is True:
        for i, auto in enumerate(autot):
            auto.accelerate(random.randint(-10, 15))
            auto.kulje(1)
            if auto.kuljettuMatka >= 10000:
                print(f"Kilpailun voittaja on auto {i + 1}\n")
                ongoing = False
                break

    taulu(autot)


def taulu(autot):
    columnit = ["Rekisteri", "Huippunopeus", "Loppunopeus", "Kuljettu matka"]
    columnOut = ""
    for c in columnit:
        columnOut += f"| {c} "
    columnOut += "|"
    divider(columnit)
    print(columnOut)
    divider(columnit)

    for auto in autot:
        output = ""
        tiedot = [auto.rekisteritunnus, auto.huippuNopeus,
                  auto.nopeus, auto.kuljettuMatka]
        for i, t in enumerate(tiedot):
            output += "| " + str(t) + " " * (len(columnit[i]) - len(str(t))+1)
        output += "|"
        print(output)

    divider(columnit)


def divider(columnit: list):
    output = ""
    for c in columnit:
        output += "+" + "-" * (len(c) + 2)
    output += "+"
    print(output)


Main()
