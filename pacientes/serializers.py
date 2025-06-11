from rest_framework import serializers
from .models import Paciente
from usuarios.models import Usuario

class PacienteSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), source='usuario', write_only=True
    )

    class Meta:
        model = Paciente
        fields = ['id', 'usuario_id', 'cpf', 'data_nascimento', 'endereço']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['usuario'] = {
            "id": instance.usuario.id,
            "username": instance.usuario.username,
            "email": instance.usuario.email,
            "tipo": instance.usuario.tipo
        }
        return data