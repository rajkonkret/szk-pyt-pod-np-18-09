# instrukcje warunkowe - instrukcje sterowania przepływem program
# if

# odp = True  # prawda
odp = False  # prawda
if odp:
    print("Brawo")  # obowiązkowo wciecie(4 spacje), obowiązkowo conajmniej jedna linia programu
    print("Działam w warunku, warunek", odp)
else:  # w przeciwnym przypadku
    print("Musisz uczyć się dalej", odp)

print("Działam dalej, warunek", odp)

# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:  # jeżeli
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:  # kolejny warunek, a jeżeli
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(podatek)
# # dodac podatek 20% dla zakresu 10000 do 29999
# # kolejnosc warunków w konstrukcji if elif ma znaczenie

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")  # f -string format - wartości zmiennych mogę umiescic w {}

rabat = 25 if suma_zam > 150 else 0  # po lewej to co prawda
print(f"Rabat wynosi {rabat}")  # f - string format - wartości zmiennych mogę umiescic w {}

lista_bledow = []
alert_system = 'dysk'
error = 'medium'

error_message = "Stało się coś strasznego"
if alert_system == 'console':  # porównanie
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append('email')
    if error == 'medium':
        lista_bledow.append("ostrzezenie")
    elif error == "critical":
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny")
else:
    print("System nieznany")

print(lista_bledow)

a = 14
b = 3
print(f"Wynik porównania {a} > {b}: {a > b}")
print(f"Wynik porównania {a} < {b}: {a < b}")
print(f"Wynik porównania {a} >= {b}: {a >= b}")
print(f"Wynik porównania {a} <= {b}: {a <= b}")
print(f"Wynik porównania {a} == {b}: {a == b}")  # porównanie czy a == b
print(f"Wynik porównania {a} != {b}: {a != b}")  # różne jesli różne to zwraca True
# Wynik porównania 14 > 3: True
# Wynik porównania 14 < 3: False
# Wynik porównania 14 >= 3: True
# Wynik porównania 14 <= 3: False
# Wynik porównania 14 == 3: False
# Wynik porównania 14 != 3: True

# napisac test z historii, geografii, czegokolwiek
# wyswietlic pytanie
# pobrac odpowiedz
# sprawdzic odpowiedz
# wyswietlic wynik

odp = input("Podaj datę Chrztu Polski")
if odp == '966':  # '' bo odp ma str
    print("Odpowiedź prawidłowa")
else:
    print("Masz to w książce na 23 stronie")
