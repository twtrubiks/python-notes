from mq_connection import connection, channel

# RabbitMQ 4.x 起不允許非 durable 且非 exclusive 的 queue, 所以要加上 durable=True
channel.queue_declare(queue="hello", durable=True)
channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")
connection.close()
