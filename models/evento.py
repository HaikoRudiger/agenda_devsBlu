from models.usuario import Usuario
from main import db

class Evento(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #id_usuario = db.Column(db.Integer, ForeignKey = (Usuario.id))
    data_evento = db.Column(db.Date, nullable = False)
    titulo = db.Column(db.String(50), nullable = False)
    descricao = db.Column(db.String(200), nullable = False)
    publico = db.Column(db.Boolean, default = True)
    ativo = db.Column(db.Boolean, default = True)


def __repr__(self):
        return '<Name %r>' % self.name