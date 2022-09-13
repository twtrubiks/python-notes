from mq_connection import connection, channel

channel.queue_declare(queue="task_queue", durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# two dispatching
# Round-robin dispatching
channel.basic_qos(prefetch_count=1) # -> Fair dispatch

channel.basic_consume(
    queue="task_queue",
    #   auto_ack=True, # Message acknowledgment
    on_message_callback=callback,
)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
