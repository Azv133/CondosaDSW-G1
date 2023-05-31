from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

from models.provincia import Provincia

provincia_routes = Blueprint("provincia_routes", __name__)

@provincia_routes.route('/provincia', methods=['GET'])
def getProvincias():
    if request.method == 'GET':
        provincias = Provincia.query.all()
        provincias_json = jsonify([provincia.serialize() for provincia in provincias])
        return provincias_json

@provincia_routes.route('/provincia/<string:id_depar>', methods = ['GET'])
def getProvinciasDep(id_depar):
    if request.method == 'GET':
        provincias = Provincia.query.filter_by(id_depar = id_depar).all()
        provincias_json = jsonify([provincia.serialize() for provincia in provincias])
        return provincias_json