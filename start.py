import pakiet
import pakiet.fun as pk
from pakiet import fun

print(pakiet)
# <module 'pakiet' from 'C:\\Users\\CSComarch\\PycharmProjects\\szk-pyt-pod-np-18-09\\pakiet\\__init__.py'>
pk.powitanie()
fun.powitanie()
pakiet.info()
# pakiet.powitanie()  # AttributeError: module 'pakiet' has no attribute 'powitanie'
fun.info()