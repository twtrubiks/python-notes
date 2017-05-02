# range vs xrange

import time

if __name__ == "__main__":
    # range
    print('range(5)', range(5))

    # xrange
    xrange_data = xrange(5)
    print('xrange(5)', xrange_data)
    print('xrange_data[0]', xrange_data[0])

    # range
    tStart = time.time()
    for i in range(10000000):
        pass
    tEnd = time.time()
    print('range time:', tEnd - tStart)

    # xrange
    tStart = time.time()
    for i in xrange(10000000):
        pass
    tEnd = time.time()
    print('xrange time:', tEnd - tStart)
