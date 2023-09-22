def kwadrat(n):
    for x in range(n):
        print(x ** 2)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonaj działnie, zwróc wynik i zapamietaj gdzie skończyłeś


kwadrat(5)
kwa = kwadrat2(5)
print(type(kwa))  # <class 'generator'>

print(next(kwa))  # 0
print(next(kwa))
print(next(kwa))
print(next(kwa))  # 9
print("wypisz cokowiek")
print("zrob cokowiek")
lista = []
lista.append("12234567890")
print(next(kwa))  # 16

print(next(kwa))