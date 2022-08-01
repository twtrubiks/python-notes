# ref
# https://docs.python.org/3/library/typing.html#typing.Any

from typing import Any


class A:
    def action(self, data: Any) -> None:
        print(data)


a = A()
a.action("test")
a.action(123)
a.action([1, 3, 4])
