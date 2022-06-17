# ref
# https://redis.io/commands/blpop/
# b -> block

import time
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)

while 1:
    time.sleep(0.5)
    print(redis_client.brpop("mq"), timeout=0)
