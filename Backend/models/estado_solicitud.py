from utils.db import db

class EstadoSolicitud(db.Model):
    id_estado = db.Column(db.Integer, primary_key=True)
    name_estado = db.Column(db.String(255))

    def __init__(self, name_estado):
        self.name_estado = name_estado

    def serialize(self):
        return {
            'id_estado': self.id_estado,
            'name_estado': self.name_estado
        }