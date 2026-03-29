"""
Configuração do Django Admin para os models do app Core
PJI110 - UNIVESP 2026
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import Usuario, Tutor, Veterinario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """Admin customizado para o modelo Usuario"""
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'criado_em')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'criado_em')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-criado_em',)
    
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Adicionais', {
            'fields': ('criado_em', 'atualizado_em'),
        }),
    )
    
    readonly_fields = ('criado_em', 'atualizado_em')


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    """Admin para o modelo Tutor"""
    
    list_display = ('tutor', 'email', 'cidade', 'uf', 'total_pets_display', 'criado_em')
    list_filter = ('uf', 'cidade', 'criado_em')
    search_fields = ('tutor', 'email', 'logradouro', 'bairro', 'cidade')
    ordering = ('tutor',)
    
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('tutor', 'email')
        }),
        ('Contato', {
            'fields': ('celular', 'telefone')
        }),
        ('Endereço', {
            'fields': (
                ('logradouro', 'numero_logradouro'),
                'complemento',
                ('bairro', 'cidade', 'uf'),
                'cep'
            )
        }),
        ('Sistema', {
            'fields': ('usuario', 'criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('criado_em', 'atualizado_em')
    
    def total_pets_display(self, obj):
        """Mostra total de pets do tutor"""
        total = obj.total_pets
        if total > 0:
            return format_html('<strong style="color: green;">{}</strong>', total)
        return format_html('<span style="color: gray;">0</span>')
    
    total_pets_display.short_description = 'Total de Pets'


@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    """Admin para o modelo Veterinario"""
    
    list_display = ('veterinario', 'email', 'cidade', 'uf', 'total_pets_display', 'criado_em')
    list_filter = ('uf', 'cidade', 'criado_em')
    search_fields = ('veterinario', 'email', 'logradouro', 'bairro', 'cidade')
    ordering = ('veterinario',)
    
    fieldsets = (
        ('Dados Profissionais', {
            'fields': ('veterinario', 'email')
        }),
        ('Contato', {
            'fields': ('celular', 'telefone')
        }),
        ('Endereço da Clínica', {
            'fields': (
                ('logradouro', 'numero_endereco'),
                ('bairro', 'cidade', 'uf'),
                'cep'
            )
        }),
        ('Sistema', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('criado_em', 'atualizado_em')
    
    def total_pets_display(self, obj):
        """Mostra total de pets atendidos"""
        total = obj.pets.filter(ativo=True).count()
        if total > 0:
            return format_html('<strong style="color: blue;">{}</strong>', total)
        return format_html('<span style="color: gray;">0</span>')
    
    total_pets_display.short_description = 'Pets Atendidos'