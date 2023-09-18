# krotka, tupla - niezmienna
# pomaga optymalizowac pamiec
# zmienna niezmienna

tupla = 'radek'
print(type(tupla))  # <class 'str'>

tupla2 = "Tomek", 'Radek', 'Zenek', 'Marek'
tupla2a = ("Tomek", 'Radek', 'Zenek', 'Marek')
print(type(tupla2))  # <class 'tuple'>
print(type(tupla2a))  # <class 'tuple'>

tpl2 = ('radek',)
print(type(tpl2))  # <class 'tuple'>
# tupla wypełnia znamiona zmiennej
tupla3 = 43, 55, 22.34, 11, 200
print(type(tupla3))

temp = 37, 5
print(type(temp))
print(temp)  # (37, 5)

print(tupla2.count("Tomek"))
print(tupla2.index("Tomek"))
# 1
# 0

a, b = 1, 2
print(a)
print(b)
# rozpakowanie tupli

a, *b = 1, 2, 3  # * - worek na pozostałe dane
print(a)
print(b)  # [2, 3]

# "Tomek", 'Radek', 'Zenek', 'Marek'
imie1, *imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)
# Tomek
# ['Radek', 'Zenek']
# Marek

lista = list(tupla3)
print(lista)
print(type(lista))
# [43, 55, 22.34, 11, 200]
# <class 'list'>
