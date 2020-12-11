
class Demo_1:

    def __enter__(self):
        print('__enter__')
        return 'hello enter'

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return None

class Demo_2:

    def __enter__(self):
        print('__enter__')
        return 'hello enter'

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

def example_1():
    with Demo_1() as data:
        print('data:', data)
        1/0
        print('example_1')

def example_better():
    with Demo_2() as data:
        print('data:', data)
        1/0
        print('example_1')

if __name__ == '__main__':
    # example_1()
    example_better()