# Passing mutable lists or dictionaries as default arguments to a function can have unforeseen consequences.
# Usually when a programmer uses a list or dictionary as the default argument to a function,
# the programmer wants the program to create a new list or dictionary every time that the function is called.
# However, this is not what Python does. The first time that the function is called,
# Python creates a persistent object for the list or dictionary. Every subsequent time the function is called,
# Python uses that same persistent object that was created from the first call to the function.


# ref.
# https://docs.quantifiedcode.com/python-anti-patterns/correctness/mutable_default_value_as_argument.html


# error Anti-pattern
# Be careful with mutable default arguments
def append_anti_pattern(number, number_list=[]):  # if use pycharm , will warn you
    number_list.append(number)
    print(number_list)
    return number_list


def append(number, number_list=None):
    if number_list is None:
        number_list = []
    number_list.append(number)
    print(number_list)
    return number_list


if __name__ == "__main__":
    print('error Anti-pattern:')
    append_anti_pattern(5)  # expecting: [5], actual: [5]
    append_anti_pattern(7)  # expecting: [7], actual: [5, 7]
    append_anti_pattern(2)  # expecting: [2], actual: [5, 7, 2]
    print('right:')
    append(5)  # expecting: [5]
    append(7)  # expecting: [7]
    append(2)  # expecting: [2]
