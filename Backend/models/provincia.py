from utils.db import db

class Provincia(db.Model):
    id_provin = db.Column(db.String(20), primary_key=True)
    name_provin = db.Column(db.String(255))
    id_depar = db.Column(db.String(20), db.ForeignKey('departamento.id_depar'))

    def __init__(self, name_provin, id_depar):
        self.name_provin = name_provin
        self.id_depar = id_depar

    def serialize(self):
        return {
            'id_provin': self.id_provin,
            'name_provin': self.name_provin,
            'id_depar': self.id_depar
        }