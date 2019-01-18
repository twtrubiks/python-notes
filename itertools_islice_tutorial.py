# https://docs.python.org/3.7/library/itertools.html#itertools.islice
from itertools import islice

'''
itertools.islice(iterable, start, stop[, step])

Make an iterator that returns selected elements from the iterable. 
If start is non-zero, then elements from the iterable are skipped until 
start is reached. Afterward, elements are returned consecutively unless 
step is set higher than one which results in items being skipped. 
If stop is None, then iteration continues until the iterator is exhausted, 
if at all; otherwise, it stops at the specified position.  
'''
if __name__ == '__main__':
    # islice('ABCDEFG', 2)  --> A B
    # islice('ABCDEFG', 2, 4) --> C D
    # islice('ABCDEFG', 2, None) --> C D E F G
    # islice('ABCDEFG', 0, None, 2) --> A C E G

    print(tuple(islice('ABCDEFG', 2)))  # --> A B
    print(list(islice('ABCDEFG', 2, 4)))  # --> C D
