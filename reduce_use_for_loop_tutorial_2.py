def process_item(item_new):
    item_new += 1
    result_new = item_new * item_new
    return result_new


if __name__ == "__main__":
    '''
    common write method
    '''
    results = []
    item_list = [0, 1, 2, 3, 4]
    for item in item_list:
        item += 1
        result = item * item
        results.append(result)
    print('results', results)

    '''
    better write method 1
    '''
    results = [process_item(item) for item in item_list]
    print('results', results)
