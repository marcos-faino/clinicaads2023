from django.contrib import admin
from core.models import Tecnico, Atendimento

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco', 'quantidade',)
