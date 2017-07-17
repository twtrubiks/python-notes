if __name__ == "__main__":
    my_tuple = (1, 2, 3)
    print('my_tuple:', my_tuple)
    a, b, c = my_tuple
    print('a', a)
    print('b', b)
    print('c', c)

    print('my_tuple[0]:', my_tuple[0])
    print('my_tuple[1]:', my_tuple[1])
    print('my_tuple[1:3]:', my_tuple[1:3])

    # my_tuple[0] = 1 # error , tuple read only
