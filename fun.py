# funkcje - kawałek kodu, który możemy wykonac wielokrotnia

a = 6
b = 7


# definicja funkcji, tu funkcja sie nie wykonuje
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z dwoma argumentami, obowiązkowe a i b
    print(a + b)


def odejmij(a, b, c=0):  # a i b obowiązkowe do przekazania, c ma wartośc domyslna 0
    print(a - b - c)


def odejmij2(liczba1, liczba2):
    print(liczba1 - liczba2)


# wywołanie funkcji
dodaj()  # 13
dodaj2(6, 5)  # dwa argumenty a=6 i b=5
odejmij(6, 7)  # przekazywanie argumentów po kolejności
odejmij(6, 7, 8)
odejmij(b=5, c=7, a=9)  # argumnty nazwane -3
odejmij2(6, 7)
odejmij2(liczba2=10, liczba1=5)
print(dodaj())  # None - funkcja nie zwraca wyniku
# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

