if __name__ == "__main__":
    # The isinstance() function checks if the object (first argument)
    # is an instance or subclass of classinfo class (second argument).

    # isinstance(object, classinfo)
    # object - object to be checked
    # classinfo - class, type, or tuple of classes and types


    class Foo(object):
        a = 5


    fooInstance = Foo()

    print('instance of Foo? {}'.format(isinstance(fooInstance, Foo)))

    numbers = [1, 2, 3]

    is_list = isinstance(numbers, list)
    print('instance of list? {}'.format(is_list))

    is_dic = isinstance(numbers, dict)
    print('instance of dict? {}'.format(is_dic))

    is_dic_or_list = isinstance(numbers, (dict, list))
    print('instance of dict or list? {}'.format(is_dic_or_list))

    is_int = isinstance(numbers, int)
    print('instance of int? {}'.format(is_int))
