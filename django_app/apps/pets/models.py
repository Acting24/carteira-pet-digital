"""
Modelos de Pets para Carteira Digital Pet
Baseado no esquema SQL fornecido: especie, pet, pet_veterinario

PJI110 - UNIVESP 2026
"""

from django.db import models
from django.utils import timezone
from datetime import date
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from apps.core.models import Tutor, Veterinario


class Especie(models.Model):
    """
    Modelo de espécie baseado na tabela 'especie' do SQL
    
    Campos do SQL:
    - id_especie INT AUTO_INCREMENT PRIMARY KEY
    - especie VARCHAR(50) NOT NULL (Descrição da espécie: Ave, Canina, Felina)
    """
    
    especie = models.CharField(
        'Espécie',
        max_length=50,
        unique=True,
        help_text='Nome da espécie (ex: Canina, Felina, Ave)'
    )
    
    ativo = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Espécie ativa no sistema'
    )

    class Meta:
        db_table = 'especie'
        verbose_name = 'Espécie'
        verbose_name_plural = 'Espécies'
        ordering = ['especie']

    def __str__(self):
        return self.especie


class Pet(models.Model):
    """
    Modelo de pet baseado na tabela 'pet' do SQL
    
    Campos do SQL:
    - id_pet INT AUTO_INCREMENT PRIMARY KEY
    - pet VARCHAR(50) NOT NULL (nome do pet)
    - raca VARCHAR(50)
    - sexo ENUM('M', 'F') NOT NULL
    - data_nascimento DATE
    - castrado ENUM('S', 'N')
    - data_castracao DATE
    - tutor_id INT NOT NULL (FK)
    - especie_id INT NOT NULL (FK)
    - criado_em TIMESTAMP
    - atualizado_em TIMESTAMP
    """
    
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    
    CASTRADO_CHOICES = [
        ('S', 'Sim'),
        ('N', 'Não'),
    ]
    
    # Campos básicos
    pet = models.CharField(
        'Nome do Pet',
        max_length=50,
        help_text='Nome do pet'
    )
    
    raca = models.CharField(
        'Raça',
        max_length=50,
        blank=True,
        null=True,
        help_text='Raça do pet (opcional)'
    )
    
    sexo = models.CharField(
        'Sexo',
        max_length=1,
        choices=SEXO_CHOICES,
        help_text='Sexo do pet'
    )
    
    data_nascimento = models.DateField(
        'Data de Nascimento',
        blank=True,
        null=True,
        help_text='Data de nascimento do pet'
    )
    
    castrado = models.CharField(
        'Castrado',
        max_length=1,
        choices=CASTRADO_CHOICES,
        blank=True,
        null=True,
        help_text='Pet é castrado?'
    )
    
    data_castracao = models.DateField(
        'Data da Castração',
        blank=True,
        null=True,
        help_text='Data da castração (se aplicável)'
    )
    
    # Campos extras não presentes no SQL original
    cor = models.CharField(
        'Cor',
        max_length=50,
        blank=True,
        null=True,
        help_text='Cor predominante do pet'
    )
    
    peso = models.DecimalField(
        'Peso (kg)',
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Peso em quilogramas'
    )
    
    microchip = models.CharField(
        'Microchip',
        max_length=20,
        blank=True,
        null=True,
        help_text='Número do microchip'
    )
    
    observacoes = models.TextField(
        'Observações',
        blank=True,
        null=True,
        help_text='Observações gerais sobre o pet'
    )
    
    # Foto do pet
    foto = models.ImageField(
        'Foto',
        upload_to='pets/fotos/%Y/%m/',
        blank=True,
        null=True,
        help_text='Foto do pet'
    )
    
    # Versão redimensionada da foto
    foto_thumbnail = ImageSpecField(
        source='foto',
        processors=[ResizeToFit(200, 200)],
        format='JPEG',
        options={'quality': 85}
    )
    
    # Relacionamentos
    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
        related_name='pets',
        verbose_name='Tutor'
    )
    
    especie = models.ForeignKey(
        Especie,
        on_delete=models.PROTECT,
        related_name='pets',
        verbose_name='Espécie'
    )
    
    veterinarios = models.ManyToManyField(
        Veterinario,
        through='PetVeterinario',
        related_name='pets',
        verbose_name='Veterinários'
    )
    
    # Metadados
    ativo = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Pet ativo no sistema'
    )
    
    criado_em = models.DateTimeField(
        'Criado em',
        default=timezone.now
    )
    
    atualizado_em = models.DateTimeField(
        'Atualizado em',
        auto_now=True
    )

    class Meta:
        db_table = 'pet'
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'
        ordering = ['pet']
        indexes = [
            models.Index(fields=['pet'], name='pet_idx'),
        ]

    def __str__(self):
        return f"{self.pet} ({self.especie})"

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
    def sexo_display(self):
        """Retorna nome completo do sexo"""
        return dict(self.SEXO_CHOICES).get(self.sexo, '')

    @property
    def castrado_display(self):
        """Retorna status de castração formatado"""
        if self.castrado:
            return dict(self.CASTRADO_CHOICES).get(self.castrado, '')
        return 'Não informado'

    @property
    def total_vacinas(self):
        """Retorna total de vacinas aplicadas"""
        return self.vacinas.filter(ativo=True).count()

    @property
    def proximas_vacinas(self):
        """Retorna vacinas que vencem nos próximos 30 dias"""
        from datetime import timedelta
        from apps.vacinas.models import Vacina
        
        limite = date.today() + timedelta(days=30)
        
        return self.vacinas.filter(
            ativo=True,
            proxima_dose__isnull=False,
            proxima_dose__lte=limite
        )


class PetVeterinario(models.Model):
    """
    Tabela intermediária para o relacionamento Many-to-Many entre Pet e Veterinario
    
    Baseada na tabela 'pet_veterinario' do SQL:
    - pet_id_pet INT NOT NULL (FK)
    - veterinario_id_veterinario INT NOT NULL (FK)
    """
    
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        verbose_name='Pet'
    )
    
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.CASCADE,
        verbose_name='Veterinário'
    )
    
    # Campos extras para enriquecer o relacionamento
    data_inicio = models.DateField(
        'Início do Acompanhamento',
        default=timezone.now,
        help_text='Data de início do acompanhamento'
    )
    
    ativo = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Relacionamento ativo'
    )
    
    observacoes = models.TextField(
        'Observações',
        blank=True,
        null=True,
        help_text='Observações sobre o acompanhamento'
    )

    class Meta:
        db_table = 'pet_veterinario'
        verbose_name = 'Pet-Veterinário'
        verbose_name_plural = 'Pets-Veterinários'
        unique_together = [['pet', 'veterinario']]

    def __str__(self):
        return f"{self.pet.pet} - {self.veterinario.veterinario}"