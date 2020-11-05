from operator import mul

'''
operator.mul(a, b)
Return a * b
'''
# example_1
a, b = 2, 5
print(mul(a, b))

# example_2
print(list(map(mul, [1, 2, 3], [4, 5, 6])))
