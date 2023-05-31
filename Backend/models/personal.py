from utils.db import db

class Personal(db.Model):
    id_person = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargo.id_cargo'))
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'))

    def __init__(self, cantidad, id_cargo, id_predio):
        self.cantidad = cantidad
        self.id_cargo = id_cargo
        self.id_predio = id_predio

    def serialize(self):
        return {
            'id_person': self.id_person,
            'cantidad': self.cantidad,
            'id_cargo': self.id_cargo,
            'id_predio': self.id_predio
        }
