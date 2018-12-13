class MyDecorator:
    def __init__(self, param):
        self.__param = param

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('do something before calling function {}'.format(func.__name__))
            print('self.__param', self.__param)
            func(*args, **kwargs)
            print('do something after calling function {}'.format(func.__name__))

        return wrapper


@MyDecorator('level')
def f1(*args, **kwargs):
    print('f1')
    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
