
from . import db
from flask_login import UserMixin

class Cadastrar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True) 
    projetor = db.Column(db.Integer)
    bloco = db.Column(db.Integer)
    andar = db.Column(db.Integer)
    tipo_quadro = db.Column(db.Integer)
    ac = db.Column(db.Integer)
    
    
class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    tipo = db.Column(db.Integer)
    nome = db.Column(db.String(150))
    senha = db.Column(db.String(150))
    reserva = db.relationship('Reserva')
