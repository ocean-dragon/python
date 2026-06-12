def log(func):
    def wrapper():
        print("%s 开始执行" % func.__name__)
        func()
        print("%s 执行结束" % func.__name__)
    return wrapper

@log
def say_hello():
    print("hello")

def log(func):
    def wrapper(*args, **kwargs):
        print("%s 开始执行" % func.__name__)
        func(*args, **kwargs)
        print("%s 执行结束" % func.__name__)
    return wrapper

@log
def say_hello(content):
    print("hello, %s" % content)

say_hello("world")
