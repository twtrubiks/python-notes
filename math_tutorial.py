import math


if __name__ == "__main__":
    '''
    https://docs.python.org/3/library/math.html
    '''

    # 無條件進位到整數
    print(math.ceil(2.00001))

    # 無條件捨去到整數
    print(math.floor(2.99999))

    # 無條件進位到小數點第2位
    print(math.ceil(2.55 * 10) / 10)

    # 無條件進位到小數點第2位
    print(math.ceil(2.54 * 10) / 10)