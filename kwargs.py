# You would use *args when you're not sure how many arguments might be passed to
# your function, i.e. it allows you pass an arbitrary number of arguments to your function


def everything(*args):
    for count, thing in enumerate(args, start=0):
        print('{0}. {1}'.format(count, thing))


# **kwargs allows you to handle named arguments that you have not defined in advance
def table_things(**kwargs):
    print('apple: {}'.format(kwargs.get('apple', 'default')))
    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


def print_three_things(a, b, c):
    print('a = {0}, b = {1}, c = {2}'.format(a, b, c))


if __name__ == "__main__":
    everything('apple', 'banana', 'cabbage')
    table_things(apple='fruit', cabbage='vegetable')
    mylist = ['aardvark', 'baboon', 'cat']
    print_three_things(*mylist)
