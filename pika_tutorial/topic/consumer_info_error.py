import time
import pika
from mq_connection import connection, channel

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
severities = ("*.info", "*.error")

for severity in severities:
    channel.queue_bind(exchange="topic_logs", queue=queue_name, routing_key=severity)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

connection.close()
