"""
ref
https://docs.python.org/3/reference/datamodel.html#object.__getitem__
https://docs.python.org/3/reference/datamodel.html#object.__setitem__
"""


class A:
    def __init__(self):
        self.my_dict = {
            "a": 1,
            "b": 2,
        }

    def __getitem__(self, key):
        return self.my_dict[key]

    def __setitem__(self, key, value):
        self.my_dict[key] = value


a = A()
print(a["a"])
print(a["b"])
a["c"] = 3
print(a["c"])
