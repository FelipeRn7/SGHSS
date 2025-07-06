from rest_framework import serializers
from .models import ReceitaDigital
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

# Serializer para o modelo ReceitaDigital, define os campos que serão expostos na API
class ReceitaDigitalSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(), source='paciente', write_only=True
    )
    profissional_id = serializers.PrimaryKeyRelatedField(
        queryset=ProfissionalSaude.objects.all(), source='profissional', write_only=True
    )

    class Meta:
        model = ReceitaDigital
        fields = ['id', 'paciente_id', 'profissional_id', 'data_emissao', 'medicamentos']

    # Customização da representação para incluir nomes de usuário
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['paciente'] = instance.paciente.usuario.username
        data['profissional'] = instance.profissional.usuario.username
        return data            