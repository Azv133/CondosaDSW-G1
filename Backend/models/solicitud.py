from utils.db import db

class Solicitud(db.Model):
    id_solicitud = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'))
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'))
    fecha = db.Column(db.Date)
    estado = db.Column(db.Integer, db.ForeignKey('estado_solicitud.id_estado'))
    descripcion = db.Column(db.Text, nullable=True)

    def __init__(self, id_cliente, id_predio, fecha, estado, descripcion):
        self.id_cliente = id_cliente
        self.id_predio = id_predio
        self.fecha = fecha
        self.estado = estado
        self.descripcion = descripcion

    def serialize(self):
        return {
            'id_solicitud': self.id_solicitud,
            'id_cliente': self.id_cliente,
            'id_predio': self.id_predio,
            'fecha': self.fecha,
            'estado': self.estado,
            'descripcion': self.descripcion
        }