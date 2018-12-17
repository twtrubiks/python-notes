import functools


@functools.lru_cache(maxsize=2, typed=False)
def job(n):
    print('run very long.....')
    return n + 10000


if __name__ == '__main__':
    print(job(2))
    print(job(3))
    print(job(2))
    print(job(4))
    print(job(3))
