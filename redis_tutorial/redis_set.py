import redis

client = redis.Redis(host="localhost", port=6379, db=0)
client.sadd("test-set", 1, 1, 2, 2, 4, 3)

print(client.smembers("test-set"))

client.sadd("test-set", 3, 5)
print(client.smembers("test-set"))
print(client.scard("test-set"))

# remove
client.srem("test-set", 3)
print(client.smembers("test-set"))
print(client.scard("test-set"))

# if 2 in test-set
print(client.sismember("test-set", 2))
# if 3 in test-set
print(client.sismember("test-set", 3))

# random pop (remove from set)
print(client.spop("test-set"))
print(client.smembers("test-set"))
# random picked (not remove from set)
print(client.srandmember("test-set"), 2)
print(client.smembers("test-set"))

client.sadd("user:1", 1, 2, 3, 4)
client.sadd("user:2", 3, 4)

# 共同擁有的
print(client.sinter("user:1", "user:2"))
# 第一個集合和其他集合的差異
print(client.sdiff("user:1", "user:2"))
