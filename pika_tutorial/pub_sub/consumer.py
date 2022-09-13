import time
import pika
from mq_connection import connection, channel

channel.exchange_declare(exchange="logs", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="logs", queue=queue_name)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

connection.close()
