import redis

client = redis.Redis(host="localhost", port=6379, db=0)

client.rpush("mylist", "a")
client.rpush("mylist", "b")
client.rpush("mylist", "c")
client.rpush("mylist", "d")
client.rpush("mylist", "e")
client.rpush("mylist", "f", "g")

print(client.lindex("mylist", 6))
print(client.lrange("mylist", 2, 5))

"""
redis-cli

127.0.0.1:6379> LRANGE "mylist" 0 100
1) "a"
2) "b"
3) "c"
4) "d"
5) "e"
6) "f"
7) "g"
"""

while client.llen("mylist") != 0:
    print(client.rpop("mylist"))
