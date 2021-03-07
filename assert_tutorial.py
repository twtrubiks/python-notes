
def ex1():

    x = "hello"

    # returns True, then nothing happens
    assert x == "hello"

    # raise AssertionError
    assert x == "world"

def ex2():

    x = "hello"
    assert x == "world", "x should be 'hello'"

if __name__ == "__main__":
    ex1()
    # ex2()

