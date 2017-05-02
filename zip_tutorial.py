# The zip() function take iterables (can be zero or more),
# makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples.

# zip(*iterables)

if __name__ == "__main__":
    # tutorial 1
    numbers = [1, 2, 3]
    letters = ["A", "B", "C"]

    for numbers_value, letters_value in zip(numbers, letters):
        print(numbers_value, letters_value)

    # tutorial 2
    numberList = [1, 2, 3]
    strList = ['one', 'two', 'three']
    result = zip(numberList, strList)
    resultSet = set(result)
    print(resultSet)

    #  Unzipping the Value Using zip()
    numberList_org, strList_org = zip(*resultSet)
    print('numberList_org =', numberList_org)
    print('strList_org =', strList_org)
