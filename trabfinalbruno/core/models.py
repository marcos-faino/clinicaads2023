from django.db import models


class Tecnico(models.Model):
    nome = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Atendimento (models.Model):
    descricao = models.CharField("Descricao", max_length=150)
    preco = models.DecimalField("Preco", max_digits=9, decimal_places=2)

    quantidade = models.IntegerField("Quantidade")
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE,
                                  blank=True, null=True)

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"
        ordering = ("descricao",)

    def __str__(self):
        return self.descricao
