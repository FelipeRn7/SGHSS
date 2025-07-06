from rest_framework import serializers
from .models import Paciente
from usuarios.models import Usuario

# Serializador do modelo Paciente para entrada/saída de dados via API
class PacienteSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), source='usuario', write_only=True
    )

    class Meta:
        model = Paciente
        fields = ['id', 'usuario_id', 'cpf', 'data_nascimento', 'endereco']

    # Customiza a saída do JSON para incluir informações do usuário
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['usuario'] = {
            "id": instance.usuario.id,
            "username": instance.usuario.username,
            "email": instance.usuario.email,
            "tipo": instance.usuario.tipo
        }
        return data