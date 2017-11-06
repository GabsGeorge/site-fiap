from django.db import models

# Criando modelo(classe) para sincronizar com o banco.
class Curso(models.Model):
	
    idcurso = models.AutoField("ID", db_column='IdCurso', primary_key=True)  # Field name made lowercase.
    sigla = models.CharField("Sigla", db_column='Sigla', max_length=5)  # Field name made lowercase.
    nome = models.CharField("Nome do Curso", db_column='Nome', max_length=50)  # Field name made lowercase.
    #imagem = models.ImageField(upload_to = "uploads",blank=True) #adiciona imagem na pasta "uploads"

    # Mostra o nome do curso formatado no painel admin do Django
    def __str__(self):
          return self.nome
    
    class Meta:
        managed = False
        db_table = 'Curso' # nome que aparece na tabela do banco
        unique_together = (('idcurso', 'sigla', 'nome'),)
		
	
	
	