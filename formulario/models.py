from django.db import models

# Create your models here.

PHONE_CHOICES = {
    ('0', 'Celular'),
    ('1', 'Fixo')
}


class Banco(models.Model):
    cod = models.DecimalField(
        primary_key=True,
        max_digits=3,
        decimal_places=0,
        null=False,
        blank=False,
        unique=True,

    )

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,

    )

    cep = models.DecimalField(
        max_digits=11,
        decimal_places=0,
        null=False,
        blank=False,
    )
    class Meta:
        db_table = "banco" 

    def __str__(self):
        return self.name


class Agencia(models.Model):
    cod = models.DecimalField(
        primary_key=True,
        max_digits=5,
        decimal_places=0,
        null=False,
        blank=False,
        unique=True,
    )

    name_Agencia = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    tipo_telefone = models.CharField(
        max_length=1,
        choices=PHONE_CHOICES,
    )

    telefone_Agencia = models.DecimalField(
        max_digits=11,
        decimal_places=0,
        blank=False,
        null=False,
        unique=True,
    )

    cep_agencia = models.DecimalField(
        max_digits=5,
        decimal_places=0,
        unique=True,
        null=False,
        blank=False,
    )

    cod_do_Banco = models.DecimalField(
        blank=False,
        null=False,
        max_digits=9,
        decimal_places=0,

    )
    class Meta:
        db_table = "agencia"

    def __str__(self):
        return self.nome

