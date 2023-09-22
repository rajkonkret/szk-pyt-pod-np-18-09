import requests
import xml.etree.ElementTree as ET

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format=xml'

response = requests.get(url)
print(response)  # <Response [200]>

xml_data = response.content
print(xml_data)

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x000001D9EAE46480>

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # Tabela: A

date = root.find(".//EffectiveDate").text
print(f"Data tabeli: {date}")  # Data tabeli: 2023-09-22

no = root.find('.//No').text
print(f"Numer tabeli: {no}")  # Numer tabeli: 184/A/NBP/2023

rates = root.findall('.//Rate')
print(rates)

# < Rate >
# < Currency > hrywna(Ukraina) < / Currency >
# < Code > UAH < / Code >
# < Mid > 0.1171 < / Mid >
# < / Rate >
for rate in rates:
    # print(rate)  # <Element 'Rate' at 0x0000027B39305300>
    currency = rate.find('Currency').text
    code = rate.find('Code').text
    mid = rate.find('Mid').text
    print(f"{code}: {currency} - {mid}")
