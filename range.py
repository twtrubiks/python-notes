# range vs xrange

import time

if __name__ == "__main__":
    # range
    print('range(5)', range(5))

    # range
    tStart = time.time()
    for i in range(10000000):
        pass
    tEnd = time.time()
    print('range time:', tEnd - tStart)

    # range
    tStart = time.time()
    for i in list(range(10000000)):
        pass
    tEnd = time.time()
    print('range time:', tEnd - tStart)
