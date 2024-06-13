from django.db import models 
from django.contrib.auth.models import User
# Create your models here.

class VeterinarioCadastroModel(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    cep=models.CharField(max_length=255, default='000000000')
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
    def __str__(self):
        return self.nomepet 



class ServicoModel(models.Model):
    nome = models.CharField(max_length=200, unique=True, default='Serviço Temporário')
    

    def __str__(self):
        return self.nome

class AgendamentoModel(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
        ('cancelado', 'Cancelado'),
    ]

    tutor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    animal = models.ForeignKey('cadastroAnimalModel', on_delete=models.CASCADE, default=1)
    servico = models.ForeignKey(ServicoModel, on_delete=models.CASCADE, default=1)
    data = models.DateField(default='2024-01-01')  # Valor padrão temporário
    horario = models.TimeField(default='12:00')  # Valor padrão temporário
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto')

    def __str__(self):
        return f'Tutor: {self.tutor} - Animal: {self.animal} - Serviço: {self.servico} - Data: {self.data} - Horário: {self.horario} - Status: {self.status}'
    
class cadastroVacinaModel(models.Model):
    vacina = models.CharField(max_length=200)
    datavacinado = models.DateField(max_length=200)
    nomeveterinario = models.CharField(max_length=200)
    proximavacina =  models.DateField(max_length=200)
    datavernifugo = models.DateField(max_length=200)
    produtovernifugo = models.CharField(max_length=200)
    dose = models.CharField(max_length=15)
    pesoanimal = models.CharField(max_length=15)

