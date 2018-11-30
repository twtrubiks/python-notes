import demo3.a3


def hello():
    print('hello in b3')


def show():
    print('show in b3')
    demo3.a3.world()


if __name__ == '__main__':
    show()
