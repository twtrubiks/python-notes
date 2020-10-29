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
    pass

# 有使用 abstractmethod 一定要實作 action1, action2
b = B()
# TypeError: Can't instantiate abstract class B with abstract methods action1, action2
