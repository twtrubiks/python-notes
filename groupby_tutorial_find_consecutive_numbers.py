# ref. https://docs.python.org/3.0/library/itertools.html#examples
from itertools import groupby
from operator import itemgetter

'''
seqs=[1,6,7,8,10,11]
index   value    (index-value)
  0      1          -1
  1      6          -5
  2      7          -5
  3      8          -5
  4      10         -6
  5      11         -6

[6,7,8]  [10,11]
'''

data = [1, 6, 7, 8, 10, 11]

for key, group in groupby(enumerate(data), lambda x: x[0] - x[1]):
    g = list(map(itemgetter(1), group))  # method_1
    # g = list(map(lambda x: x[1], group)) # method_2
    print('consecutive numbers', g)
