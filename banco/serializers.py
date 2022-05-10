from banco.models import Banco
from rest_framework import serializers

class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ['cod','name','cep', 'id']

