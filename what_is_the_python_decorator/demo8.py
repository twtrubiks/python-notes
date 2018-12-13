class MyDecorator:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('do something before calling function {}'.format(self.__func.__name__))
        self.__func(*args, **kwargs)
        print('do something after calling function {}'.format(self.__func.__name__))


@MyDecorator
def f1(*args, **kwargs):
    print('f1')
    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
