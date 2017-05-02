if __name__ == "__main__":
    # The join() is a string method which returns a string concatenated with the elements of an iterable.
    numList = ['1', '2', '3', '4']
    seperator = ', '
    print(seperator.join(numList))

    num_int = [1, 2, 3, 4]
    # print(seperator.join(num_int)) # error
    print(seperator.join(str(x) for x in num_int))

    numTuple = ('1', '2', '3', '4')
    print(seperator.join(numTuple))

    seq = {'Python', 'Java', 'Ruby'}
    s = '->->'
    print(s.join(seq))
