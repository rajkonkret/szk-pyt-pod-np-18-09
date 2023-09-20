# funkcje zagnieżdzone
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # bez () - ma zwrócic tylko adres gdzie sie funkcja znajduje. nie uruchamiac.


xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x00000139E1678860>
print(type(xFun))  # <class 'function'>
xFun()  # ()  - powodują uruchomienie funkcji zawartej w xFun czyli fun2
# 11:15
