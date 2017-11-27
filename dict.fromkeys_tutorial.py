if __name__ == "__main__":
    '''
    dictionary.fromkeys(sequence[, value])
    '''
    seq = ('name', 'age', 'sex')

    dict_1 = dict.fromkeys(seq)
    print('dict_1', dict_1)
    dict_2 = dict.fromkeys(seq, 10)
    print('dict_2', dict_2)
