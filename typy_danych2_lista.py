# lista - kolekcja przechowująca dowolna ilośc danych
# przechowuje rózne typy danych w jedej kolekcji
# zachowuje kolejnosc dodawania


lista = []  # definicja pustej listy
print(lista)  # []

print(type(lista))  # <class 'list'>
print(bool(lista))  # False

lista.append("radek")
print(lista)  # ['radek']
lista.append("Maciek")
lista.append("Jaśko")
lista.append("Zenek")
lista.append("Marta")
print(lista)
# ['radek', 'Maciek', 'Jaśko', 'Zenek', 'Marta'] 0(-0, -5),1(-4),2(-3),3(-2),4(-1)
# lista jest indeksowan od 0
# ostatni element listy ma również indeks -1
# -5,-4,-3,-2,-1
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

# print(lista[10])  # IndexError: list index out of range
print(len(lista))  # 5 długosc listy, ostani indeks listy = 4

print(lista[-1])  # ostatni element listy
# wypisac ujemnymi indeksami elementy listy o nazwie lista
print(lista[-2])
print(lista[-4])
print(lista[-3])
print(lista[-5])
print(lista[-0])
# Marta
# Zenek
# Maciek
# Jaśko
# radek
print(lista[0:3])  # ['radek', 'Maciek', 'Jaśko'] od indeksu 0 do indeksu 2
print(lista[2:])  # ['Jaśko', 'Zenek', 'Marta'] 2..konca
print(lista[:3])  # ['radek', 'Maciek', 'Jaśko'] poczatek..2
print(lista[7:9])  # []
print(lista[1:3])  # ['Maciek', 'Jaśko'] od 1..2
# 14:50

# nadpisanie elemntu w liscie na indeksie
lista[2] = "Mikołaj"
print(lista)  # ['radek', 'Maciek', 'Mikołaj', 'Zenek', 'Marta']

# rosrzenie lista, wstawienie elemntu w konkretne miejsce
lista.insert(1, "Marcin")
print(lista)  # ['radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek', 'Marta']

# usuniecie elemntu po indeksie
ind = lista.index("Zenek")
element = lista.pop(ind)  # pop() usuwa elemnt o indeksie, zwraca nam element usunięty
print(lista)
print(element)
# ['radek', 'Marcin', 'Maciek', 'Mikołaj', 'Marta']
# Zenek

# usuniecie po elemencie
lista.remove("Maciek")
print(lista)  # ['radek', 'Marcin', 'Mikołaj', 'Marta']

# lista.remove("Tadek") ValueError: list.remove(x): x not in list

lista.append('radek')
print(lista)  # ['radek', 'Marcin', 'Mikołaj', 'Marta', 'radek']
lista.remove('radek')
print(lista)  # ['Marcin', 'Mikołaj', 'Marta', 'radek']
# usunie pierwsze wystąpienie elemntu
# lista.remove("Radek")  # ValueError: list.remove(x): x not in list

a = 1
b = 3
a = b
print(b)  # 3
a = 7
print(b)  # 3

lista2 = lista  # kopiowanie referencji (tylko adresu pmięci)
print(lista2)
print(lista)
# ['Marcin', 'Mikołaj', 'Marta', 'radek']
# ['Marcin', 'Mikołaj', 'Marta', 'radek']
lista3 = lista.copy()  # prawidłowa kopia elemntow listy
lista.clear()  # usun wszystkie elementy
print(lista2)  # []
print(lista3)  # ['Marcin', 'Mikołaj', 'Marta', 'radek']

# liczby = [54, 999, 34, 22, 13.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
liczby = [54, 999, 34, 22, 13.34, 687]
print(liczby)  # [54, 999, 34, 22, 13.34, 687]
print(type(liczby))  # <class 'list'>
liczby.sort()
print(liczby)  # [13.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola']
lista_osoby.sort()  # sortuje
print(lista_osoby)  # ['ola', 'radek']
lista_osoby.sort(reverse=True)  # posortował i odwrócił kolejnośc
print(lista_osoby)  # ['radek', 'ola']
lista_osoby.reverse()  # tylko odwraca kolejność
print(lista_osoby)

liczby[3] = 6666
print(liczby)  # [13.34, 22, 34, 6666, 687, 999]
#                   -6    -5  -4  -3    -2    -1
print(liczby[0:3])
print(liczby[-2])
print(liczby[0:-2])  # [13.34, 22, 34, 6666] 0, -2(4) -> 0:4 czyli od 0 do 3, zawsze w prawo
print(liczby[-3:0])  # []
print(liczby[-3:])  # [6666, 687, 999] od -3 do końca

liczby.remove(34)
print(liczby)  # [13.34, 22, 6666, 687, 999]
print(liczby.pop(3))  # 687
print(len(liczby))  # 4

tekst = "Python"
lista_1 = list(tekst)  # rozpakowanie sekwencji
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n']

lista_2 = [tekst]  # stworzenie listy o elemncie podanym w zmiennej
print(lista_2)  # ['Python']

print(lista_1 + lista_2)  # ['P', 'y', 't', 'h', 'o', 'n', 'Python']

krotka = tuple(liczby)  # krotka, tupla
print(krotka)  # (13.34, 22, 6666, 999)
