# dict.get(key, default=None)

def example_1():
    # tuple 可以當作 dict 的 key
    my_dict_1 = {(1, 2): 5, (3, 4): 6, (5, 6): 7}
    print(my_dict_1[(1, 2)])

    # equal
    my_dict_2 = {1: {2: 5}}
    print(my_dict_2[1][2])

if __name__ == "__main__":
    dict_data = {'Name': 'twtrubiks', 'Age': 18}

    # dict common use
    print('dict["Name"] : {}'.format(dict_data['Name']))

    # if key does not exist in dict --> error
    # print('dict["Name"] : {}'.format(dict_['height']))  # error

    # if key does not exist in dict --> use dict.get(key, default=None)
    print('dict["Name"] : {}'.format(dict_data.get('height', 'default height')))

    # dict.pop
    print('dict_data: {}'.format(dict_data))
    pop_data = dict_data.pop('Name', None)
    print('pop_data: {} from dict_data'.format(pop_data))
    print('dict_data: {}'.format(dict_data))

    numbers = [1, 2, 3]
    my_dict = {number: number * 2 for number in numbers}
    print(my_dict)  # {1: 2, 2: 4, 3: 6}
    example_1()