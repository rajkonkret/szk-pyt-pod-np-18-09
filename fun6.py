# napisac funkcję obliczjącą średnia

def liczby(i=0, *cyfry):
    print(cyfry)  # ()
    print(type(cyfry))  # <class 'tuple'>
    suma = 0
    try:
        for c in cyfry:
            suma += c

        print(sum(cyfry))  # suma liczb z krotki cyfry
        print(suma)
        count = len(cyfry)
        srednia = suma / count
    except Exception as e:
        print("Bład", e)
    else:  # gdy nie ma błedu
        print(f"Srednia wynosi dla ucznia o numerze {i}: {srednia}")


liczby()  # ()
liczby(1, 2, 3)  # (1, 2, 3), (2, 3)
# i, *cyfry = 1,2,3
# i = 1
# cyfry = (2,3)
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 100, 100, 1, 1, 2, 3, 45)  # Srednia wynosi 17.470588235294116
liczby("1", 2, 3, 4, 5)  # Bład unsupported operand type(s) for +=: 'int' and 'str'

