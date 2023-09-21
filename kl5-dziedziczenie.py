# dziedziczenie

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczymy po kalsie Pojazd
    """
    Klasa samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)  # obowiazkowe w kontruktorze
        self.marka = marka

    def info(self):
        super().info()  # wywołanie info z klasy nadrzednej (Pojazd)
        print(f"Marka: {self.marka}")


poj = Pojazd("czerowony")
poj.info()  # Kolor: czerowony

sam = Samochod("zielony", "Fiat")
sam.info()
#
# Kolor: czerowony
# Kolor: zielony
# Marka: Fiat
