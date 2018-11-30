def hello():
    print('hello in b2')


def show():
    from demo4.a4 import world
    print('show in b2')
    world()


if __name__ == '__main__':
    show()
