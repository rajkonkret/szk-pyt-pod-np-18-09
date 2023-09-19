# set, zbiór - przechowuje niepowtarzające sie elementy
# tracimy kolejność przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # rzutowanie listy na zbiór
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

zb2 = set()  # tworzenie pustego zbioru
print(zb2)  # set() - pusty zbiór

zbior.add(33)  # add() - dodanie elemntu do zbioru
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}
