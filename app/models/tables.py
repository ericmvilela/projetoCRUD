from app import db
from datetime import datetime
from sqlalchemy import Numeric


class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    preco = db.Column(Numeric(15, 2))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __repr__(self):
        return f'<Produto {self.nome}>'
    