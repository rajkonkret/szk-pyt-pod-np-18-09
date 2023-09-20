def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)  # / oznacza, ze a i b mogą byc przekazane tylko pozycyjnie
    print("c, d", c, d)
    print("args", args)
    print('kwargs', kwargs)


# ile minimalnie argumentów trzeba podać przy wywołaniu tej funkcji
allparams(1, 2)  # a, b 1 2
# jak przekazac argument c
allparams(1, 2, 3)  # c, d 3 256
allparams(1, 2, c=3)  # c, d 3 256
# allparams(b=1, a=3, c=8)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - oddziela argumenty,
# które muszą zostac podane pozycyjnie od argumentów, które mogą zostac podane po nazwie
# jak przekazac argumenty do argsów
# allparams(1,2,c=8,1,2,3,4,5,6,7,8)  # SyntaxError: positional argument follows keyword argument
allparams(1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8, 100)  # args (1, 2, 3, 4, 5, 6, 7, 8, 100)
# argsy jako argumenty pozycyjne nie moga byc poprzedzone argumentem nazwanym np.: c=10
# jak przekazac argument d
allparams(1, 2, 3, 1, 2, 3, 4, d=123)  # d musi byc po nazwie
allparams(1, 2, 3, 1, 2, 3, d=123, a=9)  # kwargs {'a': 9}
# a trafia do kwargsów bo w definicji funkcji zmienna a nie moze byc wywołana po nazwie(/)
# elementy do kwargs
allparams(1, 2, 3, 12, 3, 4, a=0, abc='xyz', root='/', e=98)
# a, b 1 2
# c, d 3 256
# args (12, 3, 4)
# kwargs {'a': 0, 'abc': 'xyz', 'root': '/', 'e': 98}
# 13:30
# mogą byc tylko raz *args i raz **kwargs
