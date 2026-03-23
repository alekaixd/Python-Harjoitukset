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
    mazdamx5 = Auto("ABC-123", 142)
    mazdamx5.accelerate(60)
    mazdamx5.kulje(1.5)

    print(f"nopeus: {mazdamx5.nopeus} km/h")
    print(f"kuljettu matka: {mazdamx5.kuljettuMatka} km")


Main()
