# https://docs.python.org/3/library/io.html#binary-i-o

# StringIO 只能是 str，如果要操作 bytes data 就要使用 BytesIO

from io import BytesIO

def tutorial_1():
    # BytesIO 實作在內存 ( 記憶體 ram )中讀寫 bytes
    f = BytesIO()
    # 寫入的不是 str , 而是經過 utf-8 編碼的 bytes
    f.write('中文'.encode('utf-8'))
    print(f.getvalue())
    f.close() # 釋放記憶體

def tutorial_2():
    f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    result = f.read()
    print(result)
    print(result.decode('utf-8'))

def main():
    tutorial_1()
    # tutorial_2()

if __name__ == "__main__":
    main()