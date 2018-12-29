# The method setdefault() is similar to get(),
# but will set dict[key]=default if key is not already in dict.

# dict.setdefault(key, default=None)


def ex1():
    dict_data = {'Name': 'twtrubiks', 'Age': 18}
    print('Name: {}'.format(dict_data.setdefault('Name', None)))
    print('Sex: {}'.format(dict_data.setdefault('Sex', None)))
    print('dict_data: {}'.format(dict_data))


def ex2_letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies


if __name__ == "__main__":
    ex1()
    # print(ex2_letter_frequency('sentence'))
