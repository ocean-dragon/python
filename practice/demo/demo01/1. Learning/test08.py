from functools import reduce
from collections.abc import Iterable

def str2float(s):
    num_list = s.split('.')
    
    num_int=  reduce(lambda x,y:x * 10 + y,map(lambda x: int(x),num_list[0]))
    num_float_list = [int(ch) for ch in num_list[1]]
    num_float = reduce(lambda x,y:x *10+ y, num_float_list) / (10 ** len(num_float_list))

    return num_int + num_float 

def str3float(s):
    num_str = s.split('.')
    num_list = list(map(lambda x : int(x), num_str))

    return reduce(lambda x, y : x * 1.0 + y * 0.1 ** len(num_str[1]),num_list)


print('str2float(\'123.456\') =', str3float('123.456'))
if abs(str3float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
