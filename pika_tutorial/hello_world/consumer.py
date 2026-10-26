from mq_connection import connection, channel

# RabbitMQ 4.x 起不允許非 durable 且非 exclusive 的 queue, 所以要加上 durable=True
channel.queue_declare(queue="hello", durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
