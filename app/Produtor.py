import os
import json
import pika


#Abrir o arquivo json
fp = open(os.path.join(os.pardir, "data\\payload.json"))
 
#Transforma json em dicionario
data = json.load(fp) #O dicionario contem todas as mensagens que devem ser enviadas, ordenado conforme o arquivo inicial.
 
#Fechar o arquivo
fp.close()

#Cria a conexão
credentials = pika.PlainCredentials(username="guest", password="guest")
connection = pika.BlockingConnection(parameters=pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='frame_info', exchange_type='direct')

#Variavel para identificacao da mensagem
msgIndex=1

for i in data: #publica todas mensagens
    i["msgIndex"] = msgIndex
    channel.basic_publish(exchange='frame_info', routing_key='frame_info_msg', body=json.dumps(i))
    print("Mensagem enviada. ID: ",msgIndex)
    msgIndex+=1

#Fecha a conexão
connection.close()