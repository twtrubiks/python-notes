import time
from contextlib import contextmanager


@contextmanager
def my_context():
    # do things in enter  ( __enter__ )
    yield
    # do things post  ( __exit__ )


@contextmanager
def tag(name):
    print('<{}>'.format(name))
    yield 'HIHI~'
    print('</{}>'.format(name))


@contextmanager
def elapsed_time(name=''):
    start_time = time.time()
    yield
    end_time = time.time() - start_time
    print(name, '{:.2f}'.format(end_time))


@contextmanager
def try_catch():
    try:
        yield 'okok'
    except Exception as e:
        print("e=%s" % str(e))
    finally:
        print('stop')


if __name__ == '__main__':
    # tutorial_1
    with tag('h1') as data:
        print('hello')
        print(data)

    # tutorial_2
    # with tag('h1'), tag('p'):
    #     print('hello')

    # tutorial_3
    # with elapsed_time('block'):
    #     time.sleep(2)

    # tutorial_4
    # with try_catch() as data:
    #     print(data)
    #     source = 1/0

