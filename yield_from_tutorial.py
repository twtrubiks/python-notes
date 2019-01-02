# Using yield from allows us to avoid having to deal with unexpected exceptions,
# let us focus on the implementation of business code.


def demo(n):
    i = 0
    while i < n:
        yield i
        i += 1


def test_yield_from(n):
    print("test_yield_from start")
    yield from demo(n)
    # 相當於下面
    # for item in demo(n):
    #     yield item
    print("test_yield_from end")


def example_1():
    for i in test_yield_from(3):
        print(i)


def return_yield():
    yield from (
        i
        for i in range(5)
    )


def example_2():
    result = return_yield()
    print(next(result))
    print(next(result))


def chain_old(*iterables):
    for it in iterables:
        for i in it:
            yield i


def chain(*iterables):
    for it in iterables:
        yield from it


def example_3():
    s = 'ABC'
    t = tuple(range(3))
    show = list(chain(s, t))
    print(show)


if __name__ == "__main__":
    example_1()
    example_2()
    example_3()
