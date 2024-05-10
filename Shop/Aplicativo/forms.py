from django import forms
from .models import cadastroTutorModel, VeterinarioCadastroModel, cadastroAnimalModel, AgendamentoModel
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

class AgendamentoForm(forms.ModelForm):
    banhoetosa = forms.BooleanField(required=False)
    tosahigienica = forms.BooleanField(required=False)
    vanicacao = forms.BooleanField(required=False)
    exameslaboratoriais = forms.BooleanField(required=False)
    microchipagem = forms.BooleanField(required=False)
    consultaclinica = forms.BooleanField(required=False)
    atendimentodomiciliar = forms.BooleanField(required=False)
    atendimento24horas = forms.BooleanField(required=False)
    hospedagem = forms.BooleanField(required=False)
    transporte = forms.BooleanField(required=False)
    adestramento = forms.BooleanField(required=False)

    class Meta:
        model = AgendamentoModel
        fields = ['banhoetosa', 'tosahigienica', 'vanicacao', 'exameslaboratoriais', 'microchipagem', 'consultaclinica', 'atendimentodomiciliar', 'atendimento24horas', 'hospedagem', 'transporte', 'adestramento']
