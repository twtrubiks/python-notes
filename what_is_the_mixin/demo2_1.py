
class HelloMixin:
    def display(self):
        print('HelloMixin hello')

class SuperHelloMixin:
    def display(self):
        print('SuperHello hello')

class A(SuperHelloMixin, HelloMixin):
    pass

if __name__ == '__main__':
    a = A()
    a.display()

