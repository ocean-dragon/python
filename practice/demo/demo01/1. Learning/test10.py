def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    print(n)
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 生成无穷奇数序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 过滤该无穷奇数序列()


# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break
