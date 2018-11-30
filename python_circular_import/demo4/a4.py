def world():
    print('world in a2')


def show():
    from demo4.b4 import hello
    print('show in a2')
    hello()


if __name__ == '__main__':
    show()
