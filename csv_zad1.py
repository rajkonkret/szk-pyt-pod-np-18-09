# pliki csv
# pliki tekstowe gdzie elementy rozdzielone separatorem
# Radek, Maciek, Zenek
import csv

row = ['radek', 'coe', 3, '9.1']
fields = ['name', 'branch', 'year', 'cgpa']
filename = 'records.csv'

dict2 = dict(zip(fields, row))
print(dict2)  # {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.1'}

dict_x = [
    {'name': 'radek', 'branch': 'coe', 'year': 3, 'cgpa': '9.10'},
    {'name': 'Tomek', 'branch': 'cos', 'year': 2, 'cgpa': '9'},
    {'name': 'Zenek', 'branch': 'cor', 'year': 1, 'cgpa': '8.1'},
    {'name': 'Tadek', 'branch': 'coa', 'year': 2, 'cgpa': '9.7'},
    {'name': 'Mateusz', 'branch': 'cot', 'year': 3, 'cgpa': '97.1'},
]

with open(filename, 'w', newline='', encoding='utf-8') as csv_f:
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(row) zapisanie pojedynczego wiersza
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerow(dict2)  # zapis jedego wiersza
    csvwriter.writerows(dict_x)  # zapis wielu wierszy z listy słowników
# 14:30
