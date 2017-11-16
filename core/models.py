# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(db_column='Nome', unique=True, max_length=240)  # Field name made lowercase.
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


class Curso(models.Model):
    sigla = models.CharField(db_column='Sigla', unique=True, max_length=5)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curso'


class Aluno(models.Model):
    ra_aluno = models.IntegerField(db_column='RA_Aluno', unique=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=120)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='Sigla_Curso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aluno'


class Gradecurricular(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='Sigla_Curso')  # Field name made lowercase.
    ano = models.SmallIntegerField(db_column='Ano', unique=True)  # Field name made lowercase.
    semestre = models.CharField(db_column='Semestre', unique=True, max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GradeCurricular'


class Periodo(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='Sigla_Curso')  # Field name made lowercase.
    ano_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='Ano_Grade')  # Field name made lowercase.
    semestre_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='Semestre_Grade')  # Field name made lowercase.
    numeroperiodo = models.SmallIntegerField(db_column='NumeroPeriodo', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Periodo'

class Periododisciplina(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='Sigla_Curso')  # Field name made lowercase.
    ano_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='Ano_Grade')  # Field name made lowercase.
    semestre_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='Semestre_Grade')  # Field name made lowercase.
    numero_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='Numero_Periodo')  # Field name made lowercase.
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodoDisciplina'     


class Disciplinaofertada(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.
    anoofertado = models.SmallIntegerField(db_column='AnoOfertado', unique=True)  # Field name made lowercase.
    semestreofertado = models.CharField(db_column='SemestreOfertado', unique=True, max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'
                

class Professor(models.Model):
    ra_professor = models.IntegerField(db_column='RA_Professor', unique=True)  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', unique=True, max_length=30)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=120)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Professor'


class Turma(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Semestre_Ofertado')  # Field name made lowercase.
    id_turma = models.CharField(db_column='Id_Turma', unique=True, max_length=1)  # Field name made lowercase.
    ra_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='RA_Professor')  # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Turma'


class Cursoturma(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='Sigla_Curso')  # Field name made lowercase.
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Semestre_Ofertado')  # Field name made lowercase.
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='Id_Turma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CursoTurma'


class Questao(models.Model):
    nome_discplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Discplina')  # Field name made lowercase.
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Semestre_Ofertado')  # Field name made lowercase.
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='Id_Turma')  # Field name made lowercase.
    numeroquestao = models.IntegerField(db_column='NumeroQuestao', unique=True)  # Field name made lowercase.
    datalimiteentrega = models.CharField(db_column='DataLimiteEntrega', max_length=10)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase. This field type is a guess.
    data = models.CharField(db_column='Data', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Questao'        


class Arquivosquestao(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Semestre_Ofertado')  # Field name made lowercase.
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='Id_Turma')  # Field name made lowercase.
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='Numero_Questao')  # Field name made lowercase.
    arquivoquestao = models.CharField(db_column='ArquivoQuestao', unique=True, max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivosQuestao'

class Resposta(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Ano_Ofertado')  # Field name made lowercase.
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='Id_Turma')  # Field name made lowercase.
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='Numero_Questao')  # Field name made lowercase.
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Semestre_Ofertado')  # Field name made lowercase.
    ra_aluno = models.IntegerField(db_column='RA_Aluno', unique=True)  # Field name made lowercase.
    dataavaliacao = models.CharField(db_column='DataAvaliacao', max_length=10)  # Field name made lowercase.
    nota = models.DecimalField(db_column='Nota', max_digits=4, decimal_places=2)  # Field name made lowercase.
    avaliacao = models.TextField(db_column='Avaliacao')  # Field name made lowercase. This field type is a guess.
    descricao = models.TextField(db_column='Descricao')  # Field name made lowercase. This field type is a guess.
    datadeenvio = models.CharField(db_column='DataDeEnvio', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Resposta'


class Arquivosrespostas(models.Model):
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Semestre_Ofertado')  # Field name made lowercase.
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='Id_Turma')  # Field name made lowercase.
    numero_questao = models.ForeignKey(Questao, models.DO_NOTHING, db_column='Numero_Questao')  # Field name made lowercase.
    ra_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='RA_Aluno')  # Field name made lowercase.
    #arquivoresposta = models.CharField(db_column=ArquivoResposta, unique=True, max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivosRespostas'


class Matricula(models.Model):
    ra_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='RA_Aluno')  # Field name made lowercase.
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.
    ano_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='Semestre_Ofertado')  # Field name made lowercase.
    id_turma = models.ForeignKey(Turma, models.DO_NOTHING, db_column='Id_Turma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Matricula'





