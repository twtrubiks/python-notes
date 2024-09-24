from module_b import ClassB

class ClassA:
    def __init__(self, b: ClassB) -> None:
        self.b = b

    def use_b(self) -> None:
        print("Using ClassB from ClassA")
