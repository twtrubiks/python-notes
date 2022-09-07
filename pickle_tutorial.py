"""
The pickle module implements binary protocols for serializing and de-serializing a Python object structure.

https://docs.python.org/3/library/pickle.html

Warning

The pickle module is not secure. Only unpickle data you trust.

It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Never unpickle data that could have come from an untrusted source, or that could have been tampered with.

Consider signing data with hmac if you need to ensure that it has not been tampered with.

Safer serialization formats such as json may be more appropriate if you are processing untrusted data. See Comparison with json.

"""

import pickle

'''
Advantages

1.Helps in saving complicated data.
2.Quite easy to use, doesn't require several lines of code and hence not bulky.
3.Saved data is not so readable hence provides some data security.

Disadvantages

1.Non-Python programs may not be able to reconstruct pickled Python objects.
2.Security risks in unpickling data from malicious sources.
'''

if __name__ == "__main__":
    data = {
        'a': [1, 2.0, 3, 4 + 6j],
        'b': ("character string", b"byte string"),
        'c': {None, True, False}
    }

    with open('data.pickle', 'wb') as f:
        # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    with open('data.pickle', 'rb') as f:
        # The protocol version used is detected automatically, so we do not
        # have to specify it.
        data_new = pickle.load(f)
    print('data_new:', data_new)
