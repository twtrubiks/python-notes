def fib_tail_recursion(num, result, temp):
    print('call')
    if num == 0:
        return result
    else:
        return fib_tail_recursion(num - 1, temp, result + temp)


if __name__ == '__main__':
    print(fib_tail_recursion(5, 0, 1))
