import time
import pika
from mq_connection import connection, channel

channel.exchange_declare(exchange="logs", exchange_type="fanout")

for i in range(10):
    channel.basic_publish(
        exchange="logs",
        routing_key="",
        body=f"Hello World! {i}",
    )
    time.sleep(1)

connection.close()
