class Hissi():
    def __init__(self, alin: int, ylin: int):
        self.alinKerros = alin
        self.ylinKerros = ylin
        self.nykyinenKerros = alin

    def SiirryKerrokseen(self, kerros: int):
        if kerros not in range(self.alinKerros, self.ylinKerros + 1):
            print(f"Kerros {kerros} on hissin ulkopuolella.")
            return

        while self.nykyinenKerros != kerros:
            if self.nykyinenKerros < kerros:
                self.MoveUp()
            elif self.nykyinenKerros > kerros:
                self.MoveDown()
        return

    def MoveUp(self):
        self.nykyinenKerros += 1
        print(f"Liikutaan ylös kerrokseen {self.nykyinenKerros}")
        return

    def MoveDown(self):
        self.nykyinenKerros -= 1
        print(f"Liikutaan alas kerrokseen {self.nykyinenKerros}")
        return


def Main():
    h = Hissi(1, 5)
    h.SiirryKerrokseen(5)
    h.SiirryKerrokseen(1)


Main()
