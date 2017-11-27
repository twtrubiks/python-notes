# ref. https://docs.python.org/3/library/html.html
import html.parser

if __name__ == "__main__":
    test = '123>ss<see1&sd2"'
    escaped = html.escape(test, quote=True)
    print('escaped:', escaped)

    unescaped = html.unescape(test)
    print('unescaped:', unescaped)
