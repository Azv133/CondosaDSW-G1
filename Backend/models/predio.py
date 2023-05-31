from utils.db import db

class Predio(db.Model):
    id_predio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    area = db.Column(db.Float)
    ubicacion = db.Column(db.String(255), nullable=True)
    id_distrito = db.Column(db.String(20), db.ForeignKey('distrito.id_dist'))
    id_tipo = db.Column(db.Integer, db.ForeignKey('tipo_predio.id_tipo'))
    nro_casas_habitacion = db.Column(db.Integer)
    nro_puertas_acceso = db.Column(db.Integer)
    nro_torres_bloques = db.Column(db.Integer, nullable=True)

    def __init__(self, nombre, area, ubicacion, id_distrito, id_tipo, nro_casas_habitacion, nro_puertas_acceso, nro_torres_bloques):
        self.nombre = nombre
        self.area = area
        self.ubicacion = ubicacion
        self.id_distrito = id_distrito
        self.id_tipo = id_tipo
        self.nro_casas_habitacion = nro_casas_habitacion
        self.nro_puertas_acceso = nro_puertas_acceso
        self.nro_torres_bloques = nro_torres_bloques

    def serialize(self):
        return {
            'id_predio': self.id_predio,
            'nombre': self.nombre,
            'area': self.area,
            'ubicacion': self.ubicacion,
            'id_distrito': self.id_distrito,
            'id_tipo': self.id_tipo,
            'nro_casas_habitacion': self.nro_casas_habitacion,
            'nro_puertas_acceso': self.nro_puertas_acceso,
            'nro_torres_bloques': self.nro_torres_bloques
        }