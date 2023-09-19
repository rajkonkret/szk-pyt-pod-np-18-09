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
# test

zbior.remove(55)  # usuniécie bo elemencie
print(zbior)  # {33, 66, 777, 11, 44, 18, 22}

print(zbior.pop())  # usuniecie pierwszego elemntu ze zbioru, 33
print(zbior)  # {66, 777, 11, 44, 18, 22}
zbior.pop()
print(zbior)  # {777, 11, 44, 18, 22}

print(type(zbior))  # <class 'set'>

lista2 = list(zbior)
print(lista2)  # [777, 11, 44, 18, 22]

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

print(zbior | zbior2)  # suma zbiorów, {66, 999, 777, 11, 44, 18, 52, 22, 62}
print(zbior & zbior2)  # część wspólna {18, 11, 44}
print(zbior)  # {777, 11, 44, 18, 22}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}
print(zbior - zbior2)  # różnica {777, 22}
# {777, 22}
print(zbior.difference(zbior2))  # {777, 22}
print(zbior2.difference(zbior))  # {66, 52, 62, 999}
# {66, 18, 52, 999, 11, 44, 62} - {777, 11, 44, 18, 22} = {66, 52, 999, 62}
