from utils.db import db

class PredioAreaComun(db.Model):
    id_area_c = db.Column(db.Integer, db.ForeignKey('area_comun.id_area_c'), primary_key=True)
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'), primary_key=True)
    area = db.Column(db.Float)

    def __init__(self, id_area_c, id_predio, area):
        self.id_area_c = id_area_c
        self.id_predio = id_predio
        self.area = area

    def serialize(self):
        return {
            'id_area_c': self.id_area_c,
            'id_predio': self.id_predio,
            'area': self.area
        }