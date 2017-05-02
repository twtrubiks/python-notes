def sort_by_self(elem):
    return elem[1]


if __name__ == "__main__":
    # sorted(iterable[, key][, reverse])
    #  iterable - sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any iterator
    # reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
    #  key (Optional) - function that serves as a key for the sort comparison

    pyList = ['c', 'a', 'd', 'e', 'b']
    print('sorted(pyList): {}'.format(sorted(pyList)))
    print('pyList: {}'.format(pyList))

    # string
    int_string = '51423'
    print('int_string: {}'.format(sorted(int_string)))

    # vowels tuple
    pyTuple = ('c', 'a', 'd', 'e', 'b')
    print('sorted(pyTuple): {}'.format(sorted(pyTuple)))

    pySet = {'c', 'a', 'd', 'e', 'b'}
    print('sorted(pySet, reverse=True): {}'.format(sorted(pySet, reverse=True)))

    # random list
    random = [('b', 2), ('d', 4), ('a', 1), ('c', 3)]

    # sort list with key
    sortedList = sorted(random, key=sort_by_self)
    sortedList_random = sorted(random, key=lambda x: x[1])

    print('sortedList: {}'.format(sortedList))
    print('sortedList_random: {}'.format(sortedList_random))
