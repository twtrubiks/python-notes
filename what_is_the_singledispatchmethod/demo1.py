from functools import singledispatch

class A:

    @singledispatch
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
    a.fun(123)
    # 正確應該要輸出 hello int or float, <class 'int'>
    # 但這邊卻輸入 my type: <class 'int'>
    # 代表 singledispatch 沒有生效