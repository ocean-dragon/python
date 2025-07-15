def myadd(x, y, f):
    return f(x) + f(y)


k = myadd(-10, 10, abs)
print(k)
