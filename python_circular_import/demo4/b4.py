def hello():
    print('hello in b4')


def show():
    from demo4.a4 import world
    print('show in b4')
    world()


if __name__ == '__main__':
    show()
