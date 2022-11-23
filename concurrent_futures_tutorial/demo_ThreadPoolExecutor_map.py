import time
from concurrent.futures import ThreadPoolExecutor

def calculate_time(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print('total_time: {} seconds'.format(total_time))
        return result
    return timeit_wrapper

def task(id):
    print('start {}'.format(id))
    time.sleep(1)
    return 'end {}'.format(id)

@calculate_time
def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        for result in executor.map(task, [1, 2, 3, 4]):
            print(result)

main()
