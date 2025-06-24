from rest_framework import serializers
from .models import ProfissionalSaude
from usuarios.models import Usuario

class ProfissionalSaudeSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=Usuario.objects.all(), source='usuario', write_only=True
    )

    class Meta:
        model = ProfissionalSaude
        fields = ['id', 'usuario_id', 'especialidade', 'crm']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['usuario'] = {
            "id": instance.usuario.id,
            "username": instance.usuario.username,
            "email": instance.usuario.email,
            "tipo": instance.usuario.tipo
        }
        return data
