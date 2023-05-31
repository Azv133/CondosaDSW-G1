from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

from models.distrito import Distrito

distrito_routes = Blueprint("distrito_routes", __name__)

@distrito_routes.route('/distrito', methods=['GET'])
def getDistritos():
    if request.method == 'GET':
        distritos = Distrito.query.all()
        distritos_json = jsonify([distrito.serialize() for distrito in distritos])
        return distritos_json

@distrito_routes.route('/distrito/<string:id_provin>/<string:id_depar>', methods = ['GET'])
def getProvinciasDep(id_provin, id_depar):
    if request.method == 'GET':
        distritos = Distrito.query.filter_by(id_provin = id_provin, id_depar = id_depar).all()
        distritos_json = jsonify([distrito.serialize() for distrito in distritos])
        return distritos_json
