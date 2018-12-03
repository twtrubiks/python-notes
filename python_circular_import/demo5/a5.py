def world():
    print('world in a5')


from demo5.b5 import hello


def show():
    print('show in a5')
    hello()


if __name__ == '__main__':
    show()
