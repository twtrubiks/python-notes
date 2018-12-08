def my_logging(func):
    def wrapper():
        print('logging - {} is running'.format(func.__name__))
        func()  # run func()  Equivalent run f1()

    return wrapper


@my_logging
def f1():
    print("f1")


f1()
