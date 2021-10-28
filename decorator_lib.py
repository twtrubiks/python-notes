from functools import wraps
from decorator import decorator

# decorator (https://github.com/micheles/decorator)
# pip3 install decorator

@decorator
def func_log_use_lib(func, *args, **kw):
    print('call', func.__name__)
    result = func(*args, **kw)
    print('end', func.__name__)
    return result

# 原生 decorator
def func_log(func):
    @wraps(func)
    def wrapped():
        print('call', func.__name__)
        func()
        print('end', func.__name__)

    return wrapped


@func_log
def hello_log():
    print('hello')

@func_log_use_lib
def hello_log_use_lib():
    print('hello')

if __name__ == '__main__':
    hello_log()
    hello_log_use_lib()
