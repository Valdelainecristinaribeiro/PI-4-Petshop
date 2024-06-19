from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from Aplicativo.forms import VacinaForm, cadastroTutorForm,VeterinarioCadastroForm, cadastroAnimalForm, AgendamentoForm, ServicoForm
#from Aplicativo.forms import TutoresCadastroForm
from .models import VeterinarioCadastroModel, cadastroTutorModel,cadastroAnimalModel , AgendamentoModel, ServicoModel, cadastroVacinaModel
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

def about(request):
        return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def agenda_cliente(request):
    tutor_id = request.user.id
    agendamentos = AgendamentoModel.objects.filter(tutor_id=tutor_id, status='aberto')
    return render(request, 'agenda_cliente.html', {'agendamentos': agendamentos})
    return render(request, 'agenda_cliente.html')

def home_cliente(request):
    return render(request, 'home_cliente.html')

def agendamento_cliente(request):
    servicos = ServicoModel.objects.all()

    if request.method == "POST":
        tutor_id = request.POST.get('tutor')
        animal_id = request.POST.get('animal')
        servico_id = request.POST.get('servico')
        data = request.POST.get('data')
        horario = request.POST.get('horario')

        if not tutor_id or not animal_id or not servico_id or not data or not horario:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'agendamento_cliente.html', {
                'tutores': cadastroTutorModel.objects.all(),
                'animais': cadastroAnimalModel.objects.all(),
                'servicos': servicos,
            })

        servico = ServicoModel.objects.filter(id=servico_id).first()
        if not servico:
            messages.error(request, 'O serviço selecionado não está disponível. Por favor, selecione outro serviço.')
            return render(request, 'agendamento_cliente.html', {
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
        return render(request, 'agendamento_cliente.html', {
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
    return render(request, 'agendamento_cliente.html', context)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'login.html')

        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('home')  # Substitua 'home' pelo nome da sua view de página inicial
        else:
            messages.error(request, 'Email ou senha incorretos.')
            return render(request, 'index.html')

    return render(request, 'login.html')

#CRUD VETERINARIO
def cadastroVet(request):
    if request.method == 'POST':
        form = VeterinarioCadastroForm(request.POST)
        if form.is_valid():
            # Cria o objeto VeterinarioCadastroModel
            vet = VeterinarioCadastroModel(
                nome=form.cleaned_data['nome'],
                email=form.cleaned_data['email'],
                logradouro=form.cleaned_data['logradouro'],
                bairro=form.cleaned_data['bairro'],
                cep=form.cleaned_data['cep'],
                numero=form.cleaned_data['numero'],
                cidade=form.cleaned_data['cidade'],
                estado=form.cleaned_data['estado'],
                telefone=form.cleaned_data['telefone'],
                crmv=form.cleaned_data['crmv']
            )
            vet.save()
            
            # Cria o usuário associado ao veterinário
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            
            # Exemplo de mensagem de sucesso
            messages.success(request, 'Cadastro realizado com sucesso!')
            
            # Redireciona para a página inicial ou outra página desejada
            return redirect('index')
        else:
            # Exemplo de mensagem de erro
            messages.error(request, 'Formulário inválido. Verifique os dados informados.')
    else:
        form = VeterinarioCadastroForm()
    
    # Carrega os serviços cadastrados para exibir no template
    servicos_cadastrados = ServicoModel.objects.all()
    
    return render(request, 'cadastroVet.html', {'form': form, 'servicos_cadastrados': servicos_cadastrados})

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
        if form.is_valid():
            required_fields = ['nometutor', 'email', 'logradouro', 'bairro', 'cep', 'numero', 'cidade', 'estado', 'telefone', 'cpf', 'password']
            missing_fields = [field for field in required_fields if not form.cleaned_data.get(field)]
            if missing_fields:
                messages.error(request, 'Todos os campos são obrigatórios.')
                return render(request, 'cadastroTutor.html', {'form': form})

            tutor = cadastroTutorModel(
                nometutor=form.cleaned_data['nometutor'],
                email=form.cleaned_data['email'],
                logradouro=form.cleaned_data['logradouro'],
                bairro=form.cleaned_data['bairro'],
                cep=form.cleaned_data['cep'],
                numero=form.cleaned_data['numero'],
                cidade=form.cleaned_data['cidade'],
                estado=form.cleaned_data['estado'],
                telefone=form.cleaned_data['telefone'],
                cpf=form.cleaned_data['cpf']
            )
            tutor.save()

            user = User.objects.create_user(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()

            messages.success(request, 'Cadastro realizado com sucesso!')
            return render(request, 'cadastroTutor.html', {'form': cadastroTutorForm()})
        else:
            messages.error(request, 'Por favor, preencha todos os dados corretamente.')
            return render(request, 'cadastroTutor.html', {'form': form})
    else:
        form = cadastroTutorForm()
    return render(request, 'cadastroTutor.html', {'form': form})

def autenticacao_cliente(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'autenticacao_cliente.html')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('agenda_cliente')
        else:
            messages.error(request, 'Email ou senha incorretos.')
            return render(request, 'autenticacao_cliente.html')
    
    return render(request, 'autenticacao_cliente.html')

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
            messages.success(request, 'Cadastro atualizado com sucesso!')
            return redirect('atualizacaoTutor')
    else:
        form = cadastroTutorForm(instance=tutor)
    
    return render(request, 'updateTutor.html', {'form': form, 'tutor': tutor})

def deleteTutor(request, id):
     # Buscar o Tutor pelo ID
    tutor = get_object_or_404(cadastroTutorModel, pk=id)
    tutor.delete()
    return redirect('atualizacaoTutor')

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
            # Redireciona para a página de detalhes do animal após salvar
            return redirect('atualizacaoAnimal')
    else:
        form = cadastroAnimalForm(instance=animal)
    
    return render(request, 'updateAnimal.html', {'form': form, 'animal': animal})

def deleteAnimal(request, id):
     # Buscar o animal pelo ID
    animal = get_object_or_404(cadastroAnimalModel, pk=id)
    animal.delete()
    return redirect('updateAnimal')

def dashatualizacao(request):
    return render(request, 'dashatualizacao.html')

#CRUD AGENDAMENTO
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AgendamentoModel, ServicoModel, cadastroAnimalModel

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

def criarservicos(request):

    if request.method == 'POST':
        servicos_selecionados = request.POST.getlist('servicos')
        
        # Aqui você pode processar os serviços selecionados
        for servico_nome in servicos_selecionados:
            # Verifica se o serviço já existe no banco de dados
            servico, created = ServicoModel.objects.get_or_create(nome=servico_nome)
        
        # Exemplo de mensagem de sucesso
        messages.success(request, 'Serviços cadastrados com sucesso!')
        
        # Redireciona para a página de cadastro de veterinário (ou outra página desejada)
        return redirect('cadastroVet')
    
    # Caso GET, carrega a página com os serviços cadastrados
    servicos_cadastrados = ServicoModel.objects.all()
    return render(request, 'criarservicos.html', {'servicos_cadastrados': servicos_cadastrados})

def cadastrarVacinas(request):
    form = VacinaForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Vacina cadastrada com sucesso!')
            return redirect('cadastrarVacinas')  # Redirecione para a mesma página de cadastro de vacinas
        else:
            messages.error(request, 'Erro ao cadastrar vacina. Verifique os dados e tente novamente.')

    tutores = cadastroTutorModel.objects.all()
    animais = cadastroAnimalModel.objects.all()

    context = {
        'form': form,
        'tutores': tutores,
        'animais': animais,
    }
    
    return render(request, 'cadastrarVacinas.html', context)
def cancelarvacina(request, id_vacina):
    vacina = get_object_or_404(cadastroVacinaModel, id=id_vacina)
    if request.method == 'POST':
        vacina.delete()
        return redirect('success')  # Redireciona para uma página de sucesso após deletar

    return render(request, 'cancelarvacina.html', {'vacina': vacina})

def updateVacinas(request, id_vacina):
    vacina = get_object_or_404(cadastroVacinaModel, id=id_vacina)
    if request.method == 'POST':
        form = VacinaForm(request.POST, instance=vacina)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redireciona para uma página de sucesso após atualizar

    else:
        form = VacinaForm(instance=vacina)

    return render(request, 'cadastroVacinas.html', {'form': form})

    return render(request, 'cadastroVacinas.html')

def visualizar_cartaoVacina(request):
    vacinas = cadastroVacinaModel.objects.all()
    return render(request, 'visualizar_cartaoVacina.html', {'vacinas': vacinas})

