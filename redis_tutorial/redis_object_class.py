import json
import redis

redis_client = redis.Redis(host="localhost", port=6379, db=0)


class User:
    def __init__(self, name):
        self.name = name


class Stock:
    def __init__(self, num, user, push_date):
        self.num = num
        self.user = user
        self.push_date = push_date


def init():
    # create object
    user = User("twtrubiks")
    stock = Stock("2222", user, ["5/3"])
    return stock


def save_obj_to_redis(stock):
    # convert to JSON string
    json_str = json.dumps(stock, default=lambda o: o.__dict__)
    print(json_str)
    redis_client.set("my_obj", json_str)


def get_obj_from_redis():
    json_str = json.loads(redis_client.get("my_obj"))
    stock_obj = Stock(**json_str)
    print(stock_obj)
    return stock_obj


def update_obj(stock):
    stock.push_date.append("5/5")


def test_update_stock_obj():
    stock = get_obj_from_redis()
    update_obj(stock)
    save_obj_to_redis(stock)
    stock_obj = get_obj_from_redis()
    print(stock_obj.push_date)
    # ['5/3', '5/5']


stock = init()
stocksave_obj_to_redis(stock)
get_obj_from_redis()

# test_update_stock_obj()
