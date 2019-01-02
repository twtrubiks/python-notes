from collections.abc import Iterable, Iterator


# The iter() method returns an iterator for the given object.

# The syntax of iter() method is
# iter(object[, sentinel])


# The iterator protocol
# Any class that provides an __iter__ method is iterable;
# that method must return an Iterator instance that will cover
# all the elements in that class.
# Since an iterator is already looping over elements,
# its __iter__ function traditionally return itself.

# Iterable - __iter__  (for in), iter(Iterable) -> Iterator
# Iterator - __next__ + __iter__

class PrintNumber:
    def __init__(self, max_number):
        self.max_number = max_number

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= self.max_number:
            raise StopIteration
        self.num += 1
        return self.num


def example_1():
    print_mum = PrintNumber(3)

    print_mum_iter = iter(print_mum)

    # prints '1'
    print(next(print_mum_iter))

    # prints '2'
    print(next(print_mum_iter))

    # prints '3'
    print(next(print_mum_iter))

    # raises StopIteration
    print(next(print_mum_iter))


class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self


def example_2():
    iterable = CapitalIterable('the aa bb cc dd')
    print('isinstance(iterable,Iterable):', isinstance(iterable, Iterable))
    iterator = iter(iterable)
    print('isinstance(iterator,Iterator):', isinstance(iterator, Iterator))
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    for i in iterable:
        print(i)


if __name__ == "__main__":
    example_1()
    # example_2()
