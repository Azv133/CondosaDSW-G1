from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

from models.cargo import Cargo

cargo_routes = Blueprint("cargo_routes", __name__)

@cargo_routes.route('/cargo', methods=['GET'])
def getCargos():
    if request.method == 'GET':
        cargos = Cargo.query.all()
        cargos_json = jsonify([cargo.serialize() for cargo in cargos])
        return cargos_json
