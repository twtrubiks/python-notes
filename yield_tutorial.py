# yield occurs and the generator pauses.
def common_func(max_number):
    print("create counter")
    counter = 0
    while counter < max_number:
        print(counter)
        print('counter +1')
        counter += 1


def yield_func(max_number):
    print("create counter")
    counter = 0
    while counter < max_number:
        yield counter
        print('counter +1')
        counter += 1


def example_1():
    num = yield_func(5)
    print(next(num))
    # print(next(num))
    # print(next(num))
    for n in num:
        print('n:', n)


def yield_step():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3


def example_2():
    test = yield_step()
    print(next(test))
    print(next(test))


def return_list():
    return [
        i for i in range(5)
    ]


def return_yield():
    yield from (
        i
        for i in range(5)
    )


def example_3():
    # yield only traversing once
    common_var = return_list()
    yield_var = return_yield()
    print('c1 in common_var')
    for c1 in common_var:
        print('c1:', c1)

    print('y1 in yield_var')
    for y1 in yield_var:
        print('y1:', y1)

    print('c2 in common_var')
    for c2 in common_var:
        print('c2:', c2)

    print('y2 in yield_var')  # not show
    for y2 in yield_var:
        print('y2:', y2)


if __name__ == "__main__":
    example_1()
    # example_2()
    # example_3()
