class A:
    def __new__(cls, *args, **kwargs):
        print("__new__")
        instance = super().__new__(cls, *args, **kwargs)
        return instance

    def __init__(self):
        print("__init__")


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pass


if __name__ == "__main__":
    a = A()
    # output
    # __new__
    # __init__

    s1 = Singleton()
    s2 = Singleton()
    print(id(s1) == id(s2))
