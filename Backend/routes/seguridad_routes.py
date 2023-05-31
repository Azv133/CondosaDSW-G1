from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from utils.db import db

from models.seguridad import Seguridad

seguridad_routes = Blueprint("seguridad_routes", __name__)

@seguridad_routes.route('/seguridad', methods=['GET'])
def getSeguridad():
    if request.method == 'GET':
        seguridad = Seguridad.query.all()
        seguridad_json = jsonify([seg.serialize() for seg in seguridad])
        return seguridad_json

@seguridad_routes.route('/seguridad', methods=['POST'])
def createSeguridad():
    if request.method == 'POST':
        nombre_seguridad = request.json.get('nombre_seguridad') 
        tipo_seguridad = request.json.get('tipo_seguridad')

        nueva_seguridad = Seguridad(nombre_seguridad, tipo_seguridad)

        db.session.add(nueva_seguridad)
        db.session.commit()

        return jsonify(nueva_seguridad.serialize())