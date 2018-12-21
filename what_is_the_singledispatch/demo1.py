def fun(arg):
    if not arg:
        print("Nothing.")
        return
    if isinstance(arg, int) or isinstance(arg, float):
        print('hello int or float,', type(arg))
    elif isinstance(arg, list):
        print('hello list')
        for i, elem in enumerate(arg):
            print(i, elem)
    else:
        print('my type:', type(arg))


if __name__ == '__main__':
    fun("Hello, world.")
    fun(123)
    fun(123.3)
    fun([1, 2, 3])
    fun({'a': 2})
    fun(None)
