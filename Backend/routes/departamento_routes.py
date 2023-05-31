from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

from models.departamento import Departamento

departamento_routes = Blueprint("departamento_routes", __name__)

@departamento_routes.route('/departamento', methods=['GET'])
def getDepartamentos():
    if request.method == 'GET':
        departamentos = Departamento.query.all()
        departamentos_json = jsonify([departamento.serialize() for departamento in departamentos])
        return departamentos_json
