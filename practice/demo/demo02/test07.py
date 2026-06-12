def log(*args):
    is_func = callable(args[0])
    if is_func:
        f = args[0]
    else:
        text = args[0]

    def wrapper1():
        print('%s begin call' % f.__name__)
        f()
        print('%s end call' % f.__name__)

    def decorator(func):
        def wrapper2():
            print('%s begin call, %s' % (func.__name__, text))
            func()
            print('%s end call, %s' % (func.__name__, text))

        return wrapper2

    if is_func:
        return wrapper1
    else:
        return decorator


@log
def f1():
    print('hello1')


@log('execute')
def f2():
    print('hello2')


f1()
f2()
