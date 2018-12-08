def my_logging(func):
    def wrapper(*args, **kwargs):
        """my wrapper"""
        print('logging - {} is running'.format(func.__name__))
        func(*args, **kwargs)

    return wrapper


@my_logging
def f1(*args, **kwargs):
    """write logging"""
    print("f1")

    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
print('f1.__name__', f1.__name__)  # output -> 'wrapper'
print('f1.__doc__', f1.__doc__)  # output -> 'my wrapper'
