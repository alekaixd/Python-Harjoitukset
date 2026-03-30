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


class Electric(Auto):
    def __init__(self, rekkari, huippuNopeus, kapasiteetti):
        super().__init__(rekkari, huippuNopeus)
        self.kapasiteetti = kapasiteetti


class Combustion(Auto):
    def __init__(self, rekkari, huippuNopeus, tankki):
        super().__init__(rekkari, huippuNopeus)
        self.tankki = tankki


def Main():
    a1 = Electric("ABC-15", 180, 52.5)
    a2 = Combustion("ACD-123", 165, 32.3)

    a1.accelerate(160)
    a2.accelerate(155)
    a1.kulje(3)
    a2.kulje(3)

    print(a1.kuljettuMatka, "km")
    print(a2.kuljettuMatka, "km")


Main()
