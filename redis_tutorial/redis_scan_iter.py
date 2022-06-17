import redis

client = redis.Redis(host="localhost", port=6379)
client.set("foo", "bar")
client.set("foo1", "bar1")
client.set("foo2", "bar2")
client.set("fo2o2", "bar2")

for key in client.scan_iter("foo*"):
    print(client.get(key))
