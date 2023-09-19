# petle
# for - petla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # _ niema zmienna
    pass

for i in range(10):
    print(i * 2)

# w petli for uzyc losowania liczb i zamienic boiler code na kod zminimalizowany
lista2 = list(range(1, 50))  # 1..49
for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

for i in range(10):
    if i % 2 == 0:  # % - reszta z dzielenia
        print(i, "liczba parzysta")
#
# 0 liczba parzysta
# 2 liczba parzysta
# 4 liczba parzysta
# 6 liczba parzysta
# 8 liczba parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)

print(lista3)
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1

    print(c)  # 2 -> 3

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1  2 - 1 = 1
print(a)  # 1
a *= 3  # a = a * 3
print(a)  # 3
a %= 2  # a = a % 2 (modulo - reszta z dzielenia)
print(a)  # 1
a /= 2  # a = a / 2
print(a)  # 0.5 - float

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)

# Radek
# Asia
# Zbyszek
# Marcin

# wypisac imiona z listy w takiej formie 0 Radek
for p in range(len(imiona)):  # len() długosc listy, range(4) 0..3
    print(p, imiona[p])

# 0 Radek
# 1 Asia
# 2 Zbyszek
# 3 Marcin

for p in imiona:
    print(imiona.index(p), p)

# enumerate() - zwraca ponumerowane elemnty kolekcji
for p in enumerate(imiona):
    print(p)  # (3, 'Marcin')

a, b = (0, "Radek")
print(a)
print(b)

for p, w in enumerate(imiona):
    print(p, w, end='', sep=";")
# 0;Radek1;Asia2;Zbyszek3;Marcin
# end - znak końca lini (domyslnie \n)
# sep - znak oddzielający elemnty (domyślnie spacja)
print()
# 14:12

ludzie = ['Radek', 'Zenek', "Asia", 'Marcin', 'Franek']
wiek = [47, 67, 34, 32]

# wypisac indeks, osobe i wiek
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # IndexError: list index out of range
#     # bład dla różnych długości list

# zip() - łączenie kolekcji
for k in zip(ludzie, wiek):
    print(k)  # ('Marcin', 32)

for o, w in zip(ludzie, wiek):
    print(o, w)  # Marcin 32

for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (3, ('Marcin', 32))

a, b = (3, ('Marcin', 32))
print(a)
print(b)  # ('Marcin', 32)
c, d = b
print(a, c, d)

for a, (c, d) in enumerate(zip(ludzie, wiek)):
    print(a, c, d)  # 3 Marcin 32

jezyk = ['python', 'java']
for i, (o, w, j) in enumerate(zip(imiona, wiek, jezyk)):
    print(i, o, w, j)
# 0 Radek 47 python
# 1 Asia 67 java

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)

for item in zipped_list:
    print(item)  # ('Franek', 'Nan', 'Nan')

for o, w, j in zipped_list:
    print(o, w, j)
# Radek 47 python
# Zenek 67 java
# Asia 34 Nan
# Marcin 32 Nan
# Franek Nan Nan
