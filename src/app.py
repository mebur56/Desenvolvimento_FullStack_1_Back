import db
import validators
import pydanticModels
import json
from flask import request, Response
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

info = Info(title="API de Agendamentos", version="1.0.0", description="API para gerenciar agendamentos")
app = OpenAPI(
    __name__,
    info=info,
    servers=[]   
)
CORS(app)
db.init_db()

schedule_tag = Tag(name="Agenda", description="Operações relacionadas a agendamentos")


@app.get(
    "/schedules",
    tags=[schedule_tag],
    responses={
        200: pydanticModels.ScheduleListResponse,
        404: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)
def get_schedule():
    """Retorna todos os agendamentos cadastrados."""
    try:
        schedules = db.get_all_schedules()
        if not schedules:
            return Response(
                json.dumps({"message": "Nenhum agendamento encontrado"}, ensure_ascii=False),
                status=404,
                mimetype="application/json"
            )
        return Response(
            json.dumps(schedules, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao buscar agendamentos: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )


@app.post(
    "/schedule",
    tags=[schedule_tag],
    responses={
        201: pydanticModels.DefaultResponse,
        400: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)
def create_schedule(body: pydanticModels.ScheduleInput):
    """Cria um agendamento."""
    try:
        schedule = request.get_json()
        valid, message = validators.valid_schedule(schedule)
        if not valid:
            return Response(
                json.dumps({"message": message}, ensure_ascii=False),
                status=400,
                mimetype="application/json"
            )
        db.create_schedule(schedule)
        return Response(
            json.dumps({"message": "Agendamento criado!"}, ensure_ascii=False),
            status=201,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao criar agendamento: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )


@app.put(
    "/schedule",
    tags=[schedule_tag],
    responses={
        200: pydanticModels.DefaultResponse,
        400: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)
def edit_schedule(body: pydanticModels.ScheduleInput):
    """Edita um agendamento."""
    try:
        schedule = request.get_json()
        valid, message = validators.valid_schedule(schedule)
        if not valid:
            return Response(
                json.dumps({"message": message}, ensure_ascii=False),
                status=400,
                mimetype="application/json"
            )
        db.edit_schedule(schedule)
        return Response(
            json.dumps({"message": "Agendamento editado!"}, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao editar agendamento: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )


@app.delete(
    "/schedule",
    tags=[schedule_tag],
    responses={
        200: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)

def delete_schedule(query: pydanticModels.ScheduleIdQuery):
    """Remove um agendamento pelo ID."""
    try:
        db.delete_schedule(query.id)
        return Response(
            json.dumps({"message": "Agendamento removido com sucesso"}, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao remover agendamento: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
