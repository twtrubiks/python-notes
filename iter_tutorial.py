
# The iter() method returns an iterator for the given object.

# The syntax of iter() method is
# iter(object[, sentinel])


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


if __name__ == "__main__":
    printNum = PrintNumber(3)

    printNumIter = iter(printNum)

    # prints '1'
    print(next(printNumIter))

    # prints '2'
    print(next(printNumIter))

    # prints '3'
    print(next(printNumIter))

    # raises StopIteration
    print(next(printNumIter))
