from django.db import models 

# Create your models here.

class VeterinarioCadastro(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=3)
    telefone = models.CharField(max_length=15)
    crmv = models.CharField(max_length=20)
    senha = models.CharField(max_length=50)

class TutoresCadastro(models.Model):
    nometutor = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=3)
    telefone = models.CharField(max_length=15)


class Tutor(models.Model):
    nometutor = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    numero = models.IntegerField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20)
    