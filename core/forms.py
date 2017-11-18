from django import forms

from core.models import Curso

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