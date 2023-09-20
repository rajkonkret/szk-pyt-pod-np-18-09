a = 10
b = 10


# while a < 20:
#     a += 1
#
# print(a)  # 20 tu zmieniła sie globalna a

# zmienne globalne
def dodaj():
    a = 6  # a i b są lokalne, nie wpływaja na wartości globalne o tej samej nazwie, mja zakres lokalny(scope)
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)  # tu bierze wartości globalne a i b


def dodaj3():
    global a  # do działania bedzie uzyta a globalne
    a = 6  # zostanie nadpisane globalne a
    b = 7
    print(a + b)


print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 10
dodaj()
print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 10
dodaj2()
print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 10
dodaj3()
print("Zmienna a z góry (globalna)", a)  # Zmienna a z góry (globalna) 6
