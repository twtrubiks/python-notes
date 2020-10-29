import abc


# class A(metaclass=abc.ABCMeta):
class A(abc.ABC):

    @abc.abstractmethod
    def action1(self):
        pass

    @abc.abstractmethod
    def action2(self):
        pass

class B(A):
    def action1(self):
        print('hello action1')

    def action2(self):
        pass

# 有使用 abstractmethod 一定要實作 action1, action2
b = B()
b.action1()
b.action2()
