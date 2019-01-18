# https://docs.python.org/3.7/library/itertools.html#itertools.tee
from itertools import tee

'''
itertools.tee(iterable, n=2)
Return n independent iterators from a single iterable.
'''
if __name__ == '__main__':
    print(tee([1, 2, 3, 4]))  # (<itertools._tee object at 0x02EDA508>, <itertools._tee object at 0x02EDD1E8>)
    iter1, iter2 = tee([1, 2, 3, 4])
    print(list(iter1))  # [1, 2, 3, 4]
    print(list(iter2))  # [1, 2, 3, 4]
