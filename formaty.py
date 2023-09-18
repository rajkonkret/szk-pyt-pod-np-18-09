import sys

user = "Tomek"  # str
wiek = 39  # int
wersja = 3.1100001  # float liczby zmiennoprzecinkowe
liczba = 134567456234  # int

# stackoverflow
print(sys.float_info)  # 1.7976931348623157e+308
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
print(sys.int_info)
# int_infosys.int_info(bits_per_digit=30, sizeof_digit=4,
#              default_max_str_digits=4300, str_digits_check_threshold=640)

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz teraz 39 lat
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - str
# %d - digit

print("Witaj %(user)s, masz teraz %(age)d lat." % {'user': user, "age": wiek})  # Witaj Tomek, masz teraz 39 lat.

print("Witaj {} masz teraz {} lat.".format(user, wiek))  # Witaj Tomek masz teraz 39 lat.
print("Witaj {} masz teraz {} lat.".format(wiek, user))  # Witaj 39 masz teraz Tomek lat.

print(f"Witaj {user}, masz teraz {wiek} lat")  # Witaj Tomek, masz teraz 39 lat
# f - fstring - tekst sformatowany

print("Używamy wersji Pythona %i" % 3)
print("Używamy wersji Pythona %f" % 3.11)  # Używamy wersji Pythona 3.110000
print("Używamy wersji Pythona %.1f" % 3.11)  # Używamy wersji Pythona 3.1
print("Używamy wersji Pythona %.2f" % 3.11)  # Używamy wersji Pythona 3.11
print("Używamy wersji Pythona %.0f" % 3.11)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %.f" % 3.11)  # Używamy wersji Pythona 3
print("Liczba zaokrąglona %.f" % 3.9)  # Liczba zaokrąglona 4

x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("Nadal x się nie zmienił", x)
# Zero miejsc po przecinku 3
# Nadal x się nie zmienił 3.14

print(f"Używamy wersji Pythona {wersja}")
print(f"Używamy wersji Pythona {wersja:.1f}")
print(f"Używamy wersji Pythona {wersja:.0f}")
# Używamy wersji Pythona 3.1
# Używamy wersji Pythona 3
# 13:30

print(f"{user:>10}")  # "     Tomek" - uzupelniony spacjami do długosci 10, spacje z lewej
print(f'{user:>20}')  # "               Tomek"
print(f'{user:<30}')  # "Tomek                         "
print(f"{user:^10}")  # "  Tomek   " - wypośrodkowany

print(liczba)  # 134567456234 - int
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 134,567,456,234
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 134.567.456.234
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 134 567 456 234
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 134,567,456,234
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 134 567 456 234
