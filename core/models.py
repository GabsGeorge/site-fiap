from django.db import models


# Criando modelo(classe) para sincronizar com o banco.
class Curso(models.Model):
	
	nome = models.CharField("Nome",max_length=50)
	carga_horaria = models.IntegerField("Carga horária")
	professor = models.CharField("Coordenador",max_length=50)
	tipo = models.CharField("Tipo",max_length=50)
	descricao = models.TextField("Descricão",blank=(True))
	ativo = models.BooleanField("Ativo?",default=(True))
	imagem = models.ImageField(upload_to = "uploads",blank=True) #adiciona imagem na pasta "uploads"
	
	# Mostra o nome do curso formatado no painel admin do Django
	def __str__(self):
		return self.nome