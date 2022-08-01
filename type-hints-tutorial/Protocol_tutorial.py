# ref
# https://docs.python.org/3.8/library/typing.html#typing.Protocol
# static duck-typing

from typing import Protocol


class Proto(Protocol):
    def meth(self) -> int:
        ...


class A:
    def meth(self) -> int:
        return 10


class B:
    def meth(self) -> int:
        return 0


def func(duck: Proto) -> int:
    return duck.meth()


print(func(A()))
print(func(B()))
