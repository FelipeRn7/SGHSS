from rest_framework import serializers
from .models import Suprimento

# Serializer para o modelo Suprimento, define os campos que serão expostos na API
class SuprimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suprimento
        fields = ['id', 'nome', 'quantidade', 'ultima_reposicao']
