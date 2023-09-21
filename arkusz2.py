import pandas as pd

excel_data = pd.read_excel("sales.xlsx")
data = pd.DataFrame(excel_data)
# data = pd.DataFrame(excel_data, columns=['Sales Date'])
print(data)
#   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000
#   Sales Date
# 0 2018-05-12
# 1 2019-12-06
# 2 2020-08-09
# 3 2021-04-07
print(data.columns)
print(data.values)
print(data.items)
# Index(['Sales Date', 'Sales Person', 'Amount'], dtype='object')
# [[Timestamp('2018-05-12 00:00:00') 'Sila Ahmed' 60000]
#  [Timestamp('2019-12-06 00:00:00') 'Mir Hossain' 50000]
#  [Timestamp('2020-08-09 00:00:00') 'Sarmin Jahan' 45000]
#  [Timestamp('2021-04-07 00:00:00') 'Mahmudul Hasan' 30000]]
# <bound method DataFrame.items of   Sales Date    Sales Person  Amount
# 0 2018-05-12      Sila Ahmed   60000
# 1 2019-12-06     Mir Hossain   50000
# 2 2020-08-09    Sarmin Jahan   45000
# 3 2021-04-07  Mahmudul Hasan   30000>