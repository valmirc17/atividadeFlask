# Importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Carregando o SQLAlchemy na variável DB
db = SQLAlchemy()

# Classe responsável por criar a entidade "Filmes" com seus atributos
class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    
    def __init__(self, titulo, ano, categoria):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        
# Classe responsável por criar a entidade usuário e seus atributos no banco
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __init__(self,email,password):
        self.email = email
        self.password = password

# Classe de imagens
class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)
    def __init__(self, filename):
        self.filename = filename