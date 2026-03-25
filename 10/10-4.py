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


class Kilpailu:
    def __init__(self, nimi: str, pituus: int, osallistujat: list):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def TuntiKuluu(self):
        for auto in self.osallistujat:
            auto.accelerate(random.randint(-10, 15))
            auto.kulje(1)

    def TulostaTilanne(self):
        taulu(self.osallistujat)

    def KilpailuOhi(self):
        for o in self.osallistujat:
            if o.kuljettuMatka >= self.pituus:
                print(f"Kilpailun voittaja on {o.rekisteritunnus}\n")
                self.TulostaTilanne()
                return True
        return False


def Main():
    autot = []
    for i in range(10):
        autot.append(Auto(f"ABC-{i + 1}", random.randint(100, 200)))

    kisa = Kilpailu("Suuri Romuralli", 8000, autot)

    i = 0
    while True:
        kisa.TuntiKuluu()
        if kisa.KilpailuOhi() is True:
            break
        i += 1
        if i == 10:
            kisa.TulostaTilanne()
            i = 0


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
    print()


def divider(columnit: list):
    output = ""
    for c in columnit:
        output += "+" + "-" * (len(c) + 2)
    output += "+"
    print(output)


Main()
