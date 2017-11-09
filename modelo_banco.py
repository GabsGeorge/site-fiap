# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key =True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aluno(models.Model):
    idaluno = models.IntegerField(db_column='IdAluno', unique=True)  # Field name made lowercase.
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
    idarquivosquestao = models.IntegerField(db_column='IdArquivosQuestao', unique=True)  # Field name made lowercase.
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
    idarquivoresposta = models.IntegerField(db_column='IdArquivoResposta', unique=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.
    idquestao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='IdQuestao')  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idresposta = models.ForeignKey('Resposta', models.DO_NOTHING, db_column='IdResposta')  # Field name made lowercase.
    arquivoresposta = models.CharField(db_column='ArquivoResposta', max_length=500)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ArquivosRespostas'
        unique_together = (('idarquivoresposta', 'arquivoresposta'),)


class Curso(models.Model):
    idcurso = models.IntegerField(db_column='IdCurso', unique=True)  # Field name made lowercase.
    sigla = models.CharField(db_column='Sigla', max_length=5)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curso'
        unique_together = (('idcurso', 'sigla', 'nome'),)


class Cursoturma(models.Model):
    idcursoturma = models.IntegerField(db_column='IdCursoTurma', unique=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CursoTurma'


class Disciplina(models.Model):
    iddisciplina = models.IntegerField(db_column='IdDisciplina', unique=True)  # Field name made lowercase.
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
    iddisciplinaofertada = models.IntegerField(db_column='IdDisciplinaOfertada', unique=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    anoofertado = models.SmallIntegerField(db_column='AnoOfertado')  # Field name made lowercase.
    semestreofertado = models.CharField(db_column='SemestreOfertado', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'
        unique_together = (('iddisciplinaofertada', 'anoofertado', 'semestreofertado'),)


class Gradecurricular(models.Model):
    idgradecurricular = models.IntegerField(db_column='IdGradeCurricular', unique=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.CharField(db_column='Semestre', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GradeCurricular'
        unique_together = (('idgradecurricular', 'ano', 'semestre'),)


class Matricula(models.Model):
    idmatricula = models.IntegerField(db_column='IdMatricula', unique=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idturma = models.ForeignKey('Turma', models.DO_NOTHING, db_column='IdTurma')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Matricula'


class Periodo(models.Model):
    idperiodo = models.IntegerField(db_column='IdPeriodo', unique=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    idgradecurricular = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='IdGradeCurricular')  # Field name made lowercase.
    numeroperiodo = models.SmallIntegerField(db_column='NumeroPeriodo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Periodo'
        unique_together = (('idperiodo', 'numeroperiodo'),)


class Periododisciplina(models.Model):
    idperiododisciplina = models.IntegerField(db_column='IdPeriodoDisciplina', unique=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    idgradecurricular = models.ForeignKey(Gradecurricular, models.DO_NOTHING, db_column='IdGradeCurricular')  # Field name made lowercase.
    idperiodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='IdPeriodo')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeriodoDisciplina'


class Professor(models.Model):
    idprofessor = models.IntegerField(db_column='IdProfessor', unique=True)  # Field name made lowercase.
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
    idquestao = models.IntegerField(db_column='IdQuestao', unique=True)  # Field name made lowercase.
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
    idresposta = models.IntegerField(db_column='IdResposta', unique=True)  # Field name made lowercase.
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
    idturma = models.IntegerField(db_column='IdTurma', unique=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Turma'


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


class CoreCurso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    professor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    ativo = models.BooleanField()
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_curso'


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
