# ref. https://docs.python.org/3/library/stdtypes.html#str.find

# str.find(sub[, start[, end]])

if __name__ == "__main__":
    data = 'hello 123 456 789'
    target = "456"
    print('data.find(target)', data.find(target))

    # Return -1 if it is not found.
    print('data.find(target, 11)', data.find(target, 11))
