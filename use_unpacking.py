if __name__ == "__main__":
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
