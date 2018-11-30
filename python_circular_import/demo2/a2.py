from demo2.b2 import hello


def world():
    print('world in a2')


def show():
    print('show in a2')
    hello()


if __name__ == '__main__':
    show()
