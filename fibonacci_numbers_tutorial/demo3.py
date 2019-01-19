my_dict = dict()


def my_cache(fun):
    def wrap(*args, **kwargs):
        key = args[0]
        if key not in my_dict:
            my_dict[key] = fun(*args, **kwargs)
        return my_dict[key]

    return wrap


@my_cache
def fib_self_cache(n):
    if n < 2:
        return n
    return fib_self_cache(n - 1) + fib_self_cache(n - 2)


if __name__ == '__main__':
    print(fib_self_cache(5))
