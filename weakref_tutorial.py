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

def example_3():
    # With WeakValueDictionary garbage collection can reclaim the object
    # when there are no other references to it.

    class Foo(object):
        pass

    A = Foo()
    B = weakref.ref(A)
    # B = A
    # <weakref at 0x108b43958; to 'Foo' at 0x108b2f468>
    del A
    print(B)
    # <weakref at 0x108b43958; dead>

if __name__ == "__main__":
    example_1()
    # example_2()
    # example_3()