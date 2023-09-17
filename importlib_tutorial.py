"""
https://docs.python.org/3/library/importlib.html
"""

import importlib

time = importlib.import_module('time')
print(time.time())