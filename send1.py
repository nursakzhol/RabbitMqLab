import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='example1')
message = ' '.join(sys.argv[1:]) or "hello world..."
channel.basic_publish(exchange='', routing_key='example1', body=message)
print("Sent 'Hello World!'")
connection.close()