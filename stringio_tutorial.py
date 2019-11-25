# https://docs.python.org/3/library/io.html#io.StringIO

# 讀寫文件不一定是文件, 也可以是存在內存 ( 記憶體 ram )
# StringIO 就是在 Ram 中讀寫 str

from io import StringIO

def tutorial_1():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())

    # Close object and discard memory buffer
    f.close() # 釋放記憶體 
    # print(f.getvalue()) # .getvalue() will now raise an exception.

def tutorial_2():
    # 讀取 StringIO
    f = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


def main():
    tutorial_1()
    # tutorial_2()

if __name__ == "__main__":
    main()