from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

from models.personal import Personal

personal_routes = Blueprint("personal_routes", __name__)

@personal_routes.route('/personal', methods=['GET'])
def getPersonal():
    if request.method == 'GET':
        personal = Personal.query.all()
        personal_json = jsonify([persona.serialize() for persona in personal])
        return personal_json
