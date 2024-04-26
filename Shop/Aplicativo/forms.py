from django import forms
from .models import cadastroTutorModel, VeterinarioCadastroModel, cadastroAnimalModel
from. import views



class VeterinarioCadastroForm(forms.ModelForm):
    class Meta:
        model = VeterinarioCadastroModel
        fields=['nome', 'email','logradouro','bairro','numero','cidade','estado','telefone','crmv','password']

class cadastroTutorForm(forms.ModelForm):
    class Meta:
        model = cadastroTutorModel
        fields = ['nometutor', 'email', 'logradouro', 'bairro','cep','numero','cidade','estado', 'telefone', 'password','cpf']

class cadastroAnimalForm(forms.ModelForm):
    class Meta:
        model = cadastroAnimalModel
        fields = ['nomepet','especie','porte','raca','cor','sexo','datanascimento','cpftutor']
