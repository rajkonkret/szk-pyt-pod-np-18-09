from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-09-19
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)
print(type(time))
# 2023-09-19 15:14:07.158917
# <class 'datetime.datetime'>

print(time.hour)
print(today.day)

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 19/09/2023

formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 15:16

formatted_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # 2023-09-19 15:19:20
print(type(formatted_datetime))  # <class 'str'>

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tommorow = today + timedelta(days=1)
print(tommorow)  # 2023-09-20
# t2 = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'

products = [
    {'sku': 1, 'exp_date': today, "price": 100.0},
    {'sku': 2, 'exp_date': tommorow, "price": 80.0},
    {'sku': 3, 'exp_date': today, "price": 20},
]

print(products)

for product in products:
    print(product)  # {'sku': 3, 'exp_date': datetime.date(2023, 9, 19), 'price': 20}
    if product['exp_date'] != today:
        continue  # nie wykona kolejnych instrukcji,
        # pobierze kolejny elemnt z listy i zacznie instrukcje z pętli od nowa
    product['price'] *= 0.8  # p = p * 0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}""")
