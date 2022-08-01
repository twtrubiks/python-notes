# ref
# https://docs.python.org/3/library/typing.html#typing.Tuple

from typing import Tuple

# "..." To specify a variable-length tuple

def show(data : Tuple[int, ...]) -> None:
    print(data)

show((1,2,3,))
show((1,2,))