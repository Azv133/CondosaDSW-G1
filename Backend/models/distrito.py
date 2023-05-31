from utils.db import db

class Distrito(db.Model):
    id_dist = db.Column(db.String(20), primary_key=True)
    name_dist = db.Column(db.String(255))
    id_provin = db.Column(db.String(20), db.ForeignKey('provincia.id_provin'))
    id_depar = db.Column(db.String(20), db.ForeignKey('departamento.id_depar'))

    def __init__(self, id_dist, name_dist, id_provin, id_depar):
        self.id_dist = id_dist
        self.name_dist = name_dist
        self.id_provin = id_provin
        self.id_depar = id_depar

    def serialize(self):
        return {
            'id_dist': self.id_dist,
            'name_dist': self.name_dist,
            'id_provin': self.id_provin,
            'id_depar': self.id_depar
        }