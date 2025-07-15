# 错误：返回的是同一个对象
# def triangles():
#     g = []
#     i = 1
#     while 1:
#         r = []
#         for j in range(i - 1, 1, -1):
#             # a = g[j - 1]
#             # b = g[j - 2]
#             g[j - 1] += g[j - 2]
#         g.append(1)
#         r = g
#         yield r
#         i += 1


def triangles():
    g = []
    i = 1
    while 1:
        for j in range(i - 1, 1, -1):
            # a = g[j - 1]
            # b = g[j - 2]
            g[j - 1] += g[j - 2]
        g.append(1)
        yield list(g)
        i += 1


def triangles2():
    prev_row = []
    while 1:
        current_row = [1]
        for i in range(1, len(prev_row)):
            current_row.append(prev_row[i - 1] + prev_row[i])
        if prev_row:  # list非空为True，空列表[]为False
            current_row.append(1)
        prev_row = current_row
        yield current_row


def triangles3():
    row = [1]
    while 1:
        yield row
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles3():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
