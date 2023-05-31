from utils.db import db

class Cargo(db.Model):
    id_cargo = db.Column(db.Integer, primary_key=True)
    name_cargo = db.Column(db.String(255))

    def __init__(self, name_cargo):
        self.name_cargo = name_cargo

    def serialize(self):
        return {
            'id_cargo': self.id_cargo,
            'name_cargo': self.name_cargo
        }