import redis

# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# redis-cli --raw
r = redis.Redis(host="localhost", port=6379, db=0)
r.set("foo", "bar")
print(r.get("foo"))
print(r.exists("foo"))
print(r.exists("foo1"))
print(r.strlen("foo"))  # value len
print(r.delete("foo1"))

# setnx = "SET if Not eXists"
print(r.setnx("foo2", "3")) # -> True
print(r.get("foo2")) # -> 3
print(r.setnx("foo", "3")) # -> False
print(r.get("foo2")) # -> bar

r.incr("users")
print(r.get("users"))
r.incrby("users", 2)
print(r.get("users"))
r.decrby("users", 2)
print(r.get("users"))
