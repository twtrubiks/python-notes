# ref.
# https://docs.python.org/3/library/weakref.html#finalizer-objects
# https://docs.python.org/3/library/weakref.html#module-weakref

# A primary use for weak references is to implement caches or mappings holding large objects,
# where it’s desired that a large object not be kept alive solely
# because it appears in a cache or mapping.

# for garbage collector(GC)

import weakref

class Object:
    pass

def example_1():
    twtrubiks = Object()
    weakref.finalize(twtrubiks, print, "You killed twtrubiks!")
    del twtrubiks

def callback(x, y, z):
    print("hello")
    return x + y + z

def example_2():
    obj = Object()
    f = weakref.finalize(obj, callback, 1, 2, 3)
    print('f()', f())

if __name__ == "__main__":
    example_1()
    # example_2()