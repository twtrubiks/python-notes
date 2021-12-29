# Python 3.6 introduced a new implementation of dict.
# dict now keeps its items ordered as well.

# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
from collections import OrderedDict

if __name__ == "__main__":
    order_dic = OrderedDict()
    order_dic['a'] = 'A'
    order_dic['b'] = 'B'
    order_dic['c'] = 'C'
    order_dic['d'] = 'D'
    order_dic['e'] = 'E'

    for k, v in order_dic.items():
        print(k, v)

    # https://docs.python.org/3/library/collections.html#collections.OrderedDict.popitem
    # last=True -> LIFO
    # last=False -> FIFO

    print(
        order_dic.popitem(last=True) # -> ('e', 'E')
    )

    print(
        order_dic.popitem(last=False) # -> ('a', 'A')
    )


    # https://docs.python.org/3/library/collections.html#collections.OrderedDict.move_to_end
    # last=True   -> The item is moved to the right end
    # last=False  -> The item is moved to the beginning

    print('origin:', order_dic) # OrderedDict([('b', 'B'), ('c', 'C'), ('d', 'D')])
    order_dic.move_to_end('b', last=True)
    print(order_dic) # OrderedDict([('c', 'C'), ('d', 'D'), ('b', 'B')])
    order_dic.move_to_end('b', last=False)
    print(order_dic) # OrderedDict([('b', 'B'), ('c', 'C'), ('d', 'D')])