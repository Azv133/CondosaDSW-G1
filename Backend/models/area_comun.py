from utils.db import db

class AreaComun(db.Model):
    id_area_c = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))

    def __init__(self, tipo):
        self.tipo = tipo

    def serialize(self):
        return {
            'id_area_c': self.id_area_c,
            'tipo': self.tipo
        }