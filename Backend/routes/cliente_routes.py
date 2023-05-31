from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import jsonify
from models.cliente import Cliente

cliente_routes = Blueprint("cliente_routes", __name__)

@cliente_routes.route('/cliente', methods=['GET'])
def getClientes():
    if request.method == 'GET':
        clientes = Cliente.query.all()
        clientes_json = jsonify([cliente.serialize() for cliente in clientes])
        return clientes_json
