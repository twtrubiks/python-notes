# defaultdict means that if a key is not found in the dictionary,
# then instead of a KeyError being thrown, a new entry is created.
# The type of this new entry is given by the argument of defaultdict.

from collections import defaultdict

if __name__ == "__main__":
    # For the first example, default items are created using int(), which will return the integer object 0.
    int_dict = defaultdict(int)
    print('int_dict[3]', int_dict[3])  # print int(), thus 0
    # For the second example, default items are created using list(), which returns a new empty list object.
    list_dict = defaultdict(list)
    print('list_dict[test]', list_dict['ok'])  # print list(), thus []
    # default
    dic_list = defaultdict(lambda: 'test')
    dic_list['name'] = 'twtrubiks'
    print('dic_list[name]', dic_list['name'])
    print('dic_list[sex]', dic_list['sex'])
