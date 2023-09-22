# REST API - jsony, GET, POST, PUT, DELETE, HEAD
# odpowiednik w bazie danych select, insert, update, delete
# CRUD - create, read, update, delete
import requests as re

# pip install requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
print(response)
# <Response [200]> - połaczenie ok
# 3..  błedy przekierowania
# 4.. grube błedy 404 - brak zaosby, 400 bad request
# 5xx - błedy wewnętrzne serwera (json nieprawidłowy)

table = response.json()
print(table)
print(type(table))  # <class 'dict'>
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '183/A/NBP/2023', 'effectiveDate': '2023-09-21', 'mid': 4.621}]}
# wypisac warotsci wszystkich kluczy
print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates'])  # [{'no': '183/A/NBP/2023', 'effectiveDate': '2023-09-21', 'mid': 4.621}]
print(table['rates'][0])  # # {'no': '183/A/NBP/2023', 'effectiveDate': '2023-09-21', 'mid': 4.621}
print(table['rates'][0]['mid'])  # 4.621
# kurs złota

url_gold = 'http://api.nbp.pl/api/cenyzlota/today'
response_gold = re.get(url_gold)
table_gold = response_gold.json()
print(table_gold)  # [{'data': '2023-09-22', 'cena': 267.0}]
# Komunikaty błędów
# W przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat
# 404 Not Found
# W przypadku zadania nieprawidłowo sformułowanych zapytań serwis zwraca komunikat 400 Bad Request
# W przypadku zapytania przekraczającego limit zwracanych danych serwis zwróci komunikat
# 400 Bad Request - Przekroczony limit
