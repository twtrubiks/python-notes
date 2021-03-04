# ref.
# https://docs.python.org/3/library/contextlib.html#contextlib.suppress

# ignore specific errors
from contextlib import suppress

def ex1():

    with suppress(TypeError):
        t = '1' / 0

    # Equivalent

    # try:
    #     t = '1' / 0
    # except TypeError:
    #     pass

def ex2():

    with suppress(TypeError, ZeroDivisionError):
        t = 1 / 0

    # Equivalent

    # try:
    #     t = 1 / 0
    # except (TypeError,ZeroDivisionError):
    #     pass

    # try:
    #     t = 1 / 0
    # except TypeError:
    #     pass
    # except ZeroDivisionError:
    #     pass

if __name__ == "__main__":
    ex1()
    # ex2()

