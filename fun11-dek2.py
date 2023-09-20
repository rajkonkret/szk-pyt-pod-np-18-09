def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def lowercase_decorator(func):
    def wrapper():
        result = func()
        return result.lower()

    return wrapper


@lowercase_decorator
@uppercase_decorator
def greeting():
    return "Hello World"


print(greeting())  # HELLO WORLD
