import redis

client = redis.Redis(host="localhost", port=6379, db=0)

client.zadd("test-sorted-set", {"John": 111, "alan": 333})
client.zadd("test-sorted-set", {"ian": 433})

print(client.zrange("test-sorted-set", 0, -1, withscores=True))
print(client.zrevrange("test-sorted-set", 0, -1, withscores=True))

print(client.zrangebyscore("test-sorted-set", 100, 350, withscores=True))

client.zincrby("test-sorted-set", 2, "david")
print(client.zscore("test-sorted-set", "david"))

print(client.zrangebyscore("test-sorted-set", 1, 350, withscores=True))

client.zadd(
    "phone-set",
    {
        "1230000000": 0,
        "1220000000": 0,
        "1220000002": 0,
        "1240000000": 0,
        "1200000000": 0,
        "1220000001": 0,
        "1190000000": 0,
        "1180000002": 0,
        "1290000000": 0,
    },
)
print(client.zrangebylex("phone-set", "-", "+"))
# get all 122xxxxxxx
print(client.zrangebylex("phone-set", "[122", "(123"))
# 119xxxxxxx ~ 120xxxxxxx
print(client.zrangebylex("phone-set", "[119", "(121"))
# 118xxxxxxx ~ 119xxxxxxx
print(client.zrangebylex("phone-set", "[118", "(119"))

client.zadd("my-sorted-set", {"a": 0, "c": 0, "b": 0, "d": 0, "e": 0, "f": 0})
print(client.zrangebylex("my-sorted-set", "-", "[c"))  # "[" inclusive
print(client.zrangebylex("my-sorted-set", "-", "(c"))  # "(" exclusive
