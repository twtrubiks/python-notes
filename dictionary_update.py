# dict.update([other])

if __name__ == "__main__":
    '''
    The update() method adds element(s) to the dictionary if the key is not in the dictionary.
    If the key is in the dictionary, it updates the key with the new value.

    If update() is called without passing parameters, the dictionary remains unchanged.
    '''

    # If the key is in the dictionary, it updates the key with the new value.
    dict_data = {'Name': 'twtrubiks', 'Age': 18}
    dict_data_update = {'Age': 20}
    dict_data.update(dict_data_update)
    print('dict_data :', dict_data)

    # if the key is not in the dictionary, adds element(s) to the dictionary
    dict_data_2 = {'Name': 'twtrubiks', 'Age': 18}
    dict_data_2.update({"color": "blue"})
    print('dict_data_2 :', dict_data_2)
    dict_data_2.clear() # clear dict data
    print('dict_data_2 :', dict_data_2)
