class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(2 / 0)  # Bład division by zero
    # raise ZeroDivisionError  # Bład
    # raise ZeroDivisionError("Nie dziel przez zero") Bład Nie dziel przez zero

    raise MyException("Wystąpił wyjątek")  # MyException: Wystąpił wyjątek
except MyException:
    print("Wystapil wyjątek MyException")  # Wystapil wyjątek MyException
except Exception as e:
    print("Bład", e)
# 13:25