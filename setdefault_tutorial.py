# The method setdefault() is similar to get(),
# but will set dict[key]=default if key is not already in dict.

# dict.setdefault(key, default=None)

if __name__ == "__main__":
    dict_data = {'Name': 'twtrubiks', 'Age': 18}
    print('Name: {}'.format(dict_data.setdefault('Name', None)))
    print('Sex: {}'.format(dict_data.setdefault('Sex', None)))
    print('dict_data: {}'.format(dict_data))
