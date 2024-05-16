from pyexpat.errors import messages
from django.http import HttpResponseRedirect
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
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 
    else:
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user:
            login_django(request, user)
            return render(request, 'criar_agendamento.html')
        else:
            return render(request, 'criar_agendamento.html')
    
    return render(request, 'criar_agendamento.html')  

#CRUD VETERINARIO

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

#CRUD TUTOR
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

def atualizacaoTutor(request):
    # Recupera todos os Tutores cadastrados
    tutores = cadastroTutorModel.objects.all()
    return render(request, 'atualizacaoTutor.html', {'tutor': tutores})

def updateTutor(request, id):
    tutor = get_object_or_404(cadastroTutorModel, pk=id)
    
    if request.method == 'POST':
        form = cadastroTutorForm(request.POST, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cadastroTutorForm(instance=tutor)
    
    return render(request, 'updateTutor.html', {'form': form, 'tutor': tutor})

def deleteTutor(request, id):
     # Buscar o Tutor pelo ID
    tutor = get_object_or_404(cadastroTutorModel, pk=id)
    tutor.delete()
    return redirect('/')


#CRUD ANIMAL

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

def atualizacaoAnimal(request):
    # Recupera todos os animais cadastrados
    animal = cadastroAnimalModel.objects.all()
    return render(request, 'atualizacaoAnimal.html', {'animal': animal})

def updateAnimal(request, id):
    animal = get_object_or_404(cadastroAnimalModel, pk=id)
    
    if request.method == 'POST':
        form = cadastroAnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('atualizacaoAnimal')
    else:
        form = cadastroAnimalForm(instance=animal)
    
    return render(request, 'updateAnimal.html', {'form': form, 'animal': animal})

def deleteAnimal(request, id):
     # Buscar o animal pelo ID
    animal = get_object_or_404(cadastroAnimalModel, pk=id)
    animal.delete()
    return redirect('index.html')



def dashatualizacao(request):
    return render(request, 'dashatualizacao.html')


def criar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.tutor.id = request.user  # Associando o tutor atual ao agendamento

            try:
                animal_id = request.POST.get('animal')
                animal = cadastroAnimalModel.objects.get(id=animal_id)
                agendamento.animal = animal
            except cadastroAnimalModel.DoesNotExist:
                # Lidando com o caso em que o animal não foi encontrado
                
                pass

            agendamento.save()

            # Obtendo a lista de serviços marcados
            servicos_selecionados = request.POST.getlist('servicos[]')

            # Atribuindo os valores booleanos correspondentes ao objeto AgendamentoModel
            for servico in servicos_selecionados:
                setattr(agendamento, servico, True)

            agendamento.save()  # Salvando novamente para atualizar os valores dos serviços
            return redirect('/')  # Redireciona para a página inicial após o sucesso
    else:
        form = AgendamentoForm()

    tutores = cadastroTutorModel.objects.all()
    animais = cadastroAnimalModel.objects.all()
    return render(request, 'criar_agendamento.html', {'form': form, 'tutores': tutores, 'animais': animais})

    #vnome = request.POST.get("nome")
