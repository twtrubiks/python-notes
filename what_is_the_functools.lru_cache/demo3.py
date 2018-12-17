from lru_cache_tu.clockdeco import clock
import functools


@functools.lru_cache()
@clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print([fib(n) for n in range(16)])
