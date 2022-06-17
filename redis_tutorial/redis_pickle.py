import redis
import pickle

# user pickle -> decode_responses=False
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=False)


class Stock:
    def __init__(self, num, date):
        self.num = num
        self.date = date


def set_pickled():
    s_obj = Stock("xxxx", "10/02")
    pickled_object = pickle.dumps(s_obj)
    redis_client.set("test_pickle", pickled_object)


def get_pickled():
    data = pickle.loads(redis_client.get("test_pickle"))
    print(data)


set_pickled()
get_pickled()
