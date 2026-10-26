from mq_connection import connection, channel
import time

# RabbitMQ 4.x 起不允許非 durable 且非 exclusive 的 queue, 所以要加上 durable=True
channel.queue_declare(queue="hello", durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


for method, properties, body in channel.consume(
    queue="hello", inactivity_timeout=3, auto_ack=True
):
    print(f" [x] Received {body}")

    if method == None and properties == None and body == None:
        break

connection.close()
