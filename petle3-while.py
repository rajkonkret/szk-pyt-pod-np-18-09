# petla while
# petla sterowana warunek
# dopóki warunek True pętla się wykonuje

licznik = 0
while True:
    licznik += 1
    print("Komunikat !!!")
    if licznik > 10:
        break  # przrywa działanie pętli

print(licznik)

licznik = 0
while licznik < 11:
    print("Komunikat 2")
    licznik += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)  # str
    lista2.append(int(wej))

print(lista)  # ['5', '4', '3', '2'] lista stringów
print(lista2)  # [5, 4, 3, 2] lista intow
