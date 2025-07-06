from rest_framework import serializers
from .models import Prontuario
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

# Serializador para prontuário
class ProntuarioSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(
        queryset=Paciente.objects.all(), source='paciente', write_only=True
    )

    profissional_id = serializers.PrimaryKeyRelatedField(
        queryset=ProfissionalSaude.objects.all(), source='profissional', write_only=True
    )

    class Meta:
        model = Prontuario
        fields = ['id', 'paciente_id', 'profissional_id', 'data_registro', 'descricao']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['paciente'] = instance.paciente.usuario.username
        data['profissional'] = instance.profissional.usuario.username
        return data