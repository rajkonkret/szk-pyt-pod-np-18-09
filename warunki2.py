# match case
# python 3.10

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().replace(" ", "").strip():
    case "python":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case "pascal":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case _:  # wartość domyślna (odpowiednik else)
        print("Nie znam takiego języka")

print(lista)