# słownik - {klucz:wartosc}
# typ dnaych para: klucz - wartosc
# klucze nie mogą sie powtarzać
# hrejterzy
# {"name":"Radek"}
# {"klucz" : "wartość"}

dictionary = {}  # pusty słownik
print(dictionary)  # {}

dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())

# dict_values(['Radek', 39])
# dict_keys(['imie', 'wiek'])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

dictionary.update({'date': '12-12-2023'})
print(dictionary)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dictionary1 = {'x': 2}
dictionary1.update([('y', 3), ('z', 0)])
print(dictionary1)  # {'imie': 'Radek', 'wiek': 39, 'date': '12-12-2023'}

dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['imie'])  # name

# wypisac słowa jakie mamy w słowniku (polskie)
# pobrac od uzytkownika słowo do przetłuamczenia
# wypisac tłumaczenie
print(dict2.keys())
key = input("Podaj słówko do przetłumaczenia")  # odczytaj np.:  z klawitury, zawsze zwraca str
print(dict2[key.lower().replace(" ", "")])  # cat

# kalkulator
# pobrac dwie liczby
# wypisac wynik

# input zwraca stringa
# jezeli robimy oblicznie musimy zaminic na liczby za pomocą int(), float()
a = float(input("Podaj pierwszą liczbę"))
b = input("Podaj drugą liczbę")
print(a + int(b))
# 11:25
