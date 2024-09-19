from functools import singledispatchmethod

class DATA1:
    def show(self):
        print("DATA1")

class DATA2:
    def show(self):
        print("DATA2")

class A:

    @singledispatchmethod
    def fun(self, arg):
        raise NotImplementedError()


    @fun.register(DATA1)
    def _(self, arg):
        arg.show()


    @fun.register(DATA2)
    def _(self, arg):
        arg.show()


    @fun.register(type(None))
    def nothing(self, _):
        print("Nothing.")

if __name__ == '__main__':

    data1 = DATA1()
    data2 = DATA2()
    a = A()
    a.fun(data1) # DATA1
    a.fun(data2) # DATA2
    a.fun(None) # Nothing.