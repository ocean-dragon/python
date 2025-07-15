# from collections.abc import Iterable
#
# print(isinstance([], Iterable))


def myprint(x):
    return x ** 2


for item in map(myprint, [1, 2, 3, 4]):
    print(item, end=" ")
