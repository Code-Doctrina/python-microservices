# amqps://ybrodeav:Y_cMaeJOL3n1ZShcpXMGKEWKFUSXrbLW@rattlesnake.rmq.cloudamqp.com/ybrodeav
import pika 

params = pika.URLParameters('amqps://ybrodeav:Y_cMaeJOL3n1ZShcpXMGKEWKFUSXrbLW@rattlesnake.rmq.cloudamqp.com/ybrodeav')
connection  = pika.BlockingConnection(params)
channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello main')