"""
ref
https://docs.python.org/3/reference/datamodel.html#object.__getattr__

Called when the default attribute access fails with an AttributeError.

Note that if the attribute is found through the normal mechanism,
__getattr__() is not called.
"""


class A:
    def __init__(self, name: str):
        self.name = name

    def __getattribute__(self, item: str):
        return object.__getattribute__(self, item)

    def __getattr__(self, name: str) -> str:
        return name


a = A("twtrubiks")
print(a.aaa)  # trigger __getattr__
print(getattr(a, "aaa"))  # trigger __getattr__

print(a.name)  # not trigger __getattr__
print(getattr(a, "name"))  # not trigger __getattr__
