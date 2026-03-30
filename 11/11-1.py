class Julkaisu():
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivut):
        self.kirjailija = kirjailija
        self.sivut = sivut
        super().__init__(nimi)

    def TulostaTiedot(self):
        print(f"Kirja: {self.nimi}\nKirjailija: {
              self.kirjailija}\nSivumäärä: {self.sivut}\n")


class Lehti(Julkaisu):
    def __init__(self, nimi, mainToimittaja):
        self.mainToimittaja = mainToimittaja
        super().__init__(nimi)

    def TulostaTiedot(self):
        print(f"Lehti: {self.nimi}\nPäätoimittaja: {
              self.mainToimittaja}\n")


def Main():
    akuAnkka = Lehti("Aku Ankka", "Aki Hyyppä")
    hno6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    akuAnkka.TulostaTiedot()
    hno6.TulostaTiedot()


Main()
