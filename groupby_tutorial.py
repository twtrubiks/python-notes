from itertools import groupby

'''
ref. https://docs.python.org/3.6/library/itertools.html#itertools.groupby

itertools.groupby(iterable, key=None)

'''
if __name__ == "__main__":

    things = [("apple", "bear"),
              ("cherry", "bear"),
              ("banana", "duck"),
              ("cherry", "bear"),
              ("banana", "cactus"),
              ("cherry", "bear"),
              ("cherry", "bear"),
              ("apple", "speed boat"),
              ("apple", "school bus"), ]

    # Generally, the iterable needs to already be sorted on the same key function.  important!!
    things = sorted(things, key=lambda x: x[0])

    for key, group in groupby(things, lambda x: x[0]):
        print('key', key)
        print('group', list(group))
        print('==================')
