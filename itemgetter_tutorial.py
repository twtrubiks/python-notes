# ref. https://docs.python.org/3/library/operator.html#operator.itemgetter

from operator import itemgetter

# Basic tutorial
seqs = [1, 2, 3, 4]
x = itemgetter(1)
print('x:', x)
value = x(seqs)
print('value == x(seqs) == seqs[1]:', value)
xs = itemgetter(1, 3)
value2 = xs(seqs)
print('value2:', value2)

# Example of using itemgetter() to retrieve specific fields from a tuple record
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = itemgetter(1)
print('list(map(getcount, inventory)):', list(map(getcount, inventory)))
print('sorted(inventory, key=getcount):', sorted(inventory, key=getcount))
