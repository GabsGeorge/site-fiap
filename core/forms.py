from django import forms

from core.models import Curso
from core.models import Aluno
from core.models import Professor

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'


class ContatoForm(forms.Form):

    nome = forms.CharField()
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea())

    def envia_email(self):
        print("Usuário: "+self.cleaned_data["nome"]+
        "\nE-Mail: "+self.cleaned_data["email"]+
        "\nMensagem: "+self.cleaned_data["mensagem"])


class EditaContaAlunoForm(forms.ModelForm):

    def clean_email(self):
    #Verifica se Email ja está cadastrado para poder editar    
        email = self.cleaned_data['email']
        queryset = Aluno.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email

    class Meta:
        model = Aluno
        fields = ('nome','email','celular','imagemAluno')
