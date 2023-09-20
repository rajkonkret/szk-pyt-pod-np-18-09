# lambda - skrócony zapis funkcji

def odejmij2(a, b):
    return a - b


odejmij = lambda a, b: a - b  # lambda zwraca wynik
print(odejmij(9, 7))  # 2

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
# 1230.0
# 1070.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))
print(wiek(15))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))

lista = [1, 2, 3, 4, 8, 10, 23, 50]

l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 8, 16, 20, 46, 100]

print([i * 2 for i in lista])  # [2, 4, 6, 8, 16, 20, 46, 100]


# map() - mapowanie kolekcji, zamiana elemntów wg zadanej funkcji

def zmien(x):
    return x * 2


print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 16, 20, 46, 100]
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# funkcja anonimowana zdefiniowana w miejscu wykonania
# Zastosowanie map(): [2, 4, 6, 8, 16, 20, 46, 100]

# filter() - zwraca elemnty spełniające warunek
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter(): [1, 2]
# wyfiltrowac elemnty wieksze od 8
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}")  # Zastosowanie filter(): [10, 23, 50]
# wyfiltrowac wieksze od 3, mniejsze od 20
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")  # Zastosowanie filter(): [4, 8, 10]
# x > 3 and x < 20 ->  3 < x < 20

