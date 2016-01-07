from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):

    nome = forms.Charfield(required=True)
    email = forms.EmailField(required=True)
    senha = forms.Charfield(required=True)
    telefone = forms.Charfield(required=True)
    nome_empresa = forms.Charfield(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adiciona_erro('Por favor verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existente')
            valid= False
        return valid

    def adiciona_erro(self, message):
        erros = self._erros.setdefault(
            forms.forms.NON_FIELD_ERRORS, 
            forms.util.ErrorList()
            )
        error.append(message)