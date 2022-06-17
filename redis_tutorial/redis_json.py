import redis
import json

redis_client = redis.Redis(host="localhost", port=6379)

my_dict = [
    {"type": "a1", "value": "v1"},
    {"type": "a2", "value": "v2"},
    {"type": "a3", "value": "v3"},
]

json_my_dict = json.dumps(my_dict)
redis_client.set("myjson", json_my_dict)

data = json.loads(redis_client.get("myjson"))
print(data)
