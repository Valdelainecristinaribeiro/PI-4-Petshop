from django import forms
from .models import cadastroTutorModel, VeterinarioCadastro
from. import views



class VeterinarioCadastroForm(forms.ModelForm):
    class Meta:
        model = VeterinarioCadastro
        fields=['nome', 'email','endereco','bairro','numero','cidade','estado','telefone','crmv','senha']

class cadastroTutorForm(forms.ModelForm):
    class Meta:
        model = cadastroTutorModel
        fields = ['nometutor', 'email', 'logradouro', 'bairro','cep','numero','cidade','estado', 'telefone', 'password']


        