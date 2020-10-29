# The method setdefault() is similar to get(),
# but will set dict[key]=default if key is not already in dict.

# dict.setdefault(key, default=None)

# setdefault does it all with a single lookup.

def ex1():
    dict_data = {'Name': 'twtrubiks', 'Age': 18}
    print('Name: {}'.format(dict_data.setdefault('Name', None)))
    print('Sex: {}'.format(dict_data.setdefault('Sex', None)))
    print('dict_data: {}'.format(dict_data))
    print('Likes: {}'.format(dict_data.setdefault('Likes', [])))
    print('dict_data: {}'.format(dict_data))


def ex2_letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies

# equal ex2_letter_frequency
def ex2_1_letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    return frequencies

if __name__ == "__main__":
    ex1()
    # print(ex2_letter_frequency('sentence'))
    # print(ex2_1_letter_frequency('sentence'))
