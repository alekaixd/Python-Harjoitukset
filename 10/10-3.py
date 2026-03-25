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


class Talo():
    def __init__(self, alinKerros, ylinKerros, hissiAmount: int):
        self.alinKerros = alinKerros
        self.ylinKerros = ylinKerros
        self.hissit = []
        self.LuoHissit(hissiAmount)  # minä kun ääkköset :D

    def LuoHissit(self, amount):
        for i in range(amount):
            self.hissit.append(Hissi(self.alinKerros, self.ylinKerros))

    def AjaHissil(self, hissiNumero, kerrosNumero):
        self.hissit[hissiNumero - 1].SiirryKerrokseen(kerrosNumero)

    def FireAlarm(self):
        print("Palohälytys")
        for i, hissi in enumerate(self.hissit):
            self.AjaHissil(i + 1, self.alinKerros)


def Main():
    t = Talo(1, 5, 2)
    t.AjaHissil(1, 3)
    t.AjaHissil(2, 4)
    t.FireAlarm()
    for i, h in enumerate(t.hissit):
        print(f"hissi {i + 1} on kerroksessa {h.nykyinenKerros}")


Main()
