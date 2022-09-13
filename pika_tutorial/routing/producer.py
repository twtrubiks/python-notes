import time
import pika
import random
from mq_connection import connection, channel

channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

severity = ("info", "warning", "error")
for i in range(10):
    log_type = random.choices(severity)[0]
    channel.basic_publish(
        exchange="direct_logs",
        routing_key=log_type,
        body=f"Hello World! {i} {log_type}",
    )
    time.sleep(1)

connection.close()
