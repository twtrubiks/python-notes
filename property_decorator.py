class Square(object):
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @length.deleter
    def length(self):
        del self._length


if __name__ == "__main__":
    r = Square(5)
    print('length', r.length)  # automatically calls getter
    r.length = 6  # automatically calls setter
    print('length', r.length)
    del r.length
    # print('length', r.length)  # -> AttributeError: 'Square' object has no attribute '_length'
