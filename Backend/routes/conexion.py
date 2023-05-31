from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify

conexion = Blueprint("conexion", __name__)

@conexion.route('/')
def index():
    return {'mensaje':"Que haces por acá o.o"}
