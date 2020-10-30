
class StrMixin:
    def __str__(self):
        return '{}_{}'.format(self.x1, self.x2)

class A(StrMixin):
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

if __name__ == '__main__':
    a = A('x1', 'y1')
    print(a)

