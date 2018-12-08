def my_logging(func):
    print('logging - {} is running'.format(func.__name__))
    func()


def f1():
    print("f1")


my_logging(f1)
