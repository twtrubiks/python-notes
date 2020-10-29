class A:

    def action1(self):
        raise NotImplemented

    def action2(self):
        raise NotImplemented

class B(A):
    def action1(self):
        print('hello action1')

    def action2(self):
        pass

b = B()

# 沒有使用 abstractmethod 不一定要實作 action1, action2
b.action1()
b.action2()

