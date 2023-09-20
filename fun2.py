# funkcje zracające wynik

def dodaj(a, b):
    return a + b  # return - zwraca wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))  # funkcja zwróciła do głównego programy wynik 11
wyn = dodaj(5, 6)
print(wyn)
print(dodaj(5, 6) + dodaj(8, 9))  # 28

print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))  # 1070.0
print(oblicz_vat(vat=15, cena=5000))  # 5750.0

zm = oblicz_vat(1000)
print(zm)
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("Pawidłowo")  # Pawidłowo

x = 3.1485
print(f"{x:.2f}")  # 3.15
a = round(x, 2)  # 2 - liczba miejsc po przecinku
print(a)  # 3.15
print(x)  # 3.1485
