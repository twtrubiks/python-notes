import functools


@functools.lru_cache()
def fib_lru_cache(n):
    print('call')
    if n < 2:
        return n
    return fib_lru_cache(n - 1) + fib_lru_cache(n - 2)


if __name__ == '__main__':
    print(fib_lru_cache(5))
