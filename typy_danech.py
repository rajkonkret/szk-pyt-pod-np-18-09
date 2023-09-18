wiek = 47
rok = 2023
temp = 36.6
wiek2 = 37.5

print(wiek)
print(type(wiek))  # <class 'int'>

print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek * rok)
print(wiek + rok)
print(wiek - rok)
print(wiek / rok)  # 0.023232822540781017 float
print(wiek // rok)  # 0 - część cąłkowita dzielenia
print(wiek % rok)  # 47 - reszta z dzielenia
print(5 % 2)  # 1 bo 2 * 2 = 4 - 5 = 1
print(wiek ** rok)  # potęgowanie

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# float - bład zaokrąglenia wynikajacy z zapisu tej liczby w pamieci
# jako mantysta i wykładnik z okresloną precyzją

# typ logiczny
# True, False
# prawda, fałsz
czy_znasz_pythona = False
print(czy_znasz_pythona)  # False
print(type(czy_znasz_pythona))  # <class 'bool'> typ logiczny
print(int(czy_znasz_pythona))  # int() - rzutowanie na liczbę
# 0 - False, 1 - True

x = 1
print(bool(x))  # bool() zamiana na typ logiczny, True

x = 100
print(bool(x))  # True

x = -10
print(bool(x))  # True

x = 0
print(bool(x))  # False

x = 'radek'
print(bool(x))  # True
x = ''
print(bool(x))  # False

# and - i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - operacja negacji
print(not True)  # False
print(not False)  # True
