class Dom:
    """
    klasa opisująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):  # __init__ konstruktor
        # uzupełnic konstruktor
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    # stworzyc metody mam_kolor, mam_metraz, mam_liczba_okien
    def mam_kolor(self):
        print(f"Mam kolor {self.__kolor}")

    def mam_metraz(self):
        print(f"Mam metraż {self.__metraz}")

    def mam_liczba_okien(self):
        print(f"Mam okien {self.__liczba_okien}")

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraż"))  # str -> int - rzutowanie na int
        self.__metraz = wybor
        self.mam_metraz()

    # dodac metody zmien_kolor, zmien_okna
    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")  # str
        self.__kolor = wybor
        self.mam_kolor()
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj ilosc okien"))  # str -> int - rzutowanie na int
        self.__liczba_okien = wybor
        self.mam_liczba_okien()

    def __farba(self):
        print("Skońćzyła się farba")


dom1 = Dom(150, "biały", 15)
dom1.mam_kolor()  # Mam kolor biały
dom1.zmien_metraz()
dom1.zmien_okna()
dom1.zmien_kolor()
# Podaj nowy metraż456
# Mam metraż 456
# Podaj ilosc okien67
# Mam okien 67
# Podaj nowy kolorzielony
# Mam kolor zielony
# Skońćzyła się farba
