from rest_framework import serializers
from .models import LeitoHospitalar
from pacientes.models import Paciente

class LeitoSerializer(serializers.ModelSerializer):
    paciente_id = serializers.PrimaryKeyRelatedField(
                  queryset=Paciente.objects.all(), source='paciente', 
                  write_only=True, required=False)

    class Meta:
        model = LeitoHospitalar
        fields = ['id', 'numero', 'status', 'paciente_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['paciente'] = instance.paciente.usuario.username if instance.paciente else None
        return data
