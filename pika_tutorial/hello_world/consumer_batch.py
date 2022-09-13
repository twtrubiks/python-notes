from mq_connection import connection, channel
import time
import random

channel.queue_declare(queue="hello")

collection_batch_size = 2
collection = []


def batch_run(tasks):

    print("tasks length:", len(tasks))
    print(tasks, "\n")

    rand_num = random.randint(0, 2)

    if rand_num:
        print(tasks, "\n")
        time.sleep(1)
        return True
    else:
        print("failed.", "\n")
        time.sleep(1)
        return False


def batch_callback(ch, method, properties, body):

    print(f" [*] Received: {body}")

    collection.append(body)
    if len(collection) % collection_batch_size == 0:
        result = batch_run(collection)
        if result:
            ch.basic_ack(delivery_tag=method.delivery_tag, multiple=True)
        else:
            ch.basic_nack(delivery_tag=method.delivery_tag, multiple=True)
        collection.clear()


channel.basic_consume(queue="hello", on_message_callback=batch_callback)


channel.start_consuming()
