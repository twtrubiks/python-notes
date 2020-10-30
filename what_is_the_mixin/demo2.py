
class HelloMixin:
    def display(self):
        print('HelloMixin hello')

class A(HelloMixin):
    pass

if __name__ == '__main__':
    a = A()
    a.display()

