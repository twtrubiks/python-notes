"""
pip3 install cachetools

https://pypi.org/project/cachetools/
"""

from cachetools import cached, LRUCache, TTLCache
import time

@cached(cache={})
def ex1_cache():
    print('no cached')
    return 'my data'

def ex1():
    for _ in range(3):
        print(ex1_cache())

    # 手動清理快取
    # ex1_cache.cache_clear()

    # for _ in range(3):
    #     print(ex1_cache())


@cached(LRUCache(maxsize=10))
def ex2_cache(count):
    print('no cached')
    return 'my data'

def ex2():
    print('step1...')
    for i in range(10):
        # 這裡沒快取  因為第一次
        print(ex2_cache(i))

    print('step2...')
    for i in range(10):
        # 這裡都有快取
        print(ex2_cache(i))

    print('step3...')
    for i in range(30, 40):
        # 快取開始失效, 因為超過 maxsize
        print(ex2_cache(i))


@cached(TTLCache(maxsize=5, ttl=2))
def ex3_cache():
    print('no cached')
    return 'my data'

def ex3():
    for _ in range(5):
        print(ex3_cache())

    time.sleep(3)
    # 快取失效

    for _ in range(5):
        print(ex3_cache())

MY_CACHE = TTLCache(maxsize=200, ttl=2)

def set_cache():
    MY_CACHE['1'] = '1'
    MY_CACHE['2'] = '2'
    MY_CACHE['3'] = '3'

def get_cache():
    if MY_CACHE.get('1'):
        print('cached')
        print(MY_CACHE.get('1'))
    else:
        print('no cached')

def ex4():
    set_cache()

    for _ in range(3):
        get_cache()

    print('查看目前 cache 狀態:', dict(MY_CACHE))
    print('sleep 2.5 sec')
    time.sleep(2.5)

    # cached expired
    get_cache()

if __name__ == '__main__':
    ex1()
    # ex2()
    # ex3()
    # ex4()