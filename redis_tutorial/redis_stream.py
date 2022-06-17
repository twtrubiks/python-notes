import redis

# ref
# https://redis.io/docs/manual/data-types/streams/

redis_client = redis.Redis(host="localhost", port=6379, db=0)


def example_1():
    redis_client.delete("my-test-stream")

    # redis-cli -> XADD my-test-stream * sensor-id 1234
    print(redis_client.xadd("my-test-stream", {"sensor-id": 1234}, maxlen=1000))
    print(redis_client.xadd("my-test-stream", {"sensor-id": 2234}))
    print(redis_client.xinfo_stream("my-test-stream"))
    # -> <millisecondsTime>-<sequenceNumber>
    print(redis_client.xlen("my-test-stream"))

    # redis-cli -> XRANGE my-test-stream - +
    print(redis_client.xrange("my-test-stream", min="-", max="+"))
    print(redis_client.xrange("my-test-stream", min="-", max="+", count=2))
    # "(" -> exclusive
    print(redis_client.xrange("my-test-stream", min="(1655435115399-0", max="+"))

    # redis-cli -> XREAD COUNT 3 STREAMS my-test-stream 0
    print(redis_client.xread({"my-test-stream": "0"}, count=3))
    print(redis_client.xread({"my-test-stream": "1695435115399-0"}))

    # $. This special ID means that XREAD should use as last ID the maximum ID already stored in the stream
    # redis-cli -> XREAD BLOCK 0 STREAMS my-test-stream $
    # BLOCK option with a timeout of 0 milliseconds
    print(redis_client.xread({"my-test-stream": "$"}, block=0))


def example_2():

    redis_client.delete("my-test-stream")
    # redis_client.xgroup_delconsumer("my-test-stream", "mygroup2", "consumer1")
    # redis_client.xgroup_destroy("my-test-stream", "mygroup2")

    my_stream_1 = redis_client.xadd("my-test-stream", {"sensor-id": 1234})
    my_stream_2 = redis_client.xadd("my-test-stream", {"sensor-id": 2234})

    # $ -> $ means the current greatest ID in the stream, specifying $ will have the effect of consuming only new messages
    # redis-cli -> XGROUP CREATE my-test-stream mygroup $
    # 0 -> If we specify 0 instead the consumer group will consume all the messages in the stream history to start with
    # redis-cli -> XGROUP CREATE my-test-stream mygroup 0

    # redis-cli -> XGROUP CREATE my-test-stream mygroup $
    redis_client.xgroup_create("my-test-stream", "mygroup1", id="0")
    redis_client.xgroup_create("my-test-stream", "mygroup2", id="0")

    # redis-cli -> XREADGROUP GROUP group1 consumer1 COUNT 5 STREAMS my-test-stream >
    # If the ID is the special ID > then the command will return only new messages never delivered to other consumers so far, and as a side effect, will update the consumer group's last ID.
    print(redis_client.xreadgroup("mygroup1", "consumer1", {"my-test-stream": ">"}))
    print(redis_client.xreadgroup("mygroup2", "consumer1", {"my-test-stream": ">"}))

    # redis-cli -> XACK my-test-stream mygroup1 1526569495631-0
    print("XACK my-test-stream mygroup1:", my_stream_1)
    redis_client.xack("my-test-stream", "mygroup1", my_stream_1)

    print(redis_client.xreadgroup("mygroup1", "consumer1", {"my-test-stream": "0"}))
    print(redis_client.xreadgroup("mygroup2", "consumer1", {"my-test-stream": "0"}))

    print(redis_client.xpending("my-test-stream", "mygroup1"))
    print(redis_client.xpending("my-test-stream", "mygroup2"))


example_1()
# example_2()
