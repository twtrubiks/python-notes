def example1():
    # Not using explicit unpacking
    # elems = [4, 7, 18]
    #
    # elem0 = elems[0]
    # elem1 = elems[1]
    # elem2 = elems[2]
    # print(elem0, elem1, elem2)

    # Use unpacking
    elems = [4, 7, 18]
    elem0, elem1, elem2 = elems
    print(elem0, elem1, elem2)
    tuple_data = (0, 1, 2)
    tuple0, tuple1, tuple2 = tuple_data
    print(tuple0, tuple1, tuple2)


# Unpacking Operator
# *   -> Iterable
# **  -> Dictionary

def example2():
    # Packing With the * Operator

    *c, = 1, 2
    print('c', c)

    a, *b = 1, 2, 3
    print('a', a)
    print('b', b)

def example3():
    # *   -> Iterable
    *r, = range(5)
    # *r = range(5) # <- SyntaxError: starred assignment target must be in a list or tuple
    print(r)

def example4():
    # **  -> Dictionary
    # Unpacking Dictionaries With the ** Operator

    dict_1 = {"one": 1, "two": 2, "three": 3}
    dict_2 = {"a": "A", "b": "B", "c": "C"}
    merge_1 = {**dict_1, **dict_2}
    print(merge_1)
    merge_2 = {**{"a": 0, "b": 2, "c": 3}, **{"A": 3, "B": 2, "C": 1}}
    print(merge_2)

if __name__ == "__main__":
    example1()
    # example2()
    # example3()
    # example4()
