from flask import Flask
from routes.conexion import conexion
from routes.area_comun_routes import area_comun_routes
from routes.cargo_routes import cargo_routes
from routes.cliente_routes import cliente_routes
from routes.departamento_routes import departamento_routes
from routes.distrito_routes import distrito_routes
from routes.estado_solicitud_routes import estado_solicitud_routes
from routes.personal_routes import personal_routes
from routes.predio_area_comun_routes import predio_area_comun_routes
from routes.predio_routes import predio_routes
from routes.predio_seguridad_routes import predio_seguridad_routes
from routes.provincia_routes import provincia_routes
from routes.seguridad_routes import seguridad_routes
from routes.solicitud_routes import solicitud_routes
from routes.tipo_predio_routes import tipo_predio_routes
from routes.tipo_seguridad_routes import tipo_seguridad_routes
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'clavesecreta123'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app)

app.register_blueprint(conexion)
app.register_blueprint(area_comun_routes)
app.register_blueprint(cargo_routes)
app.register_blueprint(cliente_routes)
app.register_blueprint(departamento_routes)
app.register_blueprint(distrito_routes)
app.register_blueprint(estado_solicitud_routes)
app.register_blueprint(personal_routes)
app.register_blueprint(predio_area_comun_routes)
app.register_blueprint(predio_routes)
app.register_blueprint(predio_seguridad_routes)
app.register_blueprint(provincia_routes)
app.register_blueprint(seguridad_routes)
app.register_blueprint(solicitud_routes)
app.register_blueprint(tipo_predio_routes)
app.register_blueprint(tipo_seguridad_routes)