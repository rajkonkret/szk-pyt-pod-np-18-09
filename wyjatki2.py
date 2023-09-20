while True:
    try:
        z = input("Podaj działanie + - * /")
        a = float(input("Podaj pierwsza liczbę"))
        b = float(input("Podaj drugą liczbę"))

        match z:
            case "+":
                print(f"Wynik dodawania {a} + {b} = {a + b}")
            case "-":
                print(f"Wynik odejmowania {a} - {b} = {a - b}")
            case "*":
                print(f"Wynik mnozenia {a} * {b} = {a * b}")
            case "/":
                print(f"Wynik dzielenia {a} / {b} = {a / b}")
            case _:
                break
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Błąd wartości")
    except TypeError:
        print("Błąd typu")
    except Exception as e:
        print("Błąd", e)
    else:
        print("Gdy nie ma błędu")
    finally:
        print("Zawsze")
