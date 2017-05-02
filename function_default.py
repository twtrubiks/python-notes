# REF.
# http://blog.thedigitalcatonline.com/blog/2015/02/11/default-arguments-in-python/#.WPg_61OGPwc


def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default


def get_test(iterable, default='yo'):
    return '{} {}'.format(iterable, default)


if __name__ == "__main__":
    print(get_test('t1'))
    print(get_test('t1', 't2'))
