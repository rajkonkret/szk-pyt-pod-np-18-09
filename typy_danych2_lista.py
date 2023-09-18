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
