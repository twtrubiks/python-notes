import demo3.b3


def world():
    print('world in a3')


def show():
    print('show in a3')
    demo3.b3.hello()


if __name__ == '__main__':
    show()
