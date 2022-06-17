import redis

r = redis.Redis(host="localhost", port=6379, db=0)

# Atomic operations can be used when all keys are mapped to the same slot
r.mset({"boo1": "bar1", "boo2": "bar2"})
print(r.mget("boo1", "boo2"))
