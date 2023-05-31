from utils.db import db

class Seguridad(db.Model):
    id_seguridad = db.Column(db.Integer, primary_key=True)
    nombre_seguridad = db.Column(db.String(255))
    tipo_seguridad = db.Column(db.Integer, db.ForeignKey('tipo_seguridad.id_tipo_seg'))

    def __init__(self, nombre_seguridad, tipo_seguridad):
        self.nombre_seguridad = nombre_seguridad
        self.tipo_seguridad = tipo_seguridad

    def serialize(self):
        return {
            'id_seguridad': self.id_seguridad,
            'nombre_seguridad': self.nombre_seguridad,
            'tipo_seguridad': self.tipo_seguridad
        }