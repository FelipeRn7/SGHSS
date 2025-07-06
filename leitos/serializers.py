from rest_framework import serializers
from .models import LeitoHospitalar
from pacientes.models import Paciente

# Serializador para o modelo LeitoHospitalar
class LeitoSerializer(serializers.ModelSerializer):
     # Campo para associar o ID de um paciente ao leito (opcional)
    paciente_id = serializers.PrimaryKeyRelatedField(
                  queryset=Paciente.objects.all(), source='paciente', 
                  write_only=True, required=False)

    class Meta:
        model = LeitoHospitalar
        fields = ['id', 'codigo', 'ocupado', 'paciente_id']

    # Personaliza a saída da API para mostrar o nome de usuário do paciente
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['paciente'] = instance.paciente.usuario.username if instance.paciente else None
        return data
