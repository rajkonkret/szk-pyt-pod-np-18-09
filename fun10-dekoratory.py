# dekoratory
# dekoruja inna funkcje dodatkowymi wlasciwosciami

def dekor(funk):
    def wew():
        result = funk()
        print("Dekorujemy")
        # return funk()
        return result

    return wew


@dekor  # uzycia na naszej funkcji dekoratora
def hej():
    print("Hej")


@dekor
def hej2():
    print("Ja nie jestem hej !!!")


hej()  # Hej
# z dekoratorem @dekor
# Dekorujemy
# Hej

hej2()
# Dekorujemy
# Ja nie jestem hej !!!
