from collections import Counter


def ex1():
    c = Counter(['eggs', 'ham', 'eggs'])
    print('c[bacon]:', c['bacon'])
    print('c[eggs]:', c['eggs'])
    print('c:', c)


def ex2():
    cnt = Counter()
    for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
        cnt[word] += 1
    print(cnt)


def method_elements():
    c = Counter(a=4, b=2, c=0, d=-2)
    show = sorted(c.elements())
    print(show)
    print('c.values():', c.values())
    print('sum:', sum(c.values()))


def method_most_common():
    show = Counter('abracadabra').most_common(3)
    print(show)


def patterns():
    c = Counter(a=2, b=-4, c=0)
    print('+c:', +c)
    print('-c:', -c)
    # +c  # remove zero and negative counts


def method_subtract():
    c = Counter(a=4, b=2, c=0, d=-2)
    d = Counter(a=1, b=2, c=3, d=4)
    c.subtract(d)
    print('c:', c)


if __name__ == "__main__":
    ex1()
    ex2()
    method_elements()
    method_most_common()
    patterns()
    method_subtract()
