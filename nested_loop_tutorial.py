if __name__ == "__main__":
    '''
        common write method
    '''
    results = []
    for i in range(10):
        for j in range(i):
            results.append((i, j))
    print('results', results)

    '''
        better write method 1
    '''

    results = [(i, j)
               for i in range(10)
               for j in range(i)]
    print('results', results)
