import redis

client = redis.Redis(host="localhost", port=6379)


def example_1():
    pubsub = client.pubsub()
    pubsub.subscribe("channel-1")

    # use pattern subscribe
    pubsub.psubscribe("channel-*")

    print(pubsub.get_message())
    print(pubsub.get_message())

    print(client.publish("channel-1", "value-1"))
    print(pubsub.get_message())
    print(pubsub.get_message())

    print("unsubscribe")
    pubsub.unsubscribe("my")
    pubsub.punsubscribe("my-*")
    print(pubsub.get_message())
    print(pubsub.get_message())
    pubsub.close()


def my_handler(message):
    print("MY HANDLER: ", message["data"])


def example_2():
    pubsub = client.pubsub(ignore_subscribe_messages=False)
    pubsub.subscribe(**{"my-channel": my_handler})
    print(pubsub.get_message())
    client.publish("my-channel", "awesome data")
    pubsub.get_message()
    pubsub.get_message()
    pubsub.close()


# 可搭配 redis-cli MONITOR 觀察

example_1()
# example_2()
