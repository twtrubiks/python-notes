def hello():
    print('hello in b5')


from demo5.a5 import world


def show():
    print('show in b5')
    world()


if __name__ == '__main__':
    show()
