from datetime import datetime

# ref.  https://pyformat.info/
if __name__ == "__main__":
    print('%s %s' % ('one', 'two'))  # old method
    print('{} {}'.format('one', 'two'))
    print('{0} {1}'.format('one', 'two'))
    print('{1} {0}'.format('one', 'two'))

    print('{:.2}'.format(0.87666))
    print('{:.2%}'.format(0.873))

    print('{:>10}'.format('test'))
    print('{:.5}'.format('abcdefgh'))

    print('{:d}'.format(42))
    # print('{:d}'.format('42')) # error

    print('{:f}'.format(3.141592653589793))
    print('{:.2f}'.format(3.141592653589793))  # rounded to two decimal place
    # print('{:d}'.format(3.141592653589793)) # error
    print('{:0,}'.format(31234.14159))  # Format with commas
    print('{:0,.2f}'.format(31234.14159))  # rounded to two decimal place + Format with commas
    print("{:07d}".format(10)) # -> 0000010

    data_dic = {
        'first': 'TWT',
        'last': 'rubiks'
    }
    print('%(first)s %(last)s' % data_dic)  # old method
    print('{first} {last}'.format(**data_dic))

    data = [4, 8, 15, 16, 23, 42]
    print('{d[4]} {d[5]}'.format(d=data))

    # datetime format
    print('{:%Y-%m-%d %H:%M}'.format(datetime(2017, 2, 3, 4, 5)))
    DATETIME_FORMAT = '%Y-%m-%d %H:%M'
    print('{:{}}'.format(datetime(2017, 2, 3, 4, 5), DATETIME_FORMAT))
