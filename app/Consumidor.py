import pika
import json
from main import MainExtrator

#instancia a classe MainExtrator
mainExtrator = MainExtrator()

#Conexao
credentials = pika.PlainCredentials(username="guest", password="guest")
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))

channel = connection.channel()

queue = channel.queue_declare('frames_msg')
queue_name = queue.method.queue

channel.queue_bind(exchange='frame_info', queue=queue_name, routing_key='frame_info_msg')


def callback(ch, method, properties, body):
    msg = json.loads(body) #recebe as mensagens
    print("Mensagem recebida. ID: ", msg["msgIndex"])
    mainExtrator.setATRIB(idx=msg["msgIndex"], video_ref=msg["video_ref"], frame_seconds_index=msg["frame_seconds_index"], op_type=msg["op_type"]) #executa operacoes
    mainExtrator.executarExtrator()
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(on_message_callback=callback, queue=queue_name)
print('Esperando mensagens.')

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()