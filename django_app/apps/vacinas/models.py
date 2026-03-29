"""
Modelos de Vacinas para Carteira Digital Pet
Baseado no esquema SQL fornecido: vacina

PJI110 - UNIVESP 2026
"""

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from datetime import date, timedelta

from apps.pets.models import Pet
from apps.core.models import Veterinario


class Vacina(models.Model):
    """
    Modelo de vacina baseado na tabela 'vacina' do SQL
    
    Campos do SQL:
    - id_vacina INT AUTO_INCREMENT PRIMARY KEY
    - vacina VARCHAR(100) NOT NULL (nome da vacina)
    - data_aplicacao DATE NOT NULL
    - observacao VARCHAR(200)
    - pet_id_pet INT NOT NULL (FK)
    - veterinario_id_veterinario INT NOT NULL (FK)
    """
    
    # Tipos comuns de vacina
    TIPOS_VACINA_CHOICES = [
        ('V8', 'Óctupla (V8)'),
        ('V10', 'Déctupla (V10)'),
        ('V12', 'Dodectupla (V12)'),
        ('Antirrábica', 'Antirrábica'),
        ('Gripe_Canina', 'Gripe Canina'),
        ('Giardíase', 'Giardíase'),
        ('Leishmaniose', 'Leishmaniose'),
        ('Tríplice_Felina', 'Tríplice Felina'),
        ('Quádrupla_Felina', 'Quádrupla Felina'),
        ('FeLV', 'Leucemia Felina (FeLV)'),
        ('FIV', 'Imunodeficiência Felina (FIV)'),
        ('Outra', 'Outra'),
    ]
    
    STATUS_CHOICES = [
        ('Aplicada', 'Aplicada'),
        ('Agendada', 'Agendada'),
        ('Vencida', 'Vencida'),
        ('Cancelada', 'Cancelada'),
    ]
    
    # Campos principais
    vacina = models.CharField(
        'Nome da Vacina',
        max_length=100,
        help_text='Nome ou tipo da vacina aplicada'
    )
    
    tipo_vacina = models.CharField(
        'Tipo de Vacina',
        max_length=20,
        choices=TIPOS_VACINA_CHOICES,
        blank=True,
        null=True,
        help_text='Tipo padrão da vacina'
    )
    
    data_aplicacao = models.DateField(
        'Data de Aplicação',
        help_text='Data em que a vacina foi aplicada'
    )
    
    observacao = models.TextField(
        'Observações',
        max_length=200,
        blank=True,
        null=True,
        help_text='Observações sobre a aplicação da vacina'
    )
    
    # Campos extras para melhor controle
    lote = models.CharField(
        'Lote',
        max_length=50,
        blank=True,
        null=True,
        help_text='Lote da vacina'
    )
    
    fabricante = models.CharField(
        'Fabricante',
        max_length=100,
        blank=True,
        null=True,
        help_text='Fabricante da vacina'
    )
    
    validade = models.DateField(
        'Validade',
        blank=True,
        null=True,
        help_text='Data de validade da vacina'
    )
    
    dose = models.PositiveSmallIntegerField(
        'Dose',
        validators=[MinValueValidator(1)],
        default=1,
        help_text='Número da dose (1ª, 2ª, 3ª, etc.)'
    )
    
    doses_total = models.PositiveSmallIntegerField(
        'Total de Doses',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True,
        help_text='Número total de doses necessárias'
    )
    
    proxima_dose = models.DateField(
        'Próxima Dose',
        blank=True,
        null=True,
        help_text='Data prevista para próxima dose/reforço'
    )
    
    intervalo_dias = models.PositiveIntegerField(
        'Intervalo em Dias',
        blank=True,
        null=True,
        help_text='Intervalo em dias para próxima dose'
    )
    
    status = models.CharField(
        'Status',
        max_length=10,
        choices=STATUS_CHOICES,
        default='Aplicada',
        help_text='Status da vacinação'
    )
    
    valor = models.DecimalField(
        'Valor',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Valor pago pela vacina'
    )
    
    # Relacionamentos
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='vacinas',
        verbose_name='Pet'
    )
    
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.PROTECT,
        related_name='vacinas_aplicadas',
        verbose_name='Veterinário'
    )
    
    # Metadados
    ativo = models.BooleanField(
        'Ativo',
        default=True,
        help_text='Vacina ativa no sistema'
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
        db_table = 'vacina'
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['-data_aplicacao']
        indexes = [
            models.Index(fields=['data_aplicacao'], name='vacina_data_idx'),
            models.Index(fields=['proxima_dose'], name='vacina_proxima_idx'),
        ]

    def __str__(self):
        return f"{self.vacina} - {self.pet.pet} ({self.data_aplicacao})"

    def save(self, *args, **kwargs):
        """Override save para calcular próxima dose automaticamente"""
        if self.intervalo_dias and self.data_aplicacao and not self.proxima_dose:
            self.proxima_dose = self.data_aplicacao + timedelta(days=self.intervalo_dias)
        
        super().save(*args, **kwargs)

    @property
    def eh_primeira_dose(self):
        """Verifica se é a primeira dose"""
        return self.dose == 1

    @property
    def eh_ultima_dose(self):
        """Verifica se é a última dose do protocolo"""
        if self.doses_total:
            return self.dose >= self.doses_total
        return False

    @property
    def precisa_reforco(self):
        """Verifica se precisa de reforço"""
        if not self.proxima_dose:
            return False
        return date.today() >= self.proxima_dose

    @property
    def dias_para_reforco(self):
        """Calcula dias para próxima dose"""
        if not self.proxima_dose:
            return None
        
        delta = self.proxima_dose - date.today()
        return delta.days

    @property
    def status_reforco(self):
        """Retorna status do reforço"""
        if not self.proxima_dose:
            return 'Não programado'
        
        dias = self.dias_para_reforco
        
        if dias < 0:
            return 'Atrasado'
        elif dias == 0:
            return 'Hoje'
        elif dias <= 7:
            return 'Esta semana'
        elif dias <= 30:
            return 'Este mês'
        else:
            return 'No prazo'

    @property
    def tipo_display(self):
        """Retorna tipo da vacina formatado"""
        if self.tipo_vacina:
            return dict(self.TIPOS_VACINA_CHOICES).get(self.tipo_vacina, self.vacina)
        return self.vacina

    @property
    def dose_display(self):
        """Retorna dose formatada"""
        if self.doses_total:
            return f"{self.dose}ª dose de {self.doses_total}"
        return f"{self.dose}ª dose"

    @property
    def valor_display(self):
        """Retorna valor formatado"""
        if self.valor:
            return f"R$ {self.valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        return 'Não informado'

    @classmethod
    def get_vacinas_por_vencer(cls, dias=30):
        """Retorna vacinas que vencem nos próximos X dias"""
        limite = date.today() + timedelta(days=dias)
        
        return cls.objects.filter(
            ativo=True,
            status='Aplicada',
            proxima_dose__isnull=False,
            proxima_dose__lte=limite,
            proxima_dose__gte=date.today()
        )

    @classmethod
    def get_vacinas_vencidas(cls):
        """Retorna vacinas vencidas"""
        return cls.objects.filter(
            ativo=True,
            status='Aplicada',
            proxima_dose__isnull=False,
            proxima_dose__lt=date.today()
        )

    @classmethod
    def get_estatisticas_pet(cls, pet):
        """Retorna estatísticas de vacinação do pet"""
        vacinas = cls.objects.filter(pet=pet, ativo=True)
        
        return {
            'total': vacinas.count(),
            'aplicadas': vacinas.filter(status='Aplicada').count(),
            'agendadas': vacinas.filter(status='Agendada').count(),
            'vencidas': vacinas.filter(
                status='Aplicada',
                proxima_dose__isnull=False,
                proxima_dose__lt=date.today()
            ).count(),
            'por_vencer': vacinas.filter(
                status='Aplicada',
                proxima_dose__isnull=False,
                proxima_dose__gte=date.today(),
                proxima_dose__lte=date.today() + timedelta(days=30)
            ).count(),
        }


class ProtocoloVacinacao(models.Model):
    """
    Modelo para protocolos de vacinação por espécie/idade
    Não estava no SQL original, mas é útil para o sistema
    """
    
    especie = models.ForeignKey(
        'pets.Especie',
        on_delete=models.CASCADE,
        related_name='protocolos',
        verbose_name='Espécie'
    )
    
    nome_protocolo = models.CharField(
        'Nome do Protocolo',
        max_length=100,
        help_text='Nome do protocolo de vacinação'
    )
    
    idade_inicial_dias = models.PositiveIntegerField(
        'Idade Inicial (dias)',
        help_text='Idade mínima para começar o protocolo'
    )
    
    idade_final_dias = models.PositiveIntegerField(
        'Idade Final (dias)',
        blank=True,
        null=True,
        help_text='Idade máxima para o protocolo (opcional)'
    )
    
    ativo = models.BooleanField(
        'Ativo',
        default=True
    )

    class Meta:
        verbose_name = 'Protocolo de Vacinação'
        verbose_name_plural = 'Protocolos de Vacinação'
        ordering = ['especie', 'idade_inicial_dias']

    def __str__(self):
        return f"{self.nome_protocolo} - {self.especie}"


class ItemProtocolo(models.Model):
    """
    Item individual de um protocolo de vacinação
    """
    
    protocolo = models.ForeignKey(
        ProtocoloVacinacao,
        on_delete=models.CASCADE,
        related_name='itens',
        verbose_name='Protocolo'
    )
    
    vacina_nome = models.CharField(
        'Nome da Vacina',
        max_length=100
    )
    
    idade_aplicacao_dias = models.PositiveIntegerField(
        'Idade para Aplicação (dias)',
        help_text='Idade em dias para aplicar esta vacina'
    )
    
    dose_numero = models.PositiveSmallIntegerField(
        'Número da Dose',
        default=1
    )
    
    intervalo_dias = models.PositiveIntegerField(
        'Intervalo para Próxima Dose',
        blank=True,
        null=True,
        help_text='Dias até próxima dose/reforço'
    )
    
    obrigatoria = models.BooleanField(
        'Obrigatória',
        default=True,
        help_text='Vacina obrigatória no protocolo'
    )
    
    observacoes = models.TextField(
        'Observações',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Item do Protocolo'
        verbose_name_plural = 'Itens do Protocolo'
        ordering = ['protocolo', 'idade_aplicacao_dias', 'dose_numero']

    def __str__(self):
        return f"{self.vacina_nome} - {self.idade_aplicacao_dias} dias"