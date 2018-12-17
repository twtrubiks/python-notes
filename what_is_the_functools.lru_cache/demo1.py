import functools


@functools.lru_cache()
def job(n):
    print('run very long.....')
    return n + 10000


if __name__ == '__main__':
    print(job(2))
    print(job(2))
