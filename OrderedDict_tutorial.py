# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
from collections import OrderedDict

if __name__ == "__main__":
    print('Regular dictionary:')
    regular_dic = dict()
    regular_dic['a'] = 'A'
    regular_dic['b'] = 'B'
    regular_dic['c'] = 'C'
    regular_dic['d'] = 'D'
    regular_dic['e'] = 'E'

    for k, v in regular_dic.items():
        print k, v

    print('OrderedDict:')
    order_dic = OrderedDict()
    order_dic['a'] = 'A'
    order_dic['b'] = 'B'
    order_dic['c'] = 'C'
    order_dic['d'] = 'D'
    order_dic['e'] = 'E'

    for k, v in order_dic.items():
        print k, v
