from main import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.String(50), nullable = False)
    nome = db.Column(db.String(50), nullable = False)
    admin = db.Column(db.Boolean, default = False)    
    senha = db.Column(db.String(256), nullable = False)

def __repr__(self):
    return '<Name %r>' % self.name