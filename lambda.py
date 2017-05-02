def show_max(m, n):
    return m if m > n else n


if __name__ == "__main__":
    # anonymous functions
    # often used in like filter(), map() and reduce(). ref. filter.py  map.py

    # common def
    print('show_max:{}'.format(show_max(100, 5)))  # show 100 (common def)

    # lambda
    show_lambda = lambda m, n: m if m > n else n  # but PEP-8 recommend use def
    print('show_lambda:{}'.format(show_lambda(100, 5)))  # show 100 (lambda)
