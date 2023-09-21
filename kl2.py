class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'):  # tzw konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec
        self.wzrost = wzrost

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat.")

    def moj_wzrost(self):
        print(f"Mam {self.wzrost} cm")

    def ruszaj(self):
        if self.plec == 'm':
            print("Ruszyłem w drogę")
        else:
            print("Rusyłam w drogę")


cz1 = Human("Katarzyna", 24, 198)  # tworzymy obiekt klasy Human z zadanymi cechami
print(cz1.wiek)  # odczyt cech
print(cz1.imie)
print(cz1.plec)
# 24
# Katarzyna
# k
cz1.powitanie()  # uruchomienie funkcji na obiekcie
cz1.podaj_wiek()
cz1.moj_wzrost()  # Mam 198 cm
cz1.ruszaj()  # Rusyłam w drogę

cz2 = Human("Marek", 56, 178, "m")
cz2.powitanie()  # Nazywam się Marek
cz2.ruszaj()  # Ruszyłem w drogę
