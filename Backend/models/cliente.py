from utils.db import db

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    dni = db.Column(db.String(255))
    nombres = db.Column(db.String(255))
    apellidos = db.Column(db.String(255))
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String(255))

    def __init__(self, dni, nombres, apellidos, telefono, correo):
        self.dni = dni
        self.nombres = nombres 
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo

    def serialize(self):
        return {
            'id_cliente': self.id_cliente,
            'dni': self.dni,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'telefono': self.telefono,
            'correo': self.correo
        }