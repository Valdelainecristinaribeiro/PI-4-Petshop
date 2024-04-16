from django.shortcuts import render, redirect
from Aplicativo.models import VeterinarioCadastro

def index(request):
    return render(request, 'index.html')
def cadastro(request):
    return render(request, 'cadastro.html')
def login(request):
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
    vet = VeterinarioCadastro.objects.get(id=id)
    vet.delete()
    return redirect(index)


#TUTOR

#defsalvartutor(request):
    #vnome = request.POST.get("nome")

#def salvaranimal(request):
    #vnome = request.POST.get("nome")


#ANIMAIS