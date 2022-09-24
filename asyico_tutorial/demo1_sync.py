import time

def something(num):
    print('第 {} 任務，第一步'.format(num))
    time.sleep(2)
    print('第 {} 任務，第二步'.format(num))

if __name__ == "__main__":
    start = time.time()
    tasks = [something(i) for i in range(5)]
    print('TIME: ', time.time() - start)