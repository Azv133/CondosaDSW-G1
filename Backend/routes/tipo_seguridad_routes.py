from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

from models.tipo_seguridad import TipoSeguridad

tipo_seguridad_routes = Blueprint("tipo_seguridad_routes", __name__)

@tipo_seguridad_routes.route('/tipoSeguridad', methods=['GET'])
def getTiposSeguridad():
    if request.method == 'GET':
        tipos_seguridad = TipoSeguridad.query.all()
        tipos_seguridad_json = jsonify([tipo_seguridad.serialize() for tipo_seguridad in tipos_seguridad])
        return tipos_seguridad_json
