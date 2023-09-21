# klasa abstrakcyjna - klasa z której nie mozna stworzyc obiektu
# metoda abstrakcyjna - nie ma funkcji, obowiązkowo trzeba nadpisac ją w kalsach dziedziczących
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda stała sie abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokokokokoko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać.")


class Orzel(Ptak):
    def wydaj_odglos(self):
        print("piiiiiiiiiiii")

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    klasa Sowa
    """

    def wydaj_odglos(self):
        print("huu hu huu hu hu")


# gdy oznaczymy kalse jako abstrakcyjna
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# orz1 = Ptak("Orzeł", 20)
# orz1.latam()  # Tu Orzeł lecę z szybkością 20
#
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.wydaj_odglos()  # kokokokokokoko
kur2.dziobanie()  # Tu Kura Idę sobie podziobać.

orz2 = Orzel("Orzel", 25)
orz2.latam()
orz2.wydaj_odglos()
orz2.poluj()  # Tu Orzel Rozpoczynam polowanie


sow = Sowa("Sowa", 10)
# TypeError: Can't instantiate abstract class Sowa with abstract method wydaj_odglos
# musimy w Sowa nadpisac metode wydaj_odglos
sow.wydaj_odglos()