from datetime import datetime, date, timedelta
from flask_sqlalchemy import SQLAlchemy
from .. import db

class Vacina(db.Model):
    """Modelo para vacinas do sistema"""
    
    __tablename__ = 'vacinas'
    
    # Campos básicos
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)  # Nome da vacina
    fabricante = db.Column(db.String(100))
    lote = db.Column(db.String(50))
    
    # Datas importantes
    data_aplicacao = db.Column(db.Date, nullable=False)
    data_validade = db.Column(db.Date)
    proxima_dose = db.Column(db.Date)  # Quando deve tomar a próxima
    
    # Informações da aplicação
    veterinario = db.Column(db.String(100))
    clinica = db.Column(db.String(150))
    dose_numero = db.Column(db.Integer, default=1)  # 1ª dose, 2ª dose, etc.
    
    # Observações e reações
    observacoes = db.Column(db.Text)
    reacoes_adversas = db.Column(db.Text)
    
    # Metadados
    ativo = db.Column(db.Boolean, default=True, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'), nullable=False)
    
    def __init__(self, **kwargs):
        super(Vacina, self).__init__(**kwargs)
        
        # Se não foi definida próxima dose, calcular automaticamente
        if not self.proxima_dose and self.data_aplicacao:
            self.calcular_proxima_dose()
    
    def calcular_proxima_dose(self):
        """Calcula automaticamente quando deve ser a próxima dose"""
        if not self.data_aplicacao:
            return
        
        # Regras básicas para algumas vacinas comuns
        intervalos = {
            'v8': 21,   # Múltipla canina - 3 semanas
            'v10': 21,  # Múltipla canina - 3 semanas  
            'antirrábica': 365,  # Antirrábica - 1 ano
            'gripe canina': 365,  # Gripe canina - 1 ano
            'giárdia': 21,       # Giárdia - 3 semanas
            'leishmaniose': 21,  # Leishmaniose - 3 semanas
        }
        
        # Tentar encontrar intervalo baseado no nome da vacina
        nome_lower = self.nome.lower()
        dias_intervalo = 365  # Padrão: 1 ano
        
        for vacina, intervalo in intervalos.items():
            if vacina in nome_lower:
                dias_intervalo = intervalo
                break
        
        # Para primeiras doses de filhotes, intervalo menor
        if self.dose_numero == 1 and 'v8' in nome_lower or 'v10' in nome_lower:
            dias_intervalo = 21  # 3 semanas
        elif self.dose_numero == 2 and 'v8' in nome_lower or 'v10' in nome_lower:
            dias_intervalo = 21  # Mais 3 semanas
        elif self.dose_numero >= 3:
            dias_intervalo = 365  # Reforço anual
        
        self.proxima_dose = self.data_aplicacao + timedelta(days=dias_intervalo)
    
    @property
    def dias_para_proxima(self):
        """Retorna quantos dias faltam para a próxima dose"""
        if not self.proxima_dose:
            return None
        
        hoje = date.today()
        diferenca = (self.proxima_dose - hoje).days
        return diferenca
    
    @property
    def status_proxima_dose(self):
        """Retorna o status da próxima dose"""
        if not self.proxima_dose:
            return "Dose única"
        
        dias = self.dias_para_proxima
        if dias is None:
            return "Indefinido"
        
        if dias < 0:
            return f"Atrasada ({abs(dias)} dias)"
        elif dias == 0:
            return "Hoje"
        elif dias <= 7:
            return f"Em {dias} dias (urgente)"
        elif dias <= 30:
            return f"Em {dias} dias"
        else:
            return f"Em {dias} dias"
    
    @property
    def precisa_renovar(self):
        """Verifica se precisa renovar a vacina (próximos 30 dias ou atrasada)"""
        if not self.proxima_dose:
            return False
        
        hoje = date.today()
        limite = hoje + timedelta(days=30)
        
        return self.proxima_dose <= limite
    
    @property
    def esta_atrasada(self):
        """Verifica se a vacina está atrasada"""
        if not self.proxima_dose:
            return False
        
        return date.today() > self.proxima_dose
    
    @property
    def idade_pet_na_aplicacao(self):
        """Calcula idade do pet na data da aplicação"""
        if not self.pet or not self.pet.data_nascimento:
            return None
        
        idade_anos = self.data_aplicacao.year - self.pet.data_nascimento.year
        
        if (self.data_aplicacao.month < self.pet.data_nascimento.month or 
           (self.data_aplicacao.month == self.pet.data_nascimento.month and 
            self.data_aplicacao.day < self.pet.data_nascimento.day)):
            idade_anos -= 1
        
        return max(0, idade_anos)
    
    def to_dict(self):
        """Converte o objeto para dicionário (para APIs)"""
        return {
            'id': self.id,
            'nome': self.nome,
            'fabricante': self.fabricante,
            'lote': self.lote,
            'data_aplicacao': self.data_aplicacao.isoformat() if self.data_aplicacao else None,
            'data_validade': self.data_validade.isoformat() if self.data_validade else None,
            'proxima_dose': self.proxima_dose.isoformat() if self.proxima_dose else None,
            'veterinario': self.veterinario,
            'clinica': self.clinica,
            'dose_numero': self.dose_numero,
            'observacoes': self.observacoes,
            'reacoes_adversas': self.reacoes_adversas,
            'ativo': self.ativo,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'dias_para_proxima': self.dias_para_proxima,
            'status_proxima_dose': self.status_proxima_dose,
            'precisa_renovar': self.precisa_renovar,
            'esta_atrasada': self.esta_atrasada,
            'pet_id': self.pet_id
        }
    
    def __repr__(self):
        return f'<Vacina {self.nome} - {self.data_aplicacao}>'