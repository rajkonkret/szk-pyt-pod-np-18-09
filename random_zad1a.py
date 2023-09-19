import random

# random - generowanie liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6
print(random.random())  # float 0.14310813192354965 0..0.999999
print(random.random() * 6)  # 5.456057641210876 0..5.999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # 1..49
print(lista2)
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)

print(random.choices(lista2, k=6))  # [45, 34, 49, 5, 45, 48] - losuje z powtórzeniami
print(random.sample(lista2, 6))  # [23, 8, 22, 35, 2, 29] losuje bez powtórzeń
# 13:25
