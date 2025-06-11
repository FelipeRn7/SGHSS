from rest_framework import serializers
from .models import Consulta
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

class ConsultaSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(
                queryset=Paciente.objects.all(), source='paciente', write_only=True)
    
    profissional_id = serializers.PrimaryKeyRelatedField(
                queryset=ProfissionalSaude.objects.all(), source='profissional', write_only=True)

    class Meta:
        model = Consulta
        fields = ['id', 'paciente_id', 'profissional_id', 'data', 'horario', 'status', 'criado_em']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['paciente'] = {
            'id': instance.paciente.id,
            'usuario': instance.paciente.usuario.username
        }
        data['profissional'] = {
            'id': instance.profissional.id,
            'usuario': instance.profissional.usuario.username
        }
        return data 