from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from Aplicativo.forms import cadastroTutorForm,VeterinarioCadastroForm, cadastroAnimalForm, AgendamentoForm
#from Aplicativo.forms import TutoresCadastroForm
from .models import VeterinarioCadastroModel, cadastroTutorModel,cadastroAnimalModel , AgendamentoModel, ServicoModel
#from validate_docbr import CPF, CNPJ
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.core.exceptions import MultipleObjectsReturned
from . import views
from django.shortcuts import render, redirect
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

@login_required
def home(request):
    return render(request, 'home.html')

def cadastroServicos(request):
    return render(request, 'cadastroServicos.html')

def cadastrarVacinas(request):
    return render(request, 'cadastrarVacinas.html')

def agendar_cliente(request):
    return render(request, 'agendar_cliente.html')

def visualizar_cartaoVacina(request):
    return render(request, 'visualizar_cartaoVacina.html')

def autenticacao_cliente(request):
    return render(request, 'autenticacao_cliente.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 
    else:
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user:
            login_django(request, user)
            return render(request, 'home.html', {'username': username})
        else:
            return render(request, 'index.html')
    
    return render(request, 'criar_agendamento.html')  

#CRUD VETERINARIO

def cadastroVet(request):
    if request.method == 'POST':
        form = VeterinarioCadastroForm(request.POST)
        if form.is_valid():
            vet = VeterinarioCadastroModel()
            vet.nome = form.cleaned_data['nome']
            vet.email = form.cleaned_data['email']
            vet.logradouro = form.cleaned_data['logradouro']
            vet.bairro = form.cleaned_data['bairro']
            vet.cep = form.cleaned_data['cep']
            vet.numero = form.cleaned_data['numero']
            vet.cidade = form.cleaned_data['cidade']
            vet.estado = form.cleaned_data['estado']
            vet.telefone = form.cleaned_data['telefone']
            vet.crmv = form.cleaned_data['crmv']
            vet.password = form.cleaned_data['password']
            vet.save()
            
            user = User.objects.create_user(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()
            
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')  # Redirecione para uma página de sucesso ou
            # return render(request, 'cadastroVet.html')  # Renderize a mesma página com a mensagem
        
    else:
        form = VeterinarioCadastroForm()
    
    return render(request, 'cadastroVet.html', {'form': form})
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
    return redirect('atualizacaoVet')

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
    animais = cadastroAnimalModel.objects.all()  # Recupera todos os animais do banco de dados
    context = {
        'animais': animais
    }
    return render(request, 'atualizacaoAnimal.html', context)

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
    servicos = ServicoModel.objects.all()

    if request.method == "POST":
        tutor_id = request.POST.get('tutor')
        animal_id = request.POST.get('animal')
        servico_id = request.POST.get('servico')
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        if not tutor_id or not animal_id or not servico_id or not data or not horario:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'criar_agendamento.html', {
                'tutores': cadastroTutorModel.objects.all(),
                'animais': cadastroAnimalModel.objects.all(),
                'servicos': servicos,
            })

        servico = ServicoModel.objects.filter(id=servico_id).first()
        if not servico:
            messages.error(request, 'O serviço selecionado não está disponível. Por favor, selecione outro serviço.')
            return render(request, 'criar_agendamento.html', {
                'tutores': cadastroTutorModel.objects.all(),
                'animais': cadastroAnimalModel.objects.all(),
                'servicos': servicos,
            })

        agendamento = AgendamentoModel(
            tutor_id=tutor_id,
            animal_id=animal_id,
            servico_id=servico_id,
            data=data,
            horario=horario
        )
        agendamento.save()
        messages.success(request, 'Cadastro realizado com sucesso!')
        return render(request, 'criar_agendamento.html', {
            'tutores': cadastroTutorModel.objects.all(),
            'animais': cadastroAnimalModel.objects.all(),
            'servicos': servicos,
            'redirect_home': True,  # Adiciona um indicador para redirecionar
        })

    tutores = cadastroTutorModel.objects.all()
    animais = cadastroAnimalModel.objects.all()
    context = {
        'tutores': tutores,
        'animais': animais,
        'servicos': servicos
    }
    return render(request, 'criar_agendamento.html', context)


def visualizar_agendamentos(request):
    tutor_id = request.user.id
    agendamentos = AgendamentoModel.objects.filter(tutor_id=tutor_id, status='aberto')

    return render(request, 'visualizar_agendamentos.html', {'agendamentos': agendamentos})

def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(AgendamentoModel, id=agendamento_id)
    agendamento.status = 'cancelado'
    agendamento.save()
    messages.success(request, 'Agendamento cancelado com sucesso!')
    return redirect('visualizar_agendamentos')

def fechar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(AgendamentoModel, id=agendamento_id)
    agendamento.status = 'fechado'
    agendamento.save()
    messages.success(request, 'Agendamento marcado como realizado!')
    return redirect('visualizar_agendamentos')
# @login_required
def criarservicos(request):
    if request.method == 'POST':
        servicos_selecionados = request.POST.getlist('servicos')
        for nome_servico in servicos_selecionados:
            ServicoModel.objects.create(nome=nome_servico)
        return redirect('success')  # Redireciona para uma página de sucesso após cadastrar
    
    # Busca todos os serviços cadastrados
    servicos_cadastrados = ServicoModel.objects.all()
    
    return render(request, 'criarservicos.html', {'servicos_cadastrados': servicos_cadastrados})