from django.contrib import admin
from django.urls import path
from . import views

#from Shop.Aplicativo.models import VeterinarioCadastro 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cadastroVet/', views.cadastroVet, name='cadastroVet'),
    path('atualizacaoVet/', views.atualizacaoVet, name='atualizacaoVet'),
    path('updateVet/<int:id>/', views.updateVet, name='updateVet'),
    path('deleteVet/<int:id>', views.deleteVet, name='deleteVet'),
    path('cadastroTutor/', views.cadastroTutor, name='cadastroTutor'),
    path('cadastroAnimal/', views.cadastroAnimal, name='cadastroAnimal')
]