import fnmatch
import os

pattern = 'demo*.txt'
print('Pattern :', pattern)


files = os.listdir('.')
for name in files:
    print(name, fnmatch.fnmatch(name, pattern))
