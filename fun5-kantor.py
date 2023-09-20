# funkcja kantor
# usd, eur

def kantor(waluta):
    """
    Funkcja zwraca kantor przeliczajacy na wybraną walute
    waluta - moze byc eur lub usd
    :param waluta: eur, usd
    :return: funkcje preliczajaca wybraną walute
    """
    print("Uruchomienie kantoru")

    def usd(kwota):
        print(f"Wymieniam usd: {kwota} usd = {kwota * 4.35} zł")

    def eur(kwota=0):
        print(f"Wymieniam eur: {kwota} eur = {kwota * 4.67} zł")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_usd = kantor('usd')
print(kantor_usd)  # <function kantor.<locals>.usd at 0x0000020B1C098860>
kantor_usd(1000)  # Wymieniam dolary  Wymieniam usd: 1000 usd = 4350.0 zł
print(kantor.__doc__)
help(kantor)
help(print)
# funkcje usd i eur maja przyjmowac kwote
# ładnie wypisac np.: Wymieniam usd: 100 usd = 420 zł
kantor_eur = kantor('eur')
kantor_eur(3000)  # Wymieniam eur: 3000 eur = 14010.0 zł
