def log(f):
    def wrapper():
        print('%s begin call' % f.__name__)
        f()
        print('%s end call' % f.__name__)

    return wrapper


@log
def f1():
    print('hello')


f1()
