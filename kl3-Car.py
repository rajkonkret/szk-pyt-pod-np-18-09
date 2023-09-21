class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # __ - pole stalo się prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("Zmien bieg")


car1 = Car("Opel", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc)  # odczytanie pola predkosc -> 50
# po oznaczeniu pola jako prywatne dostajemy bład:
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
car1.licznik()  # Prędkość wynosi 50 km/h
# car1.__predkosc = 0  # ustawienia wartosci pola w klasie a  nie w obiekcie '_Car__predkosc' nie polecam tego robic
car1.licznik()  # Prędkość wynosi 0 km/h, po ustawieniu prywatne: Prędkość wynosi 50 km/h

car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Prędkość wynosi 0 km/h
