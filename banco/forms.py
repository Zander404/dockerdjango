from email.policy import default
from django import forms 

class BancoForm(forms.Form):

    cod = forms.IntegerField(
        label='Codigo do Banco: ',
        max_value=9999,
        unique=True,

    )

    nome_Banco= forms.CharField(
        label = 'Nome do Banco: ',
        max_length=100,
        unique=True,
        )


class AgenciaForm(forms.Form):
   
    num_Agecia = forms.IntegerField(
        label = 'Numero da Agencia: ',
        max_value=999,
        unique=True,

    )

