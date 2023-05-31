from flask import Blueprint, jsonify, request

from models.tipo_predio import TipoPredio

tipo_predio_routes = Blueprint("tipo_predio_routes", __name__)

@tipo_predio_routes.route('/tipoPredio', methods=['GET'])
def getTiposPredio():
    if request.method == 'GET':
        tipos_predio = TipoPredio.query.all()
        tipos_predio_json = jsonify([tipo_predio.serialize() for tipo_predio in tipos_predio])

        return tipos_predio_json
