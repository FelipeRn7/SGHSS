from rest_framework import serializers
from .models import Suprimento

class SuprimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suprimento
        fields = ['id', 'nome', 'tipo', 'quantidade', 'descricao', 'data_entrada', 'data_saida']
