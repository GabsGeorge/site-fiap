from django.db import models

# Criando modelo(classe) para sincronizar com o banco.

class Curso(models.Model):
	
    idcurso = models.AutoField("ID", db_column='IdCurso', primary_key=True)  # Field name made lowercase.
    sigla = models.CharField("Sigla", db_column='Sigla', max_length=5)  # Field name made lowercase.
    nome = models.CharField("Nome do Curso", db_column='Nome', max_length=50)  # Field name made lowercase.
    img = models.ImageField (upload_to = 'media', null = True, blank = True) #adiciona imagem na pasta "media"
    # Esta linha acima dá erro quando clona ERROR"core.Curso.img" Pillow is not instaled

    # Mostra o nome do curso formatado no painel admin do Django
    def __str__(self):
          return self.nome
    
    #class Meta:
    #    managed = False
    #    db_table = 'Curso' # nome que aparece na tabela do banco
    #    unique_together = (('idcurso', 'sigla', 'nome'),)
		
	

    #-----------------------Conexao Disciplinas----------------------------#
	
class Disciplina(models.Model):

    iddisciplina = models.IntegerField(db_column='IdDisciplina', primary_key=True)  # Field name made lowercase.
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