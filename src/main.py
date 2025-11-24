import db
import validators
import json
from flask import request, Response, Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db.init_db()

@app.route("/schedules", methods=['GET'])
def get_schedule():
    schedules = db.get_all_schedules()
    try:
        if len(schedules) <= 0:
            return Response(
                json.dumps({"message": "Nenhum agendamento encontrado"}, ensure_ascii=False),
                mimetype="application/json",
                status=404
            )
        
        return Response(
                json.dumps(schedules, ensure_ascii=False),
                mimetype="application/json",
                status=200
            )
    except Exception as e:
          return Response(
                json.dumps({"message":"Erro ao buscar agendamentos: " + str(e)}, ensure_ascii=False),
                mimetype="application/json",
                status=500
            )

@app.route("/schedule", methods=['POST'])
def create_schedule():
    try:
        schedule = request.get_json()
        valid, message = validators.valid_schedule(schedule)
        if(valid == False):
            return Response(
                json.dumps({"message": message}, ensure_ascii=False),
                mimetype="application/json",
                status=400
            )
        db.create_schedule(schedule)   

        return Response(
            json.dumps({"message":"Agendamento criado!"}, ensure_ascii=False),
            mimetype="application/json",
            status=201
        )
    except Exception as e:
          return Response(
                json.dumps({"message":"Erro ao criar agendamento: " + str(e)}, ensure_ascii=False),
                mimetype="application/json",
                status=500
            )
@app.route("/schedule", methods=['PUT'])
def edit_schedule():
    try:
        schedule = request.get_json()
        valid, message = validators.valid_schedule(schedule)
        if(valid == False):
            return Response(
                json.dumps({"message": message}, ensure_ascii=False),
                mimetype="application/json",
                status=400
            )
        db.edit_schedule(schedule)   

        return Response(
            json.dumps({"message":"Agendamento criado!"}, ensure_ascii=False),
            mimetype="application/json",
            status=201
        )
    except Exception as e:
        return Response(
                json.dumps({"message":"Erro ao editar agendamento: " + str(e)}, ensure_ascii=False),
                mimetype="application/json",
                status=500)

@app.route("/schedule/<int:id>", methods = ['DELETE'])
def delete_schedule(id):
    try:
        db.delete_schedule(id)
        return Response(
            json.dumps({"message":"Agendamento removido com sucesso"}, ensure_ascii=False),
            mimetype="application/json",
            status=200
        )  
    except Exception as e:
        return Response(
            json.dumps({"message":"Erro ao remover agendamentos: " + str(e)}, ensure_ascii=False),
            mimetype="application/json",
            status=500 
        )       

if __name__ == "__main__":
    app.run(debug=True)