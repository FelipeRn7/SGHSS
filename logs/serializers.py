from rest_framework import serializers
from .models import LogSistema
from usuarios.models import Usuario

# Serializador para o modelo LogSistema
class LogSerializer(serializers.ModelSerializer):
    # Campo para associar o usuário via ID
    usuario_id = serializers.PrimaryKeyRelatedField(
                 queryset=Usuario.objects.all(), source='usuario', 
                 write_only=True)

    class Meta:
        model = LogSistema
        fields = ['id', 'usuario_id', 'acao', 'ip']

    # Personaliza a saída da API com nome do usuário e data formatada
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['usuario'] = instance.usuario.username if instance.usuario else 'Sistema'
        data['data_hora'] = instance.data_hora.isoformat()
        return data
