import time
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

count = 0
while 1:
    time.sleep(0.3)
    count += 1
    redis_client.lpush("mq", count)
