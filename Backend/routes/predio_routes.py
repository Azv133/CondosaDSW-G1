from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from utils.db import db
from models.predio import Predio

predio_routes = Blueprint("predio_routes", __name__)

@predio_routes.route('/predio', methods=['GET'])
def getPredios():
    if request.method == 'GET':
        predios = Predio.query.all()
        predios_json = jsonify([predio.serialize() for predio in predios])
        return predios_json

@predio_routes.route('/predio', methods=['POST'])
def createPredio():
    if request.method == 'POST':
        nombre = request.json.get('nombre')
        area = request.json.get('area')
        ubicacion = request.json.get('ubicacion')
        id_distrito = request.json.get('id_distrito')
        id_tipo = request.json.get('id_tipo')
        nro_casas_habitacion = request.json.get('nro_casas_habitacion')
        nro_puertas_acceso = request.json.get('nro_puertas_acceso')
        nro_torres_bloques = request.json.get('nro_torres_bloques')
        
        nuevo_predio = Predio(nombre, area, ubicacion, id_distrito, id_tipo, nro_casas_habitacion, nro_puertas_acceso, nro_torres_bloques)

        db.session.add(nuevo_predio)
        db.session.commit()

        return jsonify(nuevo_predio.serialize())