from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from utils.db import db

from models.predio_seguridad import PredioSeguridad

predio_seguridad_routes = Blueprint("predio_seguridad_routes", __name__)

@predio_seguridad_routes.route('/predioSeguridad', methods=['GET'])
def getPrediosSeguridad():
    if request.method == 'GET':
        predios_seguridad = PredioSeguridad.query.all()
        predios_seguridad_json = jsonify([predio_seguridad.serialize() for predio_seguridad in predios_seguridad])
        return predios_seguridad_json
    
@predio_seguridad_routes.route('/predioSeguridad', methods=['POST'])
def createPredioSeguridad():
    if request.method == 'POST':
        id_seguridad = request.json.get('id_seguridad') 
        id_predio = request.json.get('id_predio') 
        cantidad_seguridad = request.json.get('cantidad_seguridad') 

        nuevo_predio_seguridad = PredioSeguridad(id_seguridad,id_predio, cantidad_seguridad)

        db.session.add(nuevo_predio_seguridad)
        db.session.commit()

        return jsonify(nuevo_predio_seguridad.serialize())