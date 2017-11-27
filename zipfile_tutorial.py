# ref. https://docs.python.org/3/library/zipfile.html
import zipfile

if __name__ == "__main__":
    with zipfile.ZipFile('spam.zip', 'w') as myzip:
        myzip.write('test.txt')
