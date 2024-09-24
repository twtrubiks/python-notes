from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module_b_fix import ClassB

class ClassA:
    def __init__(self, b: "ClassB") -> None:
        self.b = b

    def use_b(self) -> None:
        print("Using ClassB from ClassA")