if __name__ == "__main__":
    # The map() function applies a given function to each item of an iterable (list, tuple etc.)
    # and returns a list of the results.

    # tutorial_1
    numbers = (1, 2, 3, 4)
    # lambda often used in like filter(), map() and reduce().
    result = map(lambda x: x * x, numbers)
    print('result: {}'.format(result))

    # filter object  (ref. filter.py Compare the difference)
    data = [
        {'key': 'a', 'value': 1},
        {'key': 'b', 'value': 2},
        {'key': 'c', 'value': 3},
        {'key': 'd', 'value': 4},
        {'key': 'e', 'value': 4},
    ]

    data_items = map(lambda x: x['value'], data)
    print('data_items: {}'.format(data_items))
    print('data_items_distinct: {}'.format(set(data_items)))

    # tutorial_2
    str_num = '1,2,3,4,5,6,7,8,9,10,11'
    int_seqs = list(map(int, str_num.split(',')))  # python3
    # int_seqs = map(int, str_num.split(','))  # python2
    print(isinstance(int_seqs, list))
    for seq in int_seqs:
        print(isinstance(seq, int))
        print(seq)

    # tutorial_3
    pattern = 'abcidkeujaddcsjb'
    print(list(map(pattern.find, pattern)))

