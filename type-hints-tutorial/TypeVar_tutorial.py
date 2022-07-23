# ref
# https://docs.python.org/3.8/library/typing.html#typing.TypeVar

from typing import TypeVar

T = TypeVar("T")  # Can be anything


class Dog:
    pass


class Cat:
    pass


class Pet:
    def __init__(self, animal: T) -> None:
        pass


dog = Dog()
cat = Cat()
pet_cat = Pet(cat)
pet_dog = Pet(dog)
