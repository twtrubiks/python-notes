import redis

# like python dict

client = redis.Redis(host="localhost", port=6379)

# hset: Set key to value with hash name
client.hset("myhash", "field_1", "foo")

hash_val = client.hget("myhash", "field_1")
# redis-cli -> hget "myhash" field_1
print("Get hash value:", hash_val)

for key in ["field_1", "field_2"]:
    hexists = client.hexists("myhash", key)
    if hexists:
        print("Exist in redis-hash key:", key)
    else:
        print("Not exist in redis-hash key:", key)

# hgetall: Return a Python dict of the hash's name/value pairs
client.hset("myhash", "field_2", "bar")
val_dict = client.hgetall("myhash")
print("Get python-dict from redis-hash", val_dict)

# hincrby: Increment the value of ``key`` in hash ``name`` by ``amount``
# default increment is 1,
client.hset("myhash", "field_3", 20)
client.hincrby("myhash", "field_3")
print("Get incrby value(Default):", client.hget("myhash", "field_3"))
client.hincrby("myhash", "field_3", -3)
print("Get incrby value(step: -3):", client.hget("myhash", "field_3"))

# hkeys: Return the list of keys within hash ``name``
h_key = client.hkeys("myhash")
print("Get redis-hash key list", h_key)

# hlen: Return the number of elements in hash ``name``
h_len = client.hlen("myhash")
print("All hash length:", h_len)

# hmset
client.hmset("myhash", {"field_4": "444", "field_5": "555"})

# hmget: Returns a list of values ordered identically to ``keys``
# hmget(self, name, keys), keys should be python list data structure
val = client.hmget("myhash", ["field_1", "field_2", "field_3", "field_4", "field_5"])
print("Get all redis-hash value list:", val)

# hdel: Delete ``key`` from hash ``name``
client.hdel("hash", "field_1")
print("Get delete result:", client.hget("hash", "field_1"))

# hvals:  Return the list of values within hash ``name``
val = client.hvals("myhash")
print("Get redis-hash values with HVALS", val)

# hsetnx: Set ``key`` to ``value`` within hash ``name`` if ``key`` does not exist.
# Returns 1 if HSETNX created a field, otherwise 0.
r = client.hsetnx("myhash", "field_5", 2)
print("Check hsetnx execute result:", r, " Value:", client.hget("myhash", "field"))
