from functools import wraps


def my_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """my wrapper"""
        print('logging - {} is running'.format(func.__name__))
        func(*args, **kwargs)

    return wrapper


@my_logging
def f1(*args, **kwargs):
    """f1 function"""
    print("f1")

    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
print('f1.__name__', f1.__name__)  # output -> 'f1'
print('f1.__doc__', f1.__doc__)  # output -> 'f1 function'
