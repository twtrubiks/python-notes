import redis

client = redis.Redis(host="localhost", port=6379)
client.publish("room", "hello")
