from api import app
from api import db
from flask import Response, request
import json

@app.route("/registro", methods=['GET']) #rota get
def get_registros():
    try:
        registros_list = list(db.registros.find({}))
        for i in registros_list:
            del i['_id']
        return json.dumps(registros_list)
    except Exception as ex:
        print(ex)
        return Response(response="Erro.", status=500)



@app.route("/registro/create", methods=['POST']) #rota post
def post_registro():
    try:
        novo_registro = request.json
        db.registros.insert_one(novo_registro)
        return Response(response="Registro adicionado.", status=200)
    except Exception as ex:
        print(ex)
        return Response(response="Erro.", status=500)



@app.route("/registro/update/<idx>/<stat>", methods=['PUT']) #rota put
def put_registro(idx, stat):
    try:
        db.registros.update_one({"msgIndex":int(idx)}, {"$set": {"status":stat}})
        return Response(response="Status atualizado. ID: "+idx+"- status da operação: "+stat, status=200)
    except Exception as ex:
        print(ex)
        return Response(response="Erro.", status=500)