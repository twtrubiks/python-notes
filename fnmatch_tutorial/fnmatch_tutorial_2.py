import fnmatch
import os

pattern = 'demo*.txt'
print('Pattern :', pattern)
files = os.listdir('.')
matches = fnmatch.filter(files, pattern)
# equal [n for n in names if fnmatch(n, pattern)]
print('Matches', matches)
