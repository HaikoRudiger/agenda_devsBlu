from main import db
from models.usuario import Usuario

class Evento(db.Model):
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    #id_usuario = db.Column(db.Integer, ForeignKey = Usuario.id) <-- Linha com erro -->
    id_usuario = db.Column(db.Integer, db.ForeignKey("Usuario.id"), nullable = False)
    data_evento = db.Column(db.Date, nullable = False)
    titulo = db.Column(db.String(50), nullable = False) # Linha com erro <-- nullabel -->
    descricao = db.Column(db.String(200), nullable = False)
    publico = db.Column(db.Boolean, default = False)
    ativo = db.Column(db.Boolean, default = True)


def __repr__(self):
        return '<Name %r>' % self.name