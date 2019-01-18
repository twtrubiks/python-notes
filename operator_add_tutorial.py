from operator import add

'''
operator.add(a, b)
Return a + b
'''
# example_1
a, b = 1, 2
print(add(a, b))

# example_2
print(list(map(add, [1, 2, 3], [4, 5, 6])))
