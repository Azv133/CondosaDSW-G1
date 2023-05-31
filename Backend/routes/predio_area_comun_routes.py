from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from flask import jsonify

from models.predio_area_comun import PredioAreaComun

predio_area_comun_routes = Blueprint("predio_area_comun_routes", __name__)

@predio_area_comun_routes.route('/predioAreaComun', methods=['GET'])
def getPrediosAreaComun():
    if request.method == 'GET':
        predios_area_comun = PredioAreaComun.query.all()
        predios_area_comun_json = jsonify([predio.serialize() for predio in predios_area_comun])
        return predios_area_comun_json

@predio_area_comun_routes.route('/predioAreaComun', methods=['POST'])
def createPredioAreaComun():
    if request.method == 'POST':
        id_area_c = request.json.get('id_area_c') 
        id_predio = request.json.get('id_predio') 
        area = request.json.get('area') 

        nuevo_predio_area_comun = PredioAreaComun(id_area_c, id_predio, area)

        db.session.add(nuevo_predio_area_comun)
        db.session.commit()

        return jsonify(nuevo_predio_area_comun.serialize())