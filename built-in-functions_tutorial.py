# Built-in Functions
# ref. https://docs.python.org/3.6/library/functions.html

if __name__ == "__main__":
    a = list(range(10))
    print(a)
    '''
    ref. https://docs.python.org/3.6/library/functions.html#all
    Return True if all elements of the iterable are true (or if the iterable is empty)
    '''
    print('all(a)', all(a))
    print('all([])', all([])) # all([]) returns True

    '''
    ref. https://docs.python.org/3.6/library/functions.html#any
    Return True if any element of the iterable is true. If the iterable is empty, return False.
    '''
    print('any(a)', any(a))
    print('any([])', any([])) # any([]) returns False
    '''
    ref. https://docs.python.org/3.6/library/functions.html#zip
    Make an iterator that aggregates elements from each of the iterables.
    '''
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print(list(zipped))
    '''
    ref. https://docs.python.org/3.6/library/functions.html#sum
    '''
    print('sum(a)', sum(a))
    '''
    ref. https://docs.python.org/3.6/library/functions.html#max
    '''
    print('max(a)', max(a))
    '''
    ref. https://docs.python.org/3.6/library/functions.html#min
    '''
    print('min(a)', min(a))
