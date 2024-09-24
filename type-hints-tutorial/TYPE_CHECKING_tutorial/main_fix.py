from module_a_fix import ClassA
from module_b_fix import ClassB

a = ClassA(None)
b = ClassB(a)
b.use_a()