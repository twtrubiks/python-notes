def fn(x):
    return x if x > 3 else None


if __name__ == "__main__":
    # the filter() method filters the given iterable with the help of
    # a function that tests each element in the iterable to be true or not.
    # filter(function, iterable)
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = filter(fn, seq)
    print('result: {}'.format(result))

    # lambda often used in like filter(), map() and reduce().
    items = filter(lambda x: x > 3, seq)
    print('result_lambda: {}'.format(items))

    # filter object  (ref. map.py Compare the difference)
    data = [
        {'key': 'a', 'value': 1},
        {'key': 'b', 'value': 2},
        {'key': 'c', 'value': 3},
        {'key': 'd', 'value': 4},
        {'key': 'e', 'value': 4},
    ]
    data_items = filter(lambda x: x['value'] >= 3, data)
    print('data_items: {}'.format(data_items))
