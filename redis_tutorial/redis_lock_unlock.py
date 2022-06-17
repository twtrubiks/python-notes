import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# redis-cl -> SET lock_key secret NX PX 10000
# NX – Only set the key if it does not already exist.
# PX milliseconds – Set the specified expire time, in milliseconds.
my_key = "my-lock-key"
print(redis_client.set(my_key, "secret", nx=True, px=10000))

if redis_client.get(my_key) == "secret":
    print("unlock")
    redis_client.delete(my_key)
else:
    print("not unlock")
