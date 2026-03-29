from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db

class User(UserMixin, db.Model):
    """Modelo para usuários do sistema"""
    
    __tablename__ = 'usuarios'
    
    # Campos básicos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    
    # Informações pessoais
    telefone = db.Column(db.String(20))
    endereco = db.Column(db.Text)
    
    # Metadados
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    ultimo_login = db.Column(db.DateTime)
    
    # Relacionamentos
    pets = db.relationship('Pet', backref='tutor', lazy='dynamic', cascade='all, delete-orphan')
    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
    
    def set_password(self, password):
        """Define a senha do usuário (hash)"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verifica se a senha está correta"""
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        """Retorna o ID do usuário como string (requerido pelo Flask-Login)"""
        return str(self.id)
    
    def atualizar_ultimo_login(self):
        """Atualiza o timestamp do último login"""
        self.ultimo_login = datetime.utcnow()
        db.session.commit()
    
    @property
    def total_pets(self):
        """Retorna o número total de pets do usuário"""
        return self.pets.count()
    
    @property
    def pets_ativos(self):
        """Retorna pets ativos do usuário"""
        return self.pets.filter_by(ativo=True)
    
    def to_dict(self):
        """Converte o objeto para dicionário (para APIs)"""
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone,
            'ativo': self.ativo,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'total_pets': self.total_pets
        }
    
    def __repr__(self):
        return f'<User {self.email}>'