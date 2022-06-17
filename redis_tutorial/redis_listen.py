import redis

client = redis.Redis(host="localhost", port=6379)

p = client.pubsub()
p.subscribe("room")
for message in p.listen():
    print(message.get("data"))
