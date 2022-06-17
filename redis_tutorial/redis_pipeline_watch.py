import redis

client = redis.Redis(host="localhost", port=6379)

with client.pipeline() as pipe:
    while True:
        try:
            pipe.watch("OUR-SEQUENCE-KEY")
            current_value = pipe.get("OUR-SEQUENCE-KEY")
            pipe.multi()
            next_value = int(current_value) + 1
            pipe.set("OUR-SEQUENCE-KEY", next_value)
            pipe.execute()
            break
        except:
            print("except")
            continue
        finally:
            pipe.reset()

"""
ref. https://github.com/redis/redis-py#pipelines

run python3 redis_pipeline_watch.py -> start watch

redis-cli
127.0.0.1:6379> set OUR-SEQUENCE-KEY 0
OK

python3 redis_pipeline_watch.py -> done

127.0.0.1:6379> get OUR-SEQUENCE-KEY
"1"
"""
