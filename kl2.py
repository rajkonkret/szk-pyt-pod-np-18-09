class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'): # tzw konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec
        self.wzrost = wzrost

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat.")

    def moj_wzrost(self):
        print(f"Mam {self.wzrost} lat")


cz1 = Human("Katarzyna", 24, 198)
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
# 24
# Katarzyna
# k
cz1.powitanie()
cz1.podaj_wiek()
cz1.moj_wzrost()