import datetime


class A:
    def __init__(self, content):
        self._content = content

    @property
    def time(self):
        return datetime.datetime.now()


if __name__ == "__main__":
    a = A('hello')
    print('a.time:', a.time)
    # a.time = datetime.time(12, 20) # AttributeError: can't set attribute
