if __name__ == "__main__":
    # The enumerate() method adds counter to an iterable and returns it (the enumerate object).
    # enumerate(iterable, start=0)
    number_list = ['a', 'b', 'c', 'd', 'e']
    for index, value in enumerate(number_list, start=1):
        print('index: {} value: {}'.format(index, value))
