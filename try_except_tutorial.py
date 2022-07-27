
def call_indexerror():
    raise IndexError

def call_my():
    print('hello')

def example_bad():
    try:
        call_indexerror()
        call_my()
    except IndexError:
        print('IndexError')

def example_good_1():
    try:
        call_indexerror()
    except IndexError:
        print('IndexError')
    else:
        # only execute if no exceptions are raised in the try block.
        call_my()

def example_good_2():
    try:
        print('pass')
    except IndexError:
        print('IndexError')
    else:
        # only execute if no exceptions are raised in the try block.
        call_my()

if __name__ == "__main__":
    # example_bad()
    example_good_1()
    # example_good_2()