import time
import pika
import random
from mq_connection import connection, channel

# RabbitMQ 4.x 起不允許非 durable 且非 exclusive 的 queue, 所以要加上 durable=True
channel.queue_declare(queue="rpc_queue", durable=True)


def fib(n):
    time.sleep(n)
    return n


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
connection.close()
