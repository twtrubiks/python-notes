import math

if __name__ == "__main__":
    '''
    sum(iterable[, start])
    ref. https://docs.python.org/3/library/functions.html#sum
    '''
    number = [1, 2, 3, 4]
    print('sum(number):', sum(number))
    print('sum(number) + 2:', sum(number, 2))

    '''
    math.fsum(iterable)
    ref. https://docs.python.org/3/library/math.html#math.fsum
    '''
    f_number = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    print('sum(f_number):', sum(f_number))
    #  Avoids loss of precision by tracking multiple intermediate partial sums
    print('math.fsum(f_number):', math.fsum(f_number))

    seq_obj = [
        {
            "count": 1
        },
        {
            "count": 2
        },
        {
            "count": 3
        },
        {
            "count": 4
        },
    ]
    total = sum(o.get('count') for o in seq_obj)
    print('total:', total)
