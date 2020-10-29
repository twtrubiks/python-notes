import abc


# class A(metaclass=abc.ABCMeta):
class A(abc.ABC):

    # abc.abstractmethod 請放在最內層
    @staticmethod
    @abc.abstractmethod
    def action1(x, y):
        pass

    # abc.abstractmethod 請放在最內層
    @classmethod
    @abc.abstractmethod
    def action2(cls, x, y):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class B(A):

    @staticmethod
    def action1(x, y):
        print('hello action1')
        print('x', x)
        print('y', y)

    @classmethod
    def action2(cls, x, y):
        print('hello action2', cls)
        print('x', x)
        print('y', y)
        return cls()

    def display(self):
        print('hello display')


B.action1('x1', 'y1')
B.action2('x2', 'y2').display()
