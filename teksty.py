tekst = "Witaj świecie"  # str
print(tekst)
print(type(tekst))  # <class 'str'>

tekst.upper()  # zamiana na duze litery
print(tekst)  # Witaj świecie
# """ Return a copy of the string converted to uppercase. """

tekst2 = tekst.upper()
print(tekst2)  # WITAJ ŚWIECIE
# teksty są niemutowalne - czyli podstawowy tekst w wyniku operacji metod nie jest zmieniany
print(tekst)
print(tekst.lower())  # witaj świecie
print(tekst)

print(tekst)
print(tekst2)

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst)  # Witaj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

# Radek - char - pojedynczy znak
# 01234 - numerowanie od zera
# liczymy ile razy wystepuje literka i
print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # 1, e znak o indeksie 4 nie jest brany pod uwage
# Witaj
# 01234
print(tekst.count("j", 0, 4))  # 0 bo j ma indeks 4 ale 4 nie bierze

print(len(tekst))  # 13 len() - długość tekstu

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona \b"  # f - stringformat - sformatowana wersja tekstu
print(tekst_format)
#	# Mam na imię Radek
# i lubię Pythona
# \t tabulator
# \n nowa linia
# \b powrót kursora, znak zostanie skasowany(backspace)

starszy = "Wiatj %s"
print(starszy % imie)  # Witaj Radek

print("""
Tekst 
    wielolinijkowy""")

# "Tekst
#     wielolinijkowy"

print("Wiataj {}".format(imie))
