import redis

r = redis.Redis(host="localhost", port=6379, db=0)

"""
https://redis.io/commands/msetnx/

Sets the given keys to their respective values.
MSETNX will not perform any operation at all even
if just a single key already exists.

MSETNX is atomic, so all given keys are set at once.
It is not possible for clients to see that some of the keys were updated
while others are unchanged.
"""

print(r.msetnx({"a1": "2"}))
print(r.get("a1"))

print(r.msetnx({"a1": "1", "a2": "2"}))
print(r.get("a1"))
print(r.get("a2"))
