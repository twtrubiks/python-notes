# range

# ref. https://docs.python.org/3.0/whatsnew/3.0.html#views-and-iterators-instead-of-lists
# python3 no longer exists xrange
# range() now behaves like xrange() used to behave, except it works with values of arbitrary size.

import time

if __name__ == "__main__":
    # range
    print('range(5)', range(5))
    print('list(range(5))', list(range(5)))

    # range
    tStart = time.time()
    for i in range(10000000):
        pass
    tEnd = time.time()
    print('range time:', tEnd - tStart)
