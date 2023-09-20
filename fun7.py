# argumenty słownikowe **

def connect(**opcje):
    print(opcje)  # <class 'dict'>
    print(type(opcje))
    conect_param = {
        'host': '127.0.0.7',
        'port': '9090',
    }
    conect_param['pwd'] = opcje
    print(conect_param)  # {'host': '127.0.0.7', 'port': '9090', 'pwd': {'a1': '2', 'klucz': 'wartosc'}}
    print(conect_param['pwd']['klucz'])  # wartosc


# connect(1)  TypeError: connect() takes 0 positional arguments but 1 was given
# {klucz: wartosc}
# klucz=wartosc
connect(klucz='wartość')  # {'klucz': 'wartość'}
# connect(a1="2")  # {'a1': '2'}
connect(a1="2", klucz='wartosc')  # {'a1': '2', 'klucz': 'wartosc'}
connect(klucz='wartosc', a=8)
# {'host': '127.0.0.7', 'port': '9090', 'pwd': {'klucz': 'wartosc', 'a': 8}}
