dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(type(dictionary))  # <class 'dict'>

# wypisze klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wartosci
for v in dictionary.values():
    print(v)

# pary - itemy
for i in dictionary.items():
    print(i)  # ('imie', 'Radek')

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => Kowalski

dictionary2 = {'name': 'imie', 'company': 'Różne'}
print(dictionary2)  # {'name': 'imie', 'company': 'Różne'}

print({value: key for key, value in dictionary2.items()})
# {'imie': 'name', 'Różne': 'company'}# {value:key}

d2 = {}
for key, value in dictionary2.items():
    print(key, "=>", value)
    d2[value] = key

print(d2)  # {'imie': 'name', 'Różne': 'company'}
