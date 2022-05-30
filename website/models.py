
from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    nome = db.Column(db.String(150))
    senha = db.Column(db.String(150))
    reserva = db.relationship('Reserva')
