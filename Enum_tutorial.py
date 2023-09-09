from enum import Enum, unique


class Color(Enum):
    red = 1
    green = 2
    blue = 3

# @unique # 不能重複定義
# class ColorDuplicate(Enum):
#     red = 1
#     green = 2
#     blue = 2


def example_1():
    print('Color.red:', Color.red)
    print('repr(Color.red):', repr(Color.red))
    print('Color(1):', Color(1))
    member = Color.red
    print('member.name:', member.name)
    print('member.value:', member.value)


def example_2():
    animal = Enum('Animal', 'ant bee cat dog')  # <1>
    # is equivalent to
    # >>> class Animal(Enum):
    # ...     ant = 1
    # ...     bee = 2
    # ...     cat = 3
    # ...     dog = 4
    print('animal:', animal)
    print('animal.ant:', animal.ant)
    print('animal.ant.value:', animal.ant.value)
    print('list(animal):', list(animal))


if __name__ == "__main__":
    example_1()
    # example_2()
