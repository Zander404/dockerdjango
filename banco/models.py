from django.db import models


# Create your models here.

class Banco(models.Model):

  cod = models.CharField(
    max_length=5,
    null=False,
    blank=False,
    unique=True,

    )

  name = models.TextField(
    max_length=255,
    null=False,
    blank=False,
    
    )

  cep = models.CharField(
    max_length=11,
    null=False,
    blank=False,
    )
  



class Agencia(models.Model):
  pk_Agencia = models.TextField(max_length = 8)
  nome_Agencia = models.CharField(max_length=100)
  telefone_Agencia = models.TextField(max_length=11)
  cep_Agencia = models.TextField(default=0, max_length=8)