# def test_generator():
#     for i in range(1, 4):
#         yield i
def test_generator():
    i = 0
    g = []
    while i < 3:
        i += 1
        g.append(i)
        print(g)
        yield i

    return "end"


for item in test_generator():
    print(item)

g = (x for x in range(11) if x % 2 == 0)
print(g)
print(list(g))
