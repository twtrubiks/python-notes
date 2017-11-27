# ref. https://docs.python.org/3/library/stdtypes.html

if __name__ == "__main__":
    '''
    str.translate(table[, deletechars]);
    '''
    # tutorial_1
    intab_1 = "abc"
    outtab_1 = "def"
    # make translation table
    trantab_1 = str.maketrans(intab_1, outtab_1)
    value_1 = "aabbcc"
    print('tutorial_1:', value_1.translate(trantab_1))

    # tutorial_2
    intab_2 = "abc"
    outtab_2 = "def"
    # make translation table and remove "2" this character
    trantab_2 = str.maketrans(intab_2, outtab_2, "2")
    value_2 = "2aabb123cc2"
    print('tutorial_2:', value_2.translate(trantab_2))
