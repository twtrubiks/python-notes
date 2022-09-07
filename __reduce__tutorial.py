"""
ref.
https://docs.python.org/3/library/pickle.html#object.__reduce__
"""

import pickle
import os

class A:
    def __reduce__(self):
        return os.system, ("ls",)

payload = pickle.dumps(A())
pickle.loads(payload)
