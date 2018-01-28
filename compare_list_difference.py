# compare_list_difference

if __name__ == "__main__":
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 0, 4, 6, 7]
    '''
    # ex_1  list_1 - list_2 => {1, 3, 5}
    '''
    ex_1 = set(list_1) - set(list_2)
    print('ex_1', ex_1)
    '''
    # ex_2  list_1 - list_2 => { 0, 1, 3, 5, 6, 7 }
    ref. https://docs.python.org/3/library/stdtypes.html#frozenset.symmetric_difference
    '''
    ex_2 = set(list_1).symmetric_difference(list_2)
    print('ex_2', ex_2)
    '''
    # ex_3  list_1 and list_2 duplicate => {2, 4}
    ref. https://docs.python.org/3/library/stdtypes.html#frozenset.intersection
    '''
    ex_3 = set(list_1).intersection(set(list_2))
    print('ex_3', ex_3)
