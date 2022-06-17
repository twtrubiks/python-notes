import redis
import time

client = redis.Redis(host="localhost", port=6379, db=0)
client.set("test", "123", ex=3)
print(client.ttl("test"))
time.sleep(1)
print(client.get("test"))
print(client.ttl("test"))
time.sleep(3)
print(client.get("test"))
