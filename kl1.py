# klasa - szablon wskazujacy jakie cechy i funkcje bedzie miał obiekt
# cechy - pola (zmienne)
# funkcje - funkcje
# obiekt

class Human:  # definicja klasy
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat.")


cz1 = Human()  # tworzenie obiektu
print(cz1)  # <__main__.Human object at 0x00000239F055F510>
print(type(cz1))  # <class '__main__.Human'>
print(cz1.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
cz1.imie = "Katarzyna"
cz1.wiek = 24
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
# Katarzyna
# 24
cz1.powitanie()  # Nazywam się Katarzyna

cz2 = Human()
cz2.imie = "Radek"
cz2.wiek = 28
cz2.plec = "m"
print(cz2.plec)
print(cz2.imie)
print(cz2.wiek)
cz2.powitanie()  # Nazywam się Radek
cz2.podaj_wiek()
