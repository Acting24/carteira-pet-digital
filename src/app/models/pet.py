from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from .. import db

class Pet(db.Model):
    """Modelo para pets do sistema"""
    
    __tablename__ = 'pets'
    
    # Campos básicos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)  # Cão, Gato, etc.
    raca = db.Column(db.String(100))
    sexo = db.Column(db.String(10))  # Macho, Fêmea
    
    # Informações físicas
    data_nascimento = db.Column(db.Date)
    peso = db.Column(db.Float)  # em kg
    cor = db.Column(db.String(50))
    
    # Informações médicas
    castrado = db.Column(db.Boolean, default=False)
    chip = db.Column(db.String(20))  # Número do microchip
    observacoes = db.Column(db.Text)
    
    # Foto do pet
    foto_url = db.Column(db.String(255))
    
    # Metadados
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    vacinas = db.relationship('Vacina', backref='pet', lazy='dynamic', cascade='all, delete-orphan')
    
    def __init__(self, **kwargs):
        super(Pet, self).__init__(**kwargs)
    
    @property
    def idade_anos(self):
        """Calcula a idade do pet em anos"""
        if not self.data_nascimento:
            return None
        
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        
        # Ajustar se ainda não fez aniversário neste ano
        if hoje.month < self.data_nascimento.month or \
           (hoje.month == self.data_nascimento.month and hoje.day < self.data_nascimento.day):
            idade -= 1
            
        return max(0, idade)
    
    @property
    def idade_formatada(self):
        """Retorna idade formatada em anos e meses"""
        if not self.data_nascimento:
            return "Idade não informada"
        
        hoje = date.today()
        anos = self.idade_anos
        
        # Calcular meses
        meses = hoje.month - self.data_nascimento.month
        if hoje.day < self.data_nascimento.day:
            meses -= 1
        
        if meses < 0:
            meses += 12
        
        if anos == 0:
            return f"{meses} {'mês' if meses == 1 else 'meses'}"
        elif meses == 0:
            return f"{anos} {'ano' if anos == 1 else 'anos'}"
        else:
            return f"{anos} {'ano' if anos == 1 else 'anos'} e {meses} {'mês' if meses == 1 else 'meses'}"
    
    @property
    def total_vacinas(self):
        """Retorna o número total de vacinas aplicadas"""
        return self.vacinas.count()
    
    @property
    def vacinas_em_dia(self):
        """Verifica se as vacinas estão em dia (implementar lógica específica depois)"""
        # Por enquanto, retorna True se tem pelo menos uma vacina
        return self.total_vacinas > 0
    
    @property
    def proximas_vacinas(self):
        """Retorna vacinas que vencem nos próximos 30 dias"""
        from datetime import timedelta
        limite = date.today() + timedelta(days=30)
        
        return self.vacinas.filter(
            db.and_(
                Vacina.proxima_dose.isnot(None),
                Vacina.proxima_dose <= limite
            )
        ).all()
    
    def to_dict(self):
        """Converte o objeto para dicionário (para APIs)"""
        return {
            'id': self.id,
            'nome': self.nome,
            'especie': self.especie,
            'raca': self.raca,
            'sexo': self.sexo,
            'data_nascimento': self.data_nascimento.isoformat() if self.data_nascimento else None,
            'idade_formatada': self.idade_formatada,
            'peso': self.peso,
            'cor': self.cor,
            'castrado': self.castrado,
            'chip': self.chip,
            'observacoes': self.observacoes,
            'foto_url': self.foto_url,
            'ativo': self.ativo,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'total_vacinas': self.total_vacinas,
            'vacinas_em_dia': self.vacinas_em_dia
        }
    
    def __repr__(self):
        return f'<Pet {self.nome} ({self.especie})>'