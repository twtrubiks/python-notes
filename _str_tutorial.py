class Person(object):
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __str__(self):
        return '{first} {last} is {age} years old'.format(**self.__dict__)


if __name__ == "__main__":
    data = 22
    print('data.__str__(): {}'.format(data.__str__()))
    print('type: {}'.format(type(data.__str__())))
    person = Person('twt', 'rubiks', 20)
    print('person: {}'.format(person))
