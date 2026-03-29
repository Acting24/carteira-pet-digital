"""
Modelos Core do Django para Carteira Digital Pet
Baseado no esquema SQL fornecido: usuario, tutor, veterinario

PJI110 - UNIVESP 2026
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class Usuario(AbstractUser):
    """
    Modelo de usuário customizado baseado na tabela 'usuario' do SQL
    
    Campos do SQL:
    - id_usuario INT AUTO_INCREMENT PRIMARY KEY
    - login VARCHAR(50) NOT NULL
    - senha VARCHAR(250) NOT NULL  
    - criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    - atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    """
    
    # Django já fornece: id, username, email, password, first_name, last_name, is_active, date_joined, last_login
    # Vamos usar username como 'login' e adicionar campos extras
    
    username = models.CharField(
        'Login',
        max_length=50,
        unique=True,
        help_text='Nome de usuário para login'
    )
    
    email = models.EmailField(
        'Email',
        unique=True,
        help_text='Email será usado para login'
    )
    
    criado_em = models.DateTimeField(
        'Criado em',
        default=timezone.now,
        help_text='Data e hora de criação do usuário'
    )
    
    atualizado_em = models.DateTimeField(
        'Atualizado em',
        auto_now=True,
        help_text='Data e hora da última atualização'
    )

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.username} ({self.email})"


class Tutor(models.Model):
    """
    Modelo de tutor baseado na tabela 'tutor' do SQL
    
    Campos do SQL:
    - id_tutor INT AUTO_INCREMENT PRIMARY KEY
    - tutor VARCHAR(100) NOT NULL (nome do tutor)
    - email VARCHAR(100) NOT NULL
    - celular VARCHAR(20)
    - telefone VARCHAR(20)
    - logradouro VARCHAR(50) NOT NULL
    - numero_logradouro VARCHAR(10)
    - complemento VARCHAR(20)
    - bairro VARCHAR(50) NOT NULL
    - cidade VARCHAR(50) NOT NULL
    - uf VARCHAR(2) NOT NULL
    - cep VARCHAR(9)
    - usuario_id INT NOT NULL (FK)
    - criado_em TIMESTAMP
    - atualizado_em TIMESTAMP
    """
    
    # Validadores
    celular_validator = RegexValidator(
        regex=r'^\(\d{2}\)\s\d{4,5}-\d{4}$',
        message='Formato: (11) 99999-9999'
    )
    
    cep_validator = RegexValidator(
        regex=r'^\d{5}-\d{3}$',
        message='Formato: 00000-000'
    )
    
    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]
    
    # Campos
    tutor = models.CharField(
        'Nome do Tutor',
        max_length=100,
        help_text='Nome completo do tutor'
    )
    
    email = models.EmailField(
        'Email',
        max_length=100,
        help_text='Email de contato do tutor'
    )
    
    celular = models.CharField(
        'Celular',
        max_length=20,
        validators=[celular_validator],
        blank=True,
        null=True,
        help_text='Formato: (11) 99999-9999'
    )
    
    telefone = models.CharField(
        'Telefone',
        max_length=20,
        blank=True,
        null=True,
        help_text='Telefone fixo'
    )
    
    # Endereço
    logradouro = models.CharField(
        'Logradouro',
        max_length=50,
        help_text='Rua, avenida, etc.'
    )
    
    numero_logradouro = models.CharField(
        'Número',
        max_length=10,
        blank=True,
        null=True,
        help_text='Número da residência'
    )
    
    complemento = models.CharField(
        'Complemento',
        max_length=20,
        blank=True,
        null=True,
        help_text='Apartamento, casa, etc.'
    )
    
    bairro = models.CharField(
        'Bairro',
        max_length=50,
        help_text='Bairro'
    )
    
    cidade = models.CharField(
        'Cidade',
        max_length=50,
        help_text='Cidade'
    )
    
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=UF_CHOICES,
        help_text='Unidade da Federação'
    )
    
    cep = models.CharField(
        'CEP',
        max_length=9,
        validators=[cep_validator],
        blank=True,
        null=True,
        help_text='Formato: 00000-000'
    )
    
    # Relacionamento
    usuario = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name='perfil_tutor',
        verbose_name='Usuário'
    )
    
    # Metadados
    criado_em = models.DateTimeField(
        'Criado em',
        default=timezone.now
    )
    
    atualizado_em = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )

    class Meta:
        db_table = 'tutor'
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'
        ordering = ['tutor']
        indexes = [
            models.Index(fields=['tutor'], name='idx_tutor'),
        ]

    def __str__(self):
        return self.tutor

    @property
    def endereco_completo(self):
        """Retorna endereço formatado"""
        endereco = f"{self.logradouro}"
        if self.numero_logradouro:
            endereco += f", {self.numero_logradouro}"
        if self.complemento:
            endereco += f", {self.complemento}"
        endereco += f" - {self.bairro}, {self.cidade}/{self.uf}"
        if self.cep:
            endereco += f" - {self.cep}"
        return endereco

    @property
    def total_pets(self):
        """Retorna total de pets do tutor"""
        return self.pets.filter(ativo=True).count()


class Veterinario(models.Model):
    """
    Modelo de veterinário baseado na tabela 'veterinario' do SQL
    
    Campos do SQL:
    - id_veterinario INT AUTO_INCREMENT PRIMARY KEY
    - veterinario VARCHAR(100) NOT NULL
    - email VARCHAR(100)
    - celular VARCHAR(16)
    - telefone VARCHAR(16)  
    - logradouro VARCHAR(50) NOT NULL
    - numero_endereco VARCHAR(10)
    - bairro VARCHAR(50) NOT NULL
    - cidade VARCHAR(50) NOT NULL
    - uf VARCHAR(2) NOT NULL
    - cep VARCHAR(9)
    - criado_em TIMESTAMP
    - atualizado_em TIMESTAMP
    """
    
    # Validadores (mesmo do Tutor)
    celular_validator = RegexValidator(
        regex=r'^\(\d{2}\)\s\d{4,5}-\d{4}$',
        message='Formato: (11) 99999-9999'
    )
    
    cep_validator = RegexValidator(
        regex=r'^\d{5}-\d{3}$',
        message='Formato: 00000-000'
    )
    
    UF_CHOICES = Tutor.UF_CHOICES  # Reutilizar choices
    
    # Campos
    veterinario = models.CharField(
        'Nome do Veterinário',
        max_length=100,
        help_text='Nome completo do veterinário'
    )
    
    email = models.EmailField(
        'Email',
        max_length=100,
        blank=True,
        null=True,
        help_text='Email de contato'
    )
    
    celular = models.CharField(
        'Celular',
        max_length=16,
        validators=[celular_validator],
        blank=True,
        null=True,
        help_text='Formato: (11) 99999-9999'
    )
    
    telefone = models.CharField(
        'Telefone',
        max_length=16,
        blank=True,
        null=True,
        help_text='Telefone fixo'
    )
    
    # Endereço
    logradouro = models.CharField(
        'Logradouro',
        max_length=50,
        help_text='Rua, avenida, etc.'
    )
    
    numero_endereco = models.CharField(
        'Número',
        max_length=10,
        blank=True,
        null=True,
        help_text='Número da clínica/consultório'
    )
    
    bairro = models.CharField(
        'Bairro',
        max_length=50,
        help_text='Bairro'
    )
    
    cidade = models.CharField(
        'Cidade',
        max_length=50,
        help_text='Cidade'
    )
    
    uf = models.CharField(
        'UF',
        max_length=2,
        choices=UF_CHOICES,
        help_text='Unidade da Federação'
    )
    
    cep = models.CharField(
        'CEP',
        max_length=9,
        validators=[cep_validator],
        blank=True,
        null=True,
        help_text='Formato: 00000-000'
    )
    
    # Metadados
    criado_em = models.DateTimeField(
        'Criado em',
        default=timezone.now
    )
    
    atualizado_em = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )

    class Meta:
        db_table = 'veterinario'
        verbose_name = 'Veterinário'
        verbose_name_plural = 'Veterinários'
        ordering = ['veterinario']

    def __str__(self):
        return self.veterinario

    @property
    def endereco_completo(self):
        """Retorna endereço formatado"""
        endereco = f"{self.logradouro}"
        if self.numero_endereco:
            endereco += f", {self.numero_endereco}"
        endereco += f" - {self.bairro}, {self.cidade}/{self.uf}"
        if self.cep:
            endereco += f" - {self.cep}"
        return endereco