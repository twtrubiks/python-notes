from dateutil.parser import parse

# ref. http://dateutil.readthedocs.io/en/stable/parser.html


if __name__ == "__main__":
    print(parse('2017/4  /4 4:00:00 PM '))
    print(parse('2017/4  -4 16:00:00  '))
