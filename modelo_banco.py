# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoreAluno(models.Model):
    ra = models.IntegerField(db_column='RA', unique=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=120)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_aluno'


class CoreArquivoquestoes(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.CharField(db_column='id_Turma', max_length=1)  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', unique=True, max_length=500)  # Field name made lowercase.
    numero_questao = models.ForeignKey('CoreQuestoes', models.DO_NOTHING, db_column='Numero_Questao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_arquivoquestoes'


class CoreArquivorespostas(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.CharField(db_column='id_Turma', max_length=1)  # Field name made lowercase.
    ra_aluno = models.IntegerField(db_column='RA_Aluno')  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', unique=True, max_length=500)  # Field name made lowercase.
    numero_questao = models.ForeignKey('CoreRespostas', models.DO_NOTHING, db_column='Numero_Questao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_arquivorespostas'


class CoreCurso(models.Model):
    sigla = models.CharField(db_column='Sigla', unique=True, max_length=5)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_curso'


class CoreCursoturma(models.Model):
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=5)  # Field name made lowercase.
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.ForeignKey('CoreTurma', models.DO_NOTHING, db_column='id_Turma', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_cursoturma'


class CoreDisciplina(models.Model):
    nome = models.CharField(db_column='Nome', unique=True, max_length=240)  # Field name made lowercase.
    carga_horario = models.SmallIntegerField(db_column='Carga_Horario')  # Field name made lowercase.
    teoria = models.DecimalField(db_column='Teoria', max_digits=3, decimal_places=0)  # Field name made lowercase.
    pratica = models.DecimalField(db_column='Pratica', max_digits=3, decimal_places=0)  # Field name made lowercase.
    ementa = models.TextField(db_column='Ementa')  # Field name made lowercase.
    competencias = models.TextField(db_column='Competencias')  # Field name made lowercase.
    habilidades = models.TextField(db_column='Habilidades')  # Field name made lowercase.
    conteudo = models.TextField(db_column='Conteudo')  # Field name made lowercase.
    bibliografia_basica = models.TextField(db_column='Bibliografia_Basica')  # Field name made lowercase.
    bibliografia_complementar = models.TextField(db_column='Bibliografia_Complementar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_disciplina'


class CoreGradecurricular(models.Model):
    ano = models.SmallIntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.CharField(db_column='Semestre', unique=True, max_length=1)  # Field name made lowercase.
    sigla_curso = models.ForeignKey(CoreCurso, models.DO_NOTHING, db_column='Sigla_Curso')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_gradecurricular'


class CoreMatricula(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    id_turma = models.CharField(db_column='id_Turma', unique=True, max_length=1)  # Field name made lowercase.
    ra_aluno = models.ForeignKey(CoreAluno, models.DO_NOTHING, db_column='RA_Aluno')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_matricula'


class CorePeriodo(models.Model):
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=5)  # Field name made lowercase.
    ano_grade = models.SmallIntegerField(db_column='Ano_Grade')  # Field name made lowercase.
    numero = models.SmallIntegerField(db_column='Numero', unique=True)  # Field name made lowercase.
    semestre_grade = models.ForeignKey(CoreGradecurricular, models.DO_NOTHING, db_column='Semestre_Grade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_periodo'


class CorePeriododisciplina(models.Model):
    sigla_curso = models.CharField(db_column='Sigla_Curso', max_length=5)  # Field name made lowercase.
    ano_grade = models.SmallIntegerField(db_column='Ano_Grade')  # Field name made lowercase.
    semestre_grade = models.CharField(db_column='Semestre_Grade', max_length=1)  # Field name made lowercase.
    numero_periodo = models.SmallIntegerField(db_column='Numero_Periodo', unique=True)  # Field name made lowercase.
    nome_disciplina = models.ForeignKey(CoreDisciplina, models.DO_NOTHING, db_column='Nome_Disciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_periododisciplina'


class CoreProfessor(models.Model):
    ra = models.IntegerField(db_column='RA', unique=True)  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', unique=True, max_length=30)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=120)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=80)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_professor'


class CoreQuestoes(models.Model):
    nome_discplina = models.CharField(db_column='Nome_Discplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', unique=True)  # Field name made lowercase.
    data_limite_entrega = models.CharField(db_column='Data_Limite_Entrega', max_length=10)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.
    dia_publicacao = models.CharField(db_column='Dia_Publicacao', max_length=10)  # Field name made lowercase.
    id_turma = models.ForeignKey('CoreTurma', models.DO_NOTHING, db_column='id_Turma', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_questoes'


class CoreRespostas(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    numero_questao = models.IntegerField(db_column='Numero_Questao', unique=True)  # Field name made lowercase.
    ra_aluno = models.IntegerField(db_column='RA_Aluno', unique=True)  # Field name made lowercase.
    data_avaliacao = models.CharField(db_column='Data_Avaliacao', max_length=10)  # Field name made lowercase.
    nota = models.DecimalField(db_column='Nota', max_digits=4, decimal_places=2)  # Field name made lowercase.
    avaliacao = models.TextField(db_column='Avaliacao', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.
    data_de_envio = models.CharField(db_column='Data_de_Envio', max_length=10)  # Field name made lowercase.
    id_turma = models.ForeignKey(CoreQuestoes, models.DO_NOTHING, db_column='id_Turma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_respostas'


class CoreTurma(models.Model):
    nome_disciplina = models.CharField(db_column='Nome_Disciplina', max_length=240)  # Field name made lowercase.
    ano_ofertado = models.SmallIntegerField(db_column='Ano_Ofertado')  # Field name made lowercase.
    semestre_ofertado = models.CharField(db_column='Semestre_Ofertado', max_length=1)  # Field name made lowercase.
    idturma = models.CharField(db_column='idTurma', unique=True, max_length=1)  # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=15)  # Field name made lowercase.
    ra_professor = models.ForeignKey(CoreProfessor, models.DO_NOTHING, db_column='RA_Professor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_turma'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
