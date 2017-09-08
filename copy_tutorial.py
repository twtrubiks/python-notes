import copy

if __name__ == "__main__":
    '''
    ref. https://docs.python.org/3.6/library/copy.html
    
    '''
    origin_list = [1, 2, [3, 4]]
    copy1 = copy.copy(origin_list)  # shallow copy
    copy2 = copy.deepcopy(origin_list)  # deep (recursive) copy
    print(copy1 == copy2)
    print(copy1 is copy2)
    origin_list[2][0] = "yoyo"
    print('origin_list:', origin_list)
    print('copy1:', copy1)
    print('copy2:', copy2)
