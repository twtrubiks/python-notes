import time
from concurrent.futures import ProcessPoolExecutor

def calculate_time(func):
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        total_time = end_time - start_time
        print('total_time: {} ms'.format(total_time // 1000000))
        return result
    return timeit_wrapper

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

@calculate_time
def main():
    with ProcessPoolExecutor() as executor:
        for result in executor.map(fib, [10, 11, 12, 13] * 100, chunksize=1):
            print(result)

main()
