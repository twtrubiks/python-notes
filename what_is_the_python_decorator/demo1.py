def f1():
    print("f1")


def register(func):
    func()


register(f1)
