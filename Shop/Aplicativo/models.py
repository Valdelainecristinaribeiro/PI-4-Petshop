from django.db import models 

# Create your models here.

class VeterinarioCadastroModel(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cidade = models.CharField('cidade',max_length=100, default = 'cidade')
    estado = models.CharField(max_length=3)
    telefone = models.CharField(max_length=15)
    crmv = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

class cadastroTutorModel(models.Model):
    nometutor = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField('cidade',max_length=100, default = 'cidade')
    estado = models.CharField(max_length=3)
    telefone = models.CharField(max_length=15)
    password= models.CharField('password', max_length=20, default="passord")
    cpf= models.CharField('cpf',max_length=11,default='cpf')

class cadastroAnimalModel(models.Model):
    nomepet = models.CharField(max_length=200)
    especie = models.CharField(max_length=200)
    porte = models.CharField(max_length=200)
    raca = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    sexo = models.CharField(max_length=200)
    datanascimento = models.DateField(max_length=200)
    cpftutor = models.CharField(max_length=200)
