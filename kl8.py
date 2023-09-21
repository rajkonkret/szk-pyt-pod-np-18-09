# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasy B")


class C(B, A):
    """
    klasa C
    """

    def method(self):
        print("Metoda z klasy C")  # Metoda z klasy C
        super().method()  # Metoda z klasy B


a = A()
a.method()
b = B()
b.method()
# Metoda z klasy A
# Metoda z klasy B

c = C()
c.method()  # Metoda z klasy A (B,A)-> Metoda z klasy B

print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
