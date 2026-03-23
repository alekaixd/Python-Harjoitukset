class Auto:
    def __init__(self, rekkari, huippuNopeus):
        self.rekisteritunnus = rekkari
        self.huippuNopeus = huippuNopeus
        self.nopeus = 0
        self.kuljettuMatka = 0

    def accelerate(self, muutos: int):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = "0 km/h"
        if self.nopeus > self.huippuNopeus:
            self.nopeus = f"{self.huippuNopeus} km/h"


def Main():
    mazdamx5 = Auto("ABC-123", "142 km/h")

    print(f"{mazdamx5.rekisteritunnus}, {mazdamx5.huippuNopeus}, {
          mazdamx5.nopeus}, {mazdamx5.kuljettuMatka}")


Main()
