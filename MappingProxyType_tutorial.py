# ref.
# https://docs.python.org/3/library/types.html#types.MappingProxyType

####
# class types.MappingProxyType(mapping)¶
#    Read-only proxy of a mapping.
#     It provides a dynamic view on the mapping’s entries,
#     which means that when the mapping changes, the view reflects these changes.
###

from types import MappingProxyType

d = {'a': 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)      # mappingproxy({a: 'A'})
print(d_proxy['a']) # 'A'

# d_proxy['b'] = 'B'
# # Exception has occurred: TypeError
# #'mappingproxy' object does not support item assignment

d['b'] = 'B'
print(d)            # {'a': 'A', 'b': 'B'}
print(d_proxy)      # {'a': 'A', 'b': 'B'}
print(d_proxy['b']) # B

