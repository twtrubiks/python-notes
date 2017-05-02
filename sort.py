def sort_by_self(elem):
    return elem[1]


if __name__ == "__main__":
    # list.sort(key=..., reverse=...)
    # sorted(list, key=..., reverse=...)
    # Note: Simplest difference between sort() and sorted() is:
    # sort() doesn't return any value while,
    # sorted() returns an iterable list.

    # sort() Parameters
    #  reverse - If true, the sorted list is reversed (or sorted in Descending order)

    vowels = ['c', 'a', 'd', 'e', 'b']

    # sort the vowels
    vowels.sort()
    # vowels.sort(reverse=True)
    print('Sorted list: {}'.format(vowels))
    print('Sorted list: {}'.format(vowels.sort()))

    # random list
    random = [('b', 2), ('d', 4), ('a', 1), ('c', 3)]
    random_lambda = [('b', 2), ('d', 4), ('a', 1), ('c', 3)]

    # sort list with key
    random.sort(key=sort_by_self)
    random_lambda.sort(key=lambda x: x[1], reverse=True)
    print('Sorted list use def: {}'.format(random))
    print('Sorted list use lambda: {}'.format(random_lambda))
