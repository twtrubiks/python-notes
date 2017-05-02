# dict.get(key, default=None)

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
