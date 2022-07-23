# ref
# https://docs.python.org/3.8/library/typing.html#typing.Callable

from typing import Callable


class Dog:
    def action(self) -> None:
        print("dog dog")


class Pet:
    def __init__(self, animal: Callable) -> None:
        self.animal = animal

    def show(self) -> None:
        self.animal()


dog = Dog()
pet = Pet(dog.action)
pet.show()
