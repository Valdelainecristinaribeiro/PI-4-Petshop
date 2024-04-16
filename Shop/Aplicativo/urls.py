from os import name
from django.urls import path
from Aplicativo import views
#from Shop.Aplicativo.models import VeterinarioCadastro 

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('cadastroVet/', views.cadastroVet, name='cadastroVet'),


    path('salvar/', views.salvarVet, name='salvarVet'),
    path('editarVet/<int:id>', views.editarVet, name='editarVet'),#chamar link para editar
    path('updateVet/<int:id>', views.updateVet, name='updateVet'),#tela de editar
    path('deleteVet/<int:id>', views.deleteVet, name='deleteVet'),
]