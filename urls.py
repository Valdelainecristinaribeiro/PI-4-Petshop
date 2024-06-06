from django.contrib import admin
from django.urls import path
from . import views

#from Shop.Aplicativo.models import VeterinarioCadastro 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cadastroVet/', views.cadastroVet, name='cadastroVet'),
    path('atualizacaoVet/', views.atualizacaoVet, name='atualizacaoVet'),
    path('atualizacaoTutor/', views.atualizacaoTutor, name='atualizacaoTutor'),
    path('updateTutor/<int:id>/', views.updateTutor, name='updateTutor'),
    path('atualizacaoAnimal/', views.atualizacaoAnimal, name='atualizacaoAnimal'),
    path('updateAnimal/<int:id>/', views.updateAnimal, name='updateAnimal'),
    path('deleteTutor/<int:id>', views.deleteTutor, name='deleteTutor'),
    path('deleteAnimal/<int:id>', views.deleteAnimal, name='deleteAnimal'),
    path('updateVet/<int:id>/', views.updateVet, name='updateVet'),
    path('deleteVet/<int:id>', views.deleteVet, name='deleteVet'),
    path('cadastroTutor/', views.cadastroTutor, name='cadastroTutor'),
    path('cadastroAnimal/', views.cadastroAnimal, name='cadastroAnimal'),
    path('criar_agendamento/', views.criar_agendamento, name='criar_agendamento'),
    path('dashatualizacao/', views.dashatualizacao, name='dashatualizacao'),
    path('home/', views.home, name='home'),
    path('cadastroServicos/', views.cadastroServicos, name='cadastroServicos'),
    path('visualizar_agendamentos/', views.visualizar_agendamentos, name='visualizar_agendamentos'),
    path('cadastrarVacinas/', views.cadastrarVacinas, name='cadastrarVacinas'),
    path('criarservicos/', views.criarservicos, name='criarservicos')

]