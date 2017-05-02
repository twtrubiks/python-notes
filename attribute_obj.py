class Person(object):
    name = 'twtrubiks'


if __name__ == "__main__":
    p = Person()
    print('Before Set: {}'.format(p.name))

    # The setattr() method sets the value of given attribute of an object.
    # setattr(object, name, value)
    setattr(p, 'name', 'rubiks')
    print('After Set: {}'.format(p.name))

    # The getattr() method returns the value of the named attribute of an object
    # getattr(object, name[, default])
    # default (Optional) - value that is returned when the named attribute is not found
    print('The age is: {}'.format(getattr(p, 'age', 'default_20')))
    # print('The age is:'.format(p.age))  # error

    # creates a new attribute
    setattr(p, 'age', 18)
    print('After Set afe: {}'.format(getattr(p, 'age', 'default_20')))

    # The hasattr() method returns true if an object has the given named attribute and false if it does not.
    # hasattr(object, name)
    print('Person has name?: {}'.format(hasattr(p, 'name')))
    print('Person has salary?: {}'.format(hasattr(p, 'salary')))
