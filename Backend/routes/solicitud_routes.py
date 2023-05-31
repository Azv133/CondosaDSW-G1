from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from utils.db import db

from models.solicitud import Solicitud

solicitud_routes = Blueprint("solicitud_routes", __name__)

@solicitud_routes.route('/solicitud', methods=['GET'])
def getSolicitudes():
    if request.method == 'GET':
        solicitudes = Solicitud.query.all()
        solicitudes_json = jsonify([solicitud.serialize() for solicitud in solicitudes])
        return solicitudes_json
    
@solicitud_routes.route('/solicitud', methods=['POST'])
def createSolicitud():
    if request.method == 'POST':
        id_cliente = request.json.get('id_cliente')
        id_predio = request.json.get('id_predio')
        fecha = request.json.get('fecha')
        estado = request.json.get('estado')
        descripcion = request.json.get('descripcion')

        nueva_solicitud = Solicitud(id_cliente, id_predio, fecha, estado, descripcion)

        db.session.add(nueva_solicitud)
        db.session.commit()

        return jsonify(nueva_solicitud.serialize())
