from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

from models.estado_solicitud import EstadoSolicitud

estado_solicitud_routes = Blueprint("estado_solicitud_routes", __name__)

@estado_solicitud_routes.route('/estadoSolicitud', methods=['GET'])
def getEstadosSolicitud():
    if request.method == 'GET':
        estados_solicitud = EstadoSolicitud.query.all()
        estados_solicitud_json = jsonify([estado.serialize() for estado in estados_solicitud])
        return estados_solicitud_json
