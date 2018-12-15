from datetime import date


# Create simple factory method using class method
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        print('cls:', cls)
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self._name + "'s age is: " + str(self._age))


def main():
    person = Person('twtrubiks', 18)
    person.display()

    person1 = Person.from_birth_year('John', 1985)
    person1.display()


if __name__ == "__main__":
    main()
