def my_logging(func):
    def wrapper():
        print('logging - {} is running'.format(func.__name__))
        func()  # run func()  Equivalent run f1()

    return wrapper


def bold(func):
    def wrapper():
        print("<b>")
        func()
        print("</b>")

    return wrapper


def italic(func):
    def wrapper():
        print("<i>")
        func()
        print("</i>")

    return wrapper


@my_logging
@bold
@italic
def f1():
    print("f1")


f1()
