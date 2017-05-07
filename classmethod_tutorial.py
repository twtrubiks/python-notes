# ref. https://www.programiz.com/python-programming/methods/built-in/classmethod

# Static method vs Class method
# Static method knows nothing about the class and just deals with the parameters.
# Class method works with the class since its parameter is always the class itself.

from datetime import date


# Create factory method using class method
# random Person
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self._name + "'s age is: " + str(self._age))


# How class method works for inheritance?
# random Person
class Person2:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @staticmethod
    def from_fathers_age(name, father_age, father_person_age_diff):
        return Person2(name, date.today().year - father_age + father_person_age_diff)

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self._name + "'s age is: " + str(self._age))


class Man(Person2):
    sex = 'Male'


def main():
    # tutorial 1
    person = Person('Adam', 19)
    person.display()

    person1 = Person.from_birth_year('John', 1985)
    person1.display()

    # tutorial 2
    man = Man.from_birth_year('John', 1985)
    print(isinstance(man, Man))
    man.display()

    man1 = Man.from_fathers_age('John', 1965, 20)
    print(isinstance(man1, Man))
    man1.display()


if __name__ == "__main__":
    main()
