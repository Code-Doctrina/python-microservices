# amqps://ybrodeav:Y_cMaeJOL3n1ZShcpXMGKEWKFUSXrbLW@rattlesnake.rmq.cloudamqp.com/ybrodeav
import pika, json

params = pika.URLParameters('amqps://ybrodeav:Y_cMaeJOL3n1ZShcpXMGKEWKFUSXrbLW@rattlesnake.rmq.cloudamqp.com/ybrodeav')
connection  = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body),properties=properties)