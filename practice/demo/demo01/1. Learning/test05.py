from functools import reduce

# def my_factorial(pre, nxt):
#     return pre * nxt
#
#
# print(reduce(my_factorial, [1, 2, 3, 4, 5]))

print(reduce(lambda pre, nxt: pre * nxt, [1, 2, 3, 4, 5]))
