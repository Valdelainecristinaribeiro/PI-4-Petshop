from pyexpat.errors import messages
from django.shortcuts import render, redirect
from Aplicativo.forms import cadastroTutorForm
#from Aplicativo.forms import TutoresCadastroForm
from .models import VeterinarioCadastro, cadastroTutorModel
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



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 
    else:
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user:
            login_django(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    
    return render(request, 'login.html')  


def cadastroVet(request):
    return render(request, 'cadastroVet.html')


#VETERINARIO

#salvando no banco de dados
def salvarVet(request):
    vnome = request.POST.get("nome")
    vemail = request.POST.get("email")
    vendereco = request.POST.get("endereco")
    vbairro = request.POST.get("bairro")
    vnumero = request.POST.get("numero")
    vcidade = request.POST.get("cidade")
    vestado = request.POST.get("estado")
    vtelefone = request.POST.get("telefone")
    vcrmv = request.POST.get("crmv")
    vsenha = request.POST.get("senha")
    VeterinarioCadastro.objects.create(nome=vnome, email=vemail, endereco=vendereco, bairro=vbairro, numero=vnumero, cidade=vcidade, estado=vestado, telefone=vtelefone, 
                                       crmv=vcrmv, senha=vsenha)
    #mostra tudo que tem salvo no banco de dados na pagina cadastroVet
    veterinario = VeterinarioCadastro.objects.all()
    return render(request, "cadastroVet.html", {"cadastroveterinario" : veterinario})

def editarVet(request, id):
    vet = VeterinarioCadastro.objects.get(id=id)
    return render(request, "updateVet.html", {"Veterinario" : vet})
#TERMINAR O UPDATE (ERRO)
def updateVet(request, id):
    vnome = request.POST.get("nome")
    vemail = request.POST.get("email")
    vendereco = request.POST.get("endereco")
    vbairro = request.POST.get("bairro")
    vnumero = request.POST.get("numero")
    vcidade = request.POST.get("cidade")
    vestado = request.POST.get("estado")
    vtelefone = request.POST.get("telefone")
    vcrmv = request.POST.get("crmv")
    vsenha = request.POST.get("senha")
    vet = VeterinarioCadastro.objects.get(id=id)
    vet.nome = vnome
    vet.email = vemail
    vet.endereco = vendereco
    vet.bairro = vbairro
    vet.numero = vnumero
    vet.cidade = vcidade
    vet.estado = vestado
    vet.telefone = vtelefone
    vet.crmv = vcrmv
    vet.senha = vsenha
    vet.save()
    return redirect(index)


def deleteVet(request, id):
    return redirect("deleteVet")


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
        tutor.save()
        tutor = User.objects.create_user(username= form.data['email'], password = form.data ['password'])
        tutor.save()
    return render(request, 'cadastroTutor.html')




#TUTOR

#defsalvartutor(request):
    #vnome = request.POST.get("nome")

#def salvaranimal(request):
    #vnome = request.POST.get("nome")


#ANIMAIS