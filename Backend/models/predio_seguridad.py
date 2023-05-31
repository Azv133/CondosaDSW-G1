from utils.db import db

class PredioSeguridad(db.Model):
    id_seguridad = db.Column(db.Integer, db.ForeignKey('seguridad.id_seguridad'), primary_key=True)
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'), primary_key=True)
    cantidad_seguridad = db.Column(db.Integer)

    def __init__(self, id_seguridad, id_predio, cantidad_seguridad):
        self.id_seguridad = id_seguridad
        self.id_predio = id_predio
        self.cantidad_seguridad = cantidad_seguridad

    def serialize(self):
        return {
            'id_seguridad': self.id_seguridad,
            'id_predio': self.id_predio,
            'cantidad_seguridad': self.cantidad_seguridad
        }