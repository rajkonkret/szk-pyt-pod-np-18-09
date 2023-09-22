# json - {"name":"Radek"}
# json - klucz:wartosc
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

dict_json = json.dumps(person_dict)
print(dict_json)
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
# wypisac klucze, wartosci, itemy
# wypisac imie z tego słownika (name)
print(data.keys())
print(data.values())
print(data.items())
# dict_keys(['age', 'czy_pali', 'name'])
# dict_values([40, None, 'Radek'])
# dict_items([('age', 40), ('czy_pali', None), ('name', 'Radek')])
print(data['name'])  # Radek
