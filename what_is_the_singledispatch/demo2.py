from functools import singledispatch


@singledispatch
def fun(arg):
    print('my type:', type(arg))


@fun.register(int)
@fun.register(float)
def _(arg):
    print('hello int or float,', type(arg))


@fun.register(list)
def _(arg):
    print('hello list')
    for i, elem in enumerate(arg):
        print(i, elem)


@fun.register(type(None))
def nothing(_):
    print("Nothing.")


if __name__ == '__main__':
    fun("Hello, world.")
    # fun(123)
    # fun(123.3)
    # fun([1, 2, 3])
    # fun({'a': 2})
    # fun(None)
