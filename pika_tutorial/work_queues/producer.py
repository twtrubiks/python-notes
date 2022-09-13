import time
import pika
from mq_connection import connection, channel

channel.queue_declare(queue="task_queue", durable=True)

for i in range(30):
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=f"Hello World! {i}",
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ),
    )
    print(" [x] Sent 'Hello World!'")
    time.sleep(0.1)
connection.close()
