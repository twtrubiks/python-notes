from mq_connection import connection, channel

channel.queue_declare(queue="hello")
channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello World!'")
connection.close()
