import itertools
import operator

def example_1():
    # itertools.count(start=0, step=1)
    gen_1 = itertools.count(1, 2)
    print(next(gen_1))
    print(next(gen_1))
    print(next(gen_1))
    print(next(gen_1))
    print(next(gen_1))

def example_2():
    # it produces a generator that consumes
    # another generator and stops when a given predicate evaluates to False .
    # So we can combine the two and write this:
    gen_2 = itertools.takewhile(lambda n: n < 5, itertools.count(0, 1))
    print(list(gen_2))

def my_key(c):
    return c.lower() in 'abcde'

def example_3():
    print(list(filter(my_key, 'AbXHJsuaiqm')))
    print(list(itertools.filterfalse(my_key, 'AbXHJsuaiqm')))

def example_4():
    # dropwhile(predicate, it)
    # Consumes it skipping items while predicate computes truthy, then
    # yields every remaining item (no further checks are made)
    print(list(itertools.dropwhile(my_key, 'AbXHJsuaiqm')))

def example_5():
    # takewhile(predicate, it)
    # Yields items while predicate computes truthy, then stops and
    # no further checks are made
    print(list(itertools.takewhile(my_key, 'AbXHJsuaiqm')))

def example_6():
    # compress(it, selector_it)
    # Consumes two iterables in parallel; yields items from it whenever the
    # corresponding item in selector_it is truthy
    print(list(itertools.compress('abcdefg', (1,0,1,1,0,1))))

def example_7():
    # accumulate(p [,func])
    # p0, p0+p1, p0+p1+p2
    print(list(itertools.accumulate([1,2,3,4,5])))
    print(list(itertools.accumulate([9,4,2,0,5,8], min)))
    print(list(itertools.accumulate([1,0,9,2,10], max)))
    print(list(itertools.accumulate([1,2,3,4,5], operator.mul)))

def example_8():
    # enumerate(iterable, start=0)
    print(list(enumerate('abcdefg', 0)))

def example_9():
    # Yield all items from it1 , then from it2 etc., seamlessly
    # chain(it1, ..., itN)
    print(list(itertools.chain('abcdef', range(8))))

def example_10():
    # zip_longest(it1, ...,itN, fillvalue=None)
    print(list(itertools.zip_longest('ab', range(6))))
    print(list(itertools.zip_longest('ab', range(6), fillvalue='@')))

def example_11():
    print(list(itertools.product('ab', range(3)))) # 3*2 = 6(tuple)

    data = [1, 2, 3, 4]
    print(list(itertools.product('ab', data))) # 4*2 = 8(tuple)

    print(list(itertools.product('abc', repeat=2)))

    print(list(itertools.product(range(2), repeat=4)))

def example_12():
    cy = itertools.cycle('abc')
    for _ in range(10):
        print(next(cy))

def example_13():
    rp = itertools.repeat('b') # forever. b
    for _ in range(10):
        print(next(rp))

    print(list(itertools.repeat('c', 4))) # repeat 4 times

def example_14():
    print(list(itertools.combinations('ABCD', 2)))
    print(list(itertools.combinations_with_replacement('ABCD', 2)))

def example_15():
    print(list(itertools.permutations('ABCD', 2)))


if __name__ == "__main__":
    # example_1()
    # example_2()
    # example_3()
    # example_4()
    # example_5()
    # example_6()
    # example_7()
    # example_8()
    # example_9()
    # example_10()
    # example_11()
    # example_12()
    # example_13()
    # example_14()
    example_15()
