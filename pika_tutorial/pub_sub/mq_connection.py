"""
ref
https://www.rabbitmq.com/tutorials/tutorial-three-python.html

Publish/Subscribe

Sending messages to many consumers at once
"""

import pika


RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = "5672"
RABBITMQ_USER = "admin"
RABBITMQ_PASS = "admin"

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
parameters = pika.ConnectionParameters(
    host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials
)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
