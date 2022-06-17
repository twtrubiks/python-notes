import redis

client = redis.Redis(host="localhost", port=6379)
pipeline = client.pipeline()

pipeline.set("key1", "value1")
pipeline.set("key2", "value2")

print(pipeline.execute())

print(pipeline.set("foo1", "bar1").sadd("faz1", "baz1").incr("auto_number").execute())
