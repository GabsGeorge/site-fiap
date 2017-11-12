# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Aluno(models.Model):
    ra = models.IntegerField(db_column='RA', unique=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=120)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=2)  # Field name made lowercase.


class Arquivoquestoes(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.CharField(db_column='id_Turma', max_length=1)  # Field name made lowercase.
    numero_questao = models.ForeignKey('Questoes', models.DO_NOTHING, db_column='Numero_Questao')  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', unique=True, max_length=500)  # Field name made lowercase.


class Arquivorespostas(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.CharField(db_column='id_Turma', max_length=1)  # Field name made lowercase.
    numero_questao = models.ForeignKey('Respostas', models.DO_NOTHING, db_column='Numero_Questao')  # Field name made lowercase.
    ra_aluno = models.IntegerField(db_column='RA_Aluno')  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', unique=True, max_length=500)  # Field name made lowercase.


class Curso(models.Model):
    sigla = models.CharField(db_column='Sigla', unique=True, max_length=5)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=50)  # Field name made lowercase.

    

class Cursoturma(models.Model):
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=5)  # Field name made lowercase.
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_Turma', unique=True)  # Field name made lowercase.

    

class Disciplina(models.Model):
    nome = models.CharField(db_column='Nome', unique=True, max_length=240)  # Field name made lowercase.
    carga_horario = models.SmallIntegerField(db_column='Carga_Horario')  # Field name made lowercase.
    teoria = models.DecimalField(db_column='Teoria', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pratica = models.DecimalField(db_column='Pratica', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ementa = models.TextField(db_column='Ementa')  # Field name made lowercase. This field type is a guess.
    competencias = models.TextField(db_column='Competencias')  # Field name made lowercase. This field type is a guess.
    habilidades = models.TextField(db_column='Habilidades')  # Field name made lowercase. This field type is a guess.
    conteudo = models.TextField(db_column='Conteudo')  # Field name made lowercase. This field type is a guess.
    bibliografia_basica = models.TextField(db_column='Bibliografia_Basica')  # Field name made lowercase. This field type is a guess.
    bibliografia_complementar = models.TextField(db_column='Bibliografia_Complementar')  # Field name made lowercase. This field type is a guess.

    

class Gradecurricular(models.Model):
    sigla_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='Sigla_Curso')  # Field name made lowercase.
    ano = models.SmallIntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.CharField(db_column='Semestre', unique=True, max_length=1)  # Field name made lowercase.


class Matricula(models.Model):
    ra_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='RA_Aluno')  # Field name made lowercase.
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.CharField(db_column='id_Turma', unique=True, max_length=1)  # Field name made lowercase.



class Periodo(models.Model):
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=5)  # Field name made lowercase.
    ano_grade = models.SmallIntegerField(db_column='Ano_Grade')  # Field name made lowercase.
    semestre_grade = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='Semestre_Grade')  # Field name made lowercase.
    numero = models.SmallIntegerField(db_column='Numero', unique=True)  # Field name made lowercase.


class Periododisciplina(models.Model):
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=5)  # Field name made lowercase.
    ano_grade = models.SmallIntegerField(db_column='Ano_Grade')  # Field name made lowercase.
    semestre_grade = models.CharField(db_column='Semestre_Grade', max_length=1)  # Field name made lowercase.
    numero_periodo = models.SmallIntegerField(db_column='Numero_Periodo', unique=True)  # Field name made lowercase.
    nome_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.


class Professor(models.Model):
    ra = models.IntegerField(db_column='RA', unique=True)  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', unique=True, max_length=30)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=120)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.


class Questoes(models.Model):
    nome_discplina = models.CharField(db_column='Nome_Discplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='id_Turma', unique=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', unique=True)  # Field name made lowercase.
    data_limite_entrega = models.CharField(db_column='Data_Limite_Entrega', max_length=10)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dia_publicacao = models.CharField(db_column='Dia_Publicacao', max_length=10)  # Field name made lowercase.



class Respostas(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    id_turma = models.ForeignKey(Questoes, models.DO_NOTHING, db_column='id_Turma')  # Field name made lowercase.
    numero_questao = models.IntegerField(db_column='Numero_Questao', unique=True)  # Field name made lowercase.
    ra_aluno = models.IntegerField(db_column='RA_Aluno', unique=True)  # Field name made lowercase.
    data_avaliacao = models.CharField(db_column='Data_Avaliacao', max_length=10)  # Field name made lowercase.
    nota = models.DecimalField(db_column='Nota', max_digits=4, decimal_places=2)  # Field name made lowercase.
    avaliacao = models.TextField(db_column='Avaliacao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data_de_envio = models.CharField(db_column='Data_de_Envio', max_length=10)  # Field name made lowercase.


class Turma(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    idTurma = models.CharField(unique=True, max_length=1)
    turno = models.CharField(db_column='Turno', max_length=15)  # Field name made lowercase.
    ra_professor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='RA_Professor')  # Field name made lowercase.
