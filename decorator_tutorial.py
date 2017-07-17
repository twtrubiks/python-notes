import time
from functools import wraps


# tutorial decorator with argument
def decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)

    return wrapped


def bold(func):
    @wraps(func)
    def wrapper():
        print("<b> level one")
        func()
        print("</b>")

    return wrapper


def italic(func):
    @wraps(func)
    def wrapper():
        print("<i> level two")
        func()
        print("</i>")

    return wrapper


@bold
@italic
def sandwich(data="my sandwich"):
    print(data)


@italic
@bold
def sandwich_worse(data="my sandwich worse"):
    print(data)


def elapsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(func.__name__, end_time)
        return res

    return wrapper


@elapsed_time
def elapsed_time_tutorial():
    time.sleep(2)


# function log
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


# top function exception
def sub_command(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError:
            print('help_string')
        except Exception as e:
            print('please contact us:', e)

    return wrapped


@sub_command
def git_status():
    print('git_status')


if __name__ == '__main__':
    # tutorial_1
    sandwich()

    # The order is important
    # sandwich_worse()

    # tutorial_2
    # elapsed_time_tutorial()

    # tutorial_3
    # hello_log()

    # tutorial_4
    # git_status()
