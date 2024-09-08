"""
The match case statement was introduced in Python 3.10
https://docs.python.org/zh-tw/3.11/tutorial/controlflow.html#match-statements
"""


def example_1(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 666 | 999:
            return "666 | 999"
        case _:
            return "Something's wrong with the internet"


print(example_1(404))  # Not found
print(example_1(666))  # 666 | 999
print(example_1(999))  # 666 | 999
print(example_1(123))  # Something's wrong with the internet


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=x, y=y) if x == y + 2:
            print("X=Y + 2")
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


# unpacking assignment
where_is(Point(0, 0))  # 'Origin'
where_is(Point(0, 5))  # 'Y=5'
where_is(Point(3, 0))  # 'X=3'
where_is(Point(2, 2))  # 'Somewhere else'
where_is(Point(2, 0))  # 'X=Y + 2'
where_is("Not a point")  # 'Not a point'
