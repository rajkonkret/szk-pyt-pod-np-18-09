# napisanie aplikacji kalkulator
# uzyc petli while
# pobrac operacje, 5 - konczenie programu
# pobrac liczby
# wyswietlic wynik operacji

while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
""")
    odp = input("Podaj operację do wykonania")
    if odp == '5':
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == '1':
            print("Wynik", a + b)
        elif odp == '2':
            print("Wynik", a - b)
        elif odp == '3':
            print("Wynik", a * b)
        elif odp == '4':
            print("Wynik", a / b)
        else:
            print("Nie znam takiego działania")
    # ZeroDivisionError: float division by zero
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Bład wartości")
    except TypeError:
        print("Bład typu")
    except Exception as e:  # łapie pozostałe wyjatki
        print("Bład", e)
    else:
        print("Gdy nie ma błedu")
    finally:  # to wykonuje sie zawsze
        print("Zawsze")
# try except (else)(finally)
