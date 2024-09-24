from module_a import ClassA

class ClassB:
    def __init__(self, a: ClassA) -> None:
        self.a = a

    def use_a(self) -> None:
        print("Using ClassA from ClassB")