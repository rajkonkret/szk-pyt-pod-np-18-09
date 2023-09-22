import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)
data = response.json()
print(data)
# {'results': [{'gender': 'male', 'name': {'title': 'Mr', 'first': 'Adolfo', 'last': 'Pérez'},
#               'location': {'street': {'number': 3577, 'name': 'Calle de Segovia'}, 'city': 'Gijón', 'state': 'Canarias',
#                            'country': 'Spain', 'postcode': 67761,
#                            'coordinates': {'latitude': '-32.0486', 'longitude': '-39.7271'},
#                            'timezone': {'offset': '+6:00', 'description': 'Almaty, Dhaka, Colombo'}},
#               'email': 'adolfo.perez@example.com',
#               'login': {'uuid': '0bc5952a-cbff-4f6d-a150-c3c0fc864800', 'username': 'goldenbird787',
#                         'password': 'alpine', 'salt': 'XS907yZ3', 'md5': '0ab212fba60ac7b3b70da36cda9dd632',
#                         'sha1': 'aef1f7cbadd9c9dc5cc551c7dd7cb23bc9dd878a',
#                         'sha256': 'f2dbd46a6e248560f801b40529baa25b699d91cde5deeae399062587b3210470'},
#               'dob': {'date': '1956-06-26T15:12:16.918Z', 'age': 67},
#               'registered': {'date': '2018-02-10T02:47:20.447Z', 'age': 5}, 'phone': '997-542-500',
#               'cell': '623-872-485', 'id': {'name': 'DNI', 'value': '00447893-X'},
#               'picture': {'large': 'https://randomuser.me/api/portraits/men/3.jpg',
#                           'medium': 'https://randomuser.me/api/portraits/med/men/3.jpg',
#                           'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/3.jpg'}, 'nat': 'ES'}],
#  'info': {'seed': '47acd5bae1f67e8d', 'results': 1, 'page': 1, 'version': '1.4'}}

print(data['results'][0]['name']['first'])
photo_url = data['results'][0]['picture']['large']
print(photo_url)
response_photo = requests.get(photo_url)

with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)
