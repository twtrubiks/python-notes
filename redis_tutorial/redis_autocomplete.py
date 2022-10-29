import redis

"""
redis 實做 autocomplete
"""

client = redis.Redis(host="localhost", port=6379, db=0)

"""
範例
help
hello
hell
hex
helloween
"""

auto_index_name = "autocomplete"

def init_set_data():
    client.zadd(auto_index_name, {"hello": 0})
    client.zadd(auto_index_name, {"hello*": 0})
    client.zadd(auto_index_name, {"hell": 0})
    client.zadd(auto_index_name, {"hell*": 0})
    client.zadd(auto_index_name, {"hel": 0})
    client.zadd(auto_index_name, {"he": 0})
    client.zadd(auto_index_name, {"h": 0})
    client.zadd(auto_index_name, {"hex": 0})
    client.zadd(auto_index_name, {"hex*": 0})
    client.zadd(auto_index_name, {"help": 0})
    # client.zadd(auto_index_name, {"help*": 0})
    client.zadd(auto_index_name, {"helloween": 0})
    # client.zadd(auto_index_name, {"helloween*": 0})
    client.zadd(auto_index_name, {"hellowee": 0})
    client.zadd(auto_index_name, {"hellowe": 0})
    client.zadd(auto_index_name, {"hellow": 0})
    client.zadd(auto_index_name, {"hello ": 0})
    client.zadd(auto_index_name, {"hello w": 0})
    client.zadd(auto_index_name, {"hello wo": 0})
    client.zadd(auto_index_name, {"hello wor": 0})
    client.zadd(auto_index_name, {"hello worl": 0})
    client.zadd(auto_index_name, {"hello world": 0})
    # client.zadd(auto_index_name, {"hello world*": 0})
    client.zadd(auto_index_name, {"hello everyone": 0})
    # client.zadd(auto_index_name, {"hello everyone*": 0})
    client.zadd(auto_index_name, {"hello everyon": 0})
    client.zadd(auto_index_name, {"hello everyo": 0})
    client.zadd(auto_index_name, {"hello every": 0})
    client.zadd(auto_index_name, {"hello ever": 0})
    client.zadd(auto_index_name, {"hello eve": 0})
    client.zadd(auto_index_name, {"hello ev": 0})
    client.zadd(auto_index_name, {"hello e": 0})

def get_index(content):
    index = client.zrank(auto_index_name, content)
    if index:
        return index
    raise Exception("key {} not in redis".format(content))

def ex1():
    # 定位
    index = get_index("hell")
    print("index:", index)

    # result
    print(client.zrange(auto_index_name, index, index + 4, withscores=True))

def ex2():
    # 定位
    index = get_index("hello")
    print("index:", index)

    # result
    print(client.zrange(auto_index_name, index, index + 4, withscores=True))

def ex3():
    # 定位
    index = get_index("hello w")
    print("index:", index)

    # result
    print(client.zrange(auto_index_name, index, index + 4, withscores=True))

def ex4():
    # 定位
    index = get_index("hello e")
    print("index:", index)

    # result
    print(client.zrange(auto_index_name, index, index + 4, withscores=True))


init_set_data()

try:
    ex1()
    # ex2()
    # ex3()
    # ex4()
except Exception as e:
    print(e)


# clear redis data
# client.flushall()
