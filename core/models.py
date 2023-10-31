from django.db import models


class Ambulatorio(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    numleitos = models.IntegerField(blank=True, null=True)
    andar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ambulatorio'
        verbose_name = 'Ambulatório'
        verbose_name_plural = 'Ambulatórios'

    def __str__(self):
        return self.nome


class Atende(models.Model):
    medico = models.ForeignKey('Medico', models.CASCADE, db_column='medico')
    convenio = models.ForeignKey('Convenio', models.CASCADE, db_column='convenio')

    class Meta:
        managed = False
        db_table = 'atende'
        unique_together = (('medico','convenio'),)
        verbose_name = 'MedicoXConvênio'
        verbose_name_plural = 'MedicoXConvênios'

    def __str__(self):
        return f'Dr. {self.medico.nome} atende convênio {self.convenio.nome}'


class Consulta(models.Model):
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='medico', blank=True, null=True)
    paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente', blank=True, null=True)
    convenio = models.ForeignKey('Convenio', models.DO_NOTHING, db_column='convenio', blank=True, null=True)
    porcent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f'Paciente:{self.paciente.nome}, Dr.{self.medico.nome}'


class Convenio(models.Model):
    codconv = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenio'
        verbose_name = 'Convênio'
        verbose_name_plural = 'Convênios'

    def __str__(self):
        return self.nome


class Medico(models.Model):
    crm = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    ambulatorio = models.ForeignKey(Ambulatorio, models.DO_NOTHING, db_column='idamb', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    ambulatorio = models.ForeignKey(Ambulatorio, models.SET_NULL, db_column='idamb', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.nome


class Possui(models.Model):
    paciente = models.ForeignKey(Paciente, models.CASCADE, db_column='paciente')
    convenio = models.ForeignKey(Convenio, models.CASCADE, db_column='convenio')
    tipo = models.CharField(max_length=1, blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'possui'
        verbose_name = 'Paciente|convênio'
        verbose_name_plural = 'Paciente|convênios'

    def __str__(self):
        return f'{self.paciente.nome} convênio: {self.convenio.nome}'