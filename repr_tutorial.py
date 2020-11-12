# repr
# Return a string representing the object as the developer wants to see it.

# str
# Return a string representing the object as the user wants to see it.

class A:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return '{} {}'.format(self._x, self._y)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({})'.format(class_name, self)

a = A(1, 2)
print('str(a)', str(a))
print('repr(a)', repr(a))
