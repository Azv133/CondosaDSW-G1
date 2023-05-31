from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from models.area_comun import AreaComun

area_comun_routes = Blueprint("area_comun_routes", __name__)

@area_comun_routes.route('/areaComun', methods=['GET'])
def getAreaComun():
    if request.method == 'GET':
        areas_comunes = AreaComun.query.all()
        areas_comunes_json = jsonify([area_comun.serialize() for area_comun in areas_comunes])
        return areas_comunes_json