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
    # Python 3.12 起 sum() 對浮點數改用補償求和 (compensated summation),
    # 像 [0.01] * 10 這種情況 sum() 也能得到 0.1 了 (3.11 之前是 0.09999999999999999),
    # 所以這邊改用比較極端的數值 (取自 CPython math.fsum 的測試案例) 才看得出差異
    f_number = [1e100, 1.0, -1e100, 1e-100, 1e50, -1.0, -1e50]
    print('sum(f_number):', sum(f_number))  # 0.0
    #  Avoids loss of precision by tracking multiple intermediate partial sums
    print('math.fsum(f_number):', math.fsum(f_number))  # 1e-100

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
