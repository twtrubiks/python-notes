"""
ref:
https://docs.python.org/3.12/library/functools.html#functools.singledispatchmethod

the dispatch happens on the type of the first non-self or non-cls argument:

所以如果使用 class 必須使用 singledispatchmethod, singledispatch 在 class 中沒作用
"""

from functools import singledispatchmethod

class A:

    @singledispatchmethod
    def fun(self, arg):
        print('my type:', type(arg))


    @fun.register(int)
    @fun.register(float)
    def _(self, arg):
        print('hello int or float,', type(arg))


    @fun.register(list)
    def _(self, arg):
        print('hello list')
        for i, elem in enumerate(arg):
            print(i, elem)


    @fun.register(type(None))
    def nothing(self, _):
        print("Nothing.")


if __name__ == '__main__':
    a = A()
    a.fun(123) # 有正確輸出 hello int or float, <class 'int'>
