# Reduce is a really useful function for performing some computation on a list
# and returning the result. For example, if you wanted to compute the product of a list of integers.


if __name__ == "__main__":
    f = lambda a, b: a if (a > b) else b
    f_result = reduce(f, [47, 11, 42, 102, 13])
    print(f_result)
    total = reduce(lambda x, y: x + y, range(1, 101))
    print(total)
