# PEP8
print()  # wypisz, wydrukuj np.: na ekranie

print("Nazywam się Radek")  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# ctrl d - powiela linie w ktorej stoi kursor

# type() - wypisanie typu danych
print(type("Radek"))  # <class 'str'> - dane tekstowe (string)
# ctrl alt l  - wyrównanie kodu

print(39)
print(type(39))  # <class 'int'> integer - czyli liczby cłkowite

print("34" + "14")  # 3414 konkatenacja - łaczenie tekstów
print(34 + 14)  # 48

print(5 * "4")  # 44444

# zmienna - takie pudełko na dane
imie = "Radek"
print(type(imie))  # <class 'str'>

wiek = 48
print(wiek)
print(type(wiek))  # <class 'int'>

wiek = "Radek"
print(wiek)
print(type(wiek))  # <class 'str'>

# print(wiek + 1)  # TypeError: can only concatenate str (not "int") to str
# ctrl / - dodaje komentarz
print(wiek + str(1))  # łaczenie tekstów - zamiana liczby na tekst str(), Radek1

wiek = 48
print(int(wiek) + 1)  # 49
# int() - rzutownie na liczbe (zamiana)
# 11:30
