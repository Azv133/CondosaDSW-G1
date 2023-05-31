from utils.db import db

class Departamento(db.Model):
    id_depar = db.Column(db.String(20), primary_key=True)
    name_depar = db.Column(db.String(255))

    def __init__(self, name_depar):
        self.name_depar = name_depar

    def serialize(self):
        return {
            'id_depar': self.id_depar,
            'name_depar': self.name_depar
        }