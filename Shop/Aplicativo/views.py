from django.shortcuts import get_object_or_404, render, redirect
from Aplicativo.forms import cadastroTutorForm,VeterinarioCadastroForm, cadastroAnimalForm, AgendamentoForm
#from Aplicativo.forms import TutoresCadastroForm
from .models import VeterinarioCadastroModel, cadastroTutorModel,cadastroAnimalModel , AgendamentoModel
from validate_docbr import CPF, CNPJ
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from . import views




def index(request):
    return render(request, 'index.html')
def cadastro(request):
    return render(request, 'cadastro.html')
@login_required
def home(request):
    return render(request, 'home.html')
def cadastroServicos(request):
    return render(request, 'cadastroServicos.html')



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 
    else:
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user:
            login_django(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'index.html')
    
    return render(request, 'login.html')  


def cadastroVet(request):
    if request.method == 'POST':
        form = VeterinarioCadastroForm(request.POST)
        vet = VeterinarioCadastroModel()
        vet.nome = form.data['nome']
        vet.email = form.data['email']
        vet.logradouro = form.data['logradouro']
        vet.bairro = form.data['bairro']
        vet.cep = form.data['cep']
        vet.numero = form.data['numero']
        vet.cidade = form.data['cidade']
        vet.estado = form.data['estado']
        vet.telefone = form.data['telefone']
        vet.crmv = form.data['crmv']
        vet.password = form.data['password']
        vet.save()
        vet = User.objects.create_user(username= form.data['email'], password = form.data ['password'])
        vet.save()
    return render(request, 'cadastroVet.html')

def atualizacaoVet(request):
    # Recupera todos os veterinários cadastrados
    veterinarios = VeterinarioCadastroModel.objects.all()
    return render(request, 'atualizacaoVet.html', {'veterinarios': veterinarios})

def updateVet(request, id):
    veterinario = get_object_or_404(VeterinarioCadastroModel, pk=id)
    
    if request.method == 'POST':
        form = VeterinarioCadastroForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('atualizacaoVet')
    else:
        form = VeterinarioCadastroForm(instance=veterinario)
    
    return render(request, 'updateVet.html', {'form': form, 'veterinario': veterinario})


def deleteVet(request, id):
     # Buscar o veterinário pelo ID
    veterinario = get_object_or_404(VeterinarioCadastroModel, pk=id)
    veterinario.delete()
    return redirect('index.html')


def cadastroTutor(request):
    if request.method == 'POST':
        form = cadastroTutorForm(request.POST)
        tutor = cadastroTutorModel()
        tutor.nometutor = form.data['nometutor']
        tutor.email = form.data['email']
        tutor.logradouro = form.data['logradouro']
        tutor.bairro = form.data['bairro']
        tutor.cep = form.data['cep']
        tutor.numero = form.data['numero']
        tutor.cidade = form.data['cidade']
        tutor.estado = form.data['estado']
        tutor.telefone = form.data['telefone']
        tutor.cpf = form.data['cpf']
        tutor.save()
        tutor = User.objects.create_user(username= form.data['email'], password = form.data ['password'])
        tutor.save()
    return render(request, 'cadastroTutor.html')


def cadastroAnimal(request):
    if request.method == 'POST':
        form = cadastroAnimalForm(request.POST)
        animal= cadastroAnimalModel()
        animal.nomepet = form.data['nomepet']
        animal.especie = form.data['especie']
        animal.porte = form.data['porte']
        animal.raca = form.data['raca']
        animal.sexo = form.data['sexo']
        animal.datanascimento = form.data['datanascimento']
        animal.cpftutor = form.data['cpftutor']
        animal.save()
        

    return render(request, 'cadastroAnimal.html')

def index(request):
    return render(request, 'index.html')
def cadastro(request):
    return render(request, 'cadastro.html')


def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            servicos_selecionados = form.cleaned_data.get('servicos[]', [])  # Ajuste aqui para acessar o campo correto
            print("Serviços selecionados:", servicos_selecionados)
            for servico in servicos_selecionados:
                # Crie uma instância do modelo e atribua os valores dos serviços selecionados
                agendamento_model = AgendamentoModel(**{servico: True})  
                agendamento_model.save()  # Salve o modelo no banco de dados
            print("Agendamentos criados com sucesso!")
            return redirect('index.html')
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento.html', {'form': form})




#TUTOR

#def salvaranimal(request):
    #vnome = request.POST.get("nome")
