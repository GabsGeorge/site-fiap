# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aluno(models.Model):
    idaluno = models.AutoField(db_column='IdAluno', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    ra_aluno = models.IntegerField(db_column='RA_Aluno')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=120)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aluno'
        unique_together = (('idaluno', 'ra_aluno'),)


class Arquivosquestao(models.Model):
    idarquivosquestao = models.AutoField(db_column='IdArquivosQuestao', primary_key=True)  # Field name made lowercase.
    idquestao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='IdQuestao')  # Field name made lowercase.
    iddisciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.
    arquivoquestao = models.CharField(db_column='ArquivoQuestao', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivosQuestao'
        unique_together = (('idarquivosquestao', 'arquivoquestao'),)


class Arquivosrespostas(models.Model):
    idarquivoresposta = models.AutoField(db_column='IdArquivoResposta', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.
    idquestao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='IdQuestao')  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idresposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='IdResposta')  # Field name made lowercase.
    arquivoresposta = models.CharField(db_column='ArquivoResposta', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivosRespostas'
        unique_together = (('idarquivoresposta', 'arquivoresposta'),)


class Curso(models.Model):
    idcurso = models.AutoField(db_column='IdCurso', primary_key=True)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=5)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curso'
        unique_together = (('idcurso', 'sigla', 'nome'),)


class Cursoturma(models.Model):
    idcursoturma = models.AutoField(db_column='IdCursoTurma', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CursoTurma'


class Disciplina(models.Model):
    iddisciplina = models.AutoField(db_column='IdDisciplina', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=240)  # Field name made lowercase.
    cargahoraria = models.SmallIntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    teoria = models.DecimalField(db_column='Teoria', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pratica = models.DecimalField(db_column='Pratica', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ementa = models.TextField(db_column='Ementa')  # Field name made lowercase. This field type is a guess.
    competencias = models.TextField(db_column='Competencias')  # Field name made lowercase. This field type is a guess.
    habilidades = models.TextField(db_column='Habilidades')  # Field name made lowercase. This field type is a guess.
    conteudo = models.TextField(db_column='Conteudo')  # Field name made lowercase. This field type is a guess.
    bibliografia_basica = models.TextField(db_column='Bibliografia_Basica')  # Field name made lowercase. This field type is a guess.
    biblioteca_complementar = models.TextField(db_column='Biblioteca_complementar')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Disciplina'
        unique_together = (('iddisciplina', 'nome'),)


class Disciplinaofertada(models.Model):
    iddisciplinaofertada = models.AutoField(db_column='IdDisciplinaOfertada', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    anoofertado = models.SmallIntegerField(db_column='AnoOfertado')  # Field name made lowercase.
    semestreofertado = models.CharField(db_column='SemestreOfertado', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'
        unique_together = (('iddisciplinaofertada', 'anoofertado', 'semestreofertado'),)


class Gradecurricular(models.Model):
    idgradecurricular = models.AutoField(db_column='IdGradeCurricular', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.CharField(db_column='Semestre', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GradeCurricular'
        unique_together = (('idgradecurricular', 'ano', 'semestre'),)


class Matricula(models.Model):
    idmatricula = models.AutoField(db_column='IdMatricula', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Matricula'


class Periodo(models.Model):
    idperiodo = models.AutoField(db_column='IdPeriodo', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    idgradecurricular = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='IdGradeCurricular')  # Field name made lowercase.
    numeroperiodo = models.SmallIntegerField(db_column='NumeroPeriodo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Periodo'
        unique_together = (('idperiodo', 'numeroperiodo'),)


class Periododisciplina(models.Model):
    idperiododisciplina = models.AutoField(db_column='IdPeriodoDisciplina', primary_key=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    idgradecurricular = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='IdGradeCurricular')  # Field name made lowercase.
    idperiodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='IdPeriodo')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodoDisciplina'


class Professor(models.Model):
    idprofessor = models.AutoField(db_column='IdProfessor', primary_key=True)  # Field name made lowercase.
    ra_professor = models.IntegerField(db_column='RA_Professor')  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=30)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=120)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Professor'
        unique_together = (('idprofessor', 'ra_professor', 'apelido'),)


class Questao(models.Model):
    idquestao = models.AutoField(db_column='IdQuestao', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.
    numeroquestao = models.IntegerField(db_column='NumeroQuestao')  # Field name made lowercase.
    datalimiteentrega = models.CharField(db_column='DataLimiteEntrega', max_length=10)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase. This field type is a guess.
    data = models.CharField(db_column='Data', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questao'
        unique_together = (('idquestao', 'numeroquestao'),)


class Resposta(models.Model):
    idresposta = models.AutoField(db_column='IdResposta', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.
    idquestao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='IdQuestao')  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    dataavaliacao = models.CharField(db_column='DataAvaliacao', max_length=10)  # Field name made lowercase.
    nota = models.DecimalField(db_column='Nota', max_digits=4, decimal_places=2)  # Field name made lowercase.
    avaliacao = models.TextField(db_column='Avaliacao')  # Field name made lowercase. This field type is a guess.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase. This field type is a guess.
    datadeenvio = models.CharField(db_column='DataDeEnvio', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Resposta'


class Turma(models.Model):
    idturma = models.AutoField(db_column='IdTurma', primary_key=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Turma'
