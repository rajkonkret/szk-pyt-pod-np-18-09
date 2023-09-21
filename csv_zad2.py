import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    # wyszukanie automatyczne separatora dla csv
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)
    csv_f.seek(0)
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x00000142CEB86FE0>

    fields = next(csvreader)  # odczyt pierwszego elementu i ustawienie wskaznika na drugi
    for row in csvreader:  # ta petla bedzie juz odczytywac od indeksu 1 (drugi element)
        rows.append(row)

print(rows)
print(fields)  # ['name', 'branch', 'year', 'cgpa']
