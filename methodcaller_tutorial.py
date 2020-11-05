# ref.
# https://docs.python.org/3/library/operator.html#operator.methodcaller

from operator import methodcaller

def example_1():
    s = 'a b c d e'
    upcase = methodcaller('upper')
    print(upcase(s))

    # Equivalent
    print(s.upper())


class A:

    def fun_2(self, data_1, data_2):
        print('{} + {}'.format(data_1, data_2))

def example_2():
    a_obj = A()
    fun_2_case = methodcaller('fun_2', 'data_1', 'data_2')
    fun_2_case(a_obj)

    # Equivalent
    a_obj.fun_2('data_1', 'data_2')

if __name__ == "__main__":
    example_1()
    # example_2()