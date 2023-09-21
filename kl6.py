class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Kierownik(Pracownik):
    """
    kierownik
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 4000)
pracownik.przedstaw_sie()
wyn_pac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika: {pracownik.imie} {pracownik.nazwisko}: wynagrodzenie {wyn_pac}")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika: Jan Kowalski: wynagrodzenie 4000

kierownik = Kierownik("Anna", "Nowak", 6000, 2000)
kierownik.przedstaw_sie()
wyn_kier = kierownik.oblicz_pensje()
print(f"Wynagrodzenie dla kierownika: {kierownik.imie} {kierownik.nazwisko}: wynagrodzenie {wyn_pac}")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika: Jan Kowalski: wynagrodzenie 4000
# Cześć, jestem Anna Nowak
# Wynagrodzenie dla kierownika: Anna Nowak: wynagrodzenie 4000