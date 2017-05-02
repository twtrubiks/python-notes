from calendar import monthrange


def data():
    return 'n1', 'n2'


if __name__ == "__main__":
    # _ is a traditional name for don't care
    _, show = data()
    print('show : {}'.format(show))

    # monthrange(year, month)
    # Returns weekday of first day of the month and number of days in month, for the specified year and month.
    _, num_days = monthrange(2017, 4)
    print('num_days : {}'.format(num_days))
