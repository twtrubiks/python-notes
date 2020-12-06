# Note that the iter function here returns a callable_iterator .

# The for loop in the example may run for a very long time,
# but it will never display 1(sentinel)
# raise StopIteration instead of yielding the sentinel.

# iter(func, sentinel)

from random import randint

def ex():
    return randint(1, 6)

def example_1():
    # ex must be a callable
    ex_iter = iter(ex, 1)
    print(ex_iter) # <callable_iterator object at 0x7ff5962e0b38>
    for e in ex_iter:
        print(e)

# This snippet reads lines from a file until
# a blank line is found or the end of file is reached

# def example_2(self, parameter_list):
#     with open('mydata.txt') as fp:
#         for line in iter(fp.readline, ''):
#             process_line(line)

if __name__ == "__main__":
    example_1()
