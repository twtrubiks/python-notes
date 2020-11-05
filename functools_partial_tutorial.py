from functools import partial

from operator import mul

def link_string(x, y):
    print('{}_{}'.format(x, y))

def example_1():
    result = partial(link_string, y='data')
    result('test_1')
    result('test_2')

def example_1_2():
    # x = 'data'
    result = partial(link_string, 'data')
    result('test_1')
    result('test_2')

def example_2():
    ten_times = partial(mul, 10)
    print(ten_times(8))
    print(ten_times(10))
    print(list(map(ten_times, range(1, 5))))

if __name__ == "__main__":
    example_1()
    # example_1_2()
    # example_2()


