import time
import pika
import random
from mq_connection import connection, channel

channel.exchange_declare(exchange="topic_logs", exchange_type="topic")

severity = (
    "1.info",
    "2.warning",
    "3.error",
    "4.info",
    "5.warning",
    "6.error",
    "error.7",
)

for routing_key in severity:
    channel.basic_publish(
        exchange="topic_logs",
        routing_key=routing_key,
        body=f"Hello World! {routing_key}",
    )
    time.sleep(1)

connection.close()
