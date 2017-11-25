def number_add(num):
    return num + 1

if __name__ == "__main__":
    '''
    common write method
    '''
    item_list = [0, 1, 2, 3]
    result = []
    for item in item_list:
        new_item = number_add(item)
        result.append(new_item)
    print('result', result)

    '''
    better write method 1
    '''
    result = [number_add(item) for item in item_list]
    print('result', result)

    '''
    better write method 2
    '''
    # result2 = map(int, str_num.split(','))  # python2
    result = list(map(lambda x: number_add(x), item_list))
    print('result', result)

    # tuple
    result = tuple(map(lambda x: number_add(x), item_list))
    print('result tuple', result)
