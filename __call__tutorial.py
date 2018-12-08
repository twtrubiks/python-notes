class A:
    def __init__(self, data):
        self.__data = data

    def show(self):
        return self.__data

    # If a class defines a __call__ method, then its instances may be invoked as functions.
    def __call__(self):
        return self.show()


if __name__ == "__main__":
    a = A('hello')
    print('a.show():', a.show())
    print('a():', a())
    # a.show() = a()
    print('callable(a):', callable(a))
