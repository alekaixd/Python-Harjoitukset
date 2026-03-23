class Auto:
    def __init__(self, rekkari, huippuNopeus):
        self.rekisteritunnus = rekkari
        self.huippuNopeus = huippuNopeus
        self.nopeus = 0
        self.kuljettuMatka = 0


def Main():
    mazdamx5 = Auto("ABC-123", "142 km/h")

    print(f"{mazdamx5.rekisteritunnus}, {mazdamx5.huippuNopeus}, {
          mazdamx5.nopeus}, {mazdamx5.kuljettuMatka}")


Main()
