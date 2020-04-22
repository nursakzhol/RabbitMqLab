import pika
import time

def callback(ch, method, properites, body):
    print("Received: {}".format(body))
    time.sleep(body.count(b'.')) #message .... 4
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='example1')

channel.basic_consume(queue='example1',
                      on_message_callback=callback)

channel.start_consuming()