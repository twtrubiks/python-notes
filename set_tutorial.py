if __name__ == "__main__":
    '''
    ref. https://docs.python.org/3/tutorial/datastructures.html#sets
    A set is an unordered collection with no duplicate elements
    '''
    # set_seqs = {'a', 'b'} # set
    # dict_seqs = {} # dict
    set_seqs = set()
    set_seqs.add('test1')
    set_seqs.add('test2')
    print('set_seqs:', set_seqs)
    set_seqs.add('test1')
    print('set_seqs:', set_seqs)

    '''
    remove(elem)
        Remove element elem from the set. Raises KeyError if elem is not contained in the set.
    '''
    set_seqs.remove('test1')
    print('set_seqs:', set_seqs)
    # set_seqs.remove('test1') ## Raises KeyError

    '''
    discard(elem)
        Remove element elem from the set if it is present.
    '''
    set_seqs.discard('test1')
    print('set_seqs:', set_seqs)

    set_1 = {"a", "b", "c", "d"}
    set_2 = {"d", "e", "f", "g"}
    print("All: {}".format(set_1.union(set_2)))
    print("Both: {}".format(set_1.intersection(set_2)))
    print("Either but not both: {}".format(
        set_1.symmetric_difference(set_2)))
