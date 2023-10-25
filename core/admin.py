from django.contrib import admin
from . import models

@admin.register(models.Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    fields = ('codconv', 'nome',)


class ConvenioInline(admin.StackedInline):
    model = models.Atende
    extra = 1
    raw_id_fields = ['convenio']


@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    fields = ('crm', 'nome', 'telefone', 'salario', 'ambulatorio')
    inlines = [ConvenioInline,]

