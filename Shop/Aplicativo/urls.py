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
    path('updateVet/<int:id>', views.updateVets, name='updateVet'),
    path('deleteVet/<int:id>', views.deleteVet, name='deleteVet'),
    path('cadastroTutor/', views.cadastroTutor, name='cadastroTutor')

]