import pandas as pd

# pip install pandas

data = pd.read_csv('records.csv', delimiter=";")
print(data)
#
#       name branch  year  cgpa
# 0    radek    coe     3   9.1
# 1    radek    coe     3   9.1
# 2    Tomek    cos     2   9.0
# 3    Zenek    cor     1   8.1
# 4    Tadek    coa     2   9.7
# 5  Mateusz    cot     3  97.1

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
print(data.values[0])  # ['radek' 'coe' 3 9.1]
print(type(data.values))  # <class 'numpy.ndarray'>
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
# [['radek' 'coe' 3 9.1]
#  ['radek' 'coe' 3 9.1]
#  ['Tomek' 'cos' 2 9.0]
#  ['Zenek' 'cor' 1 8.1]
#  ['Tadek' 'coa' 2 9.7]
#  ['Mateusz' 'cot' 3 97.1]]
