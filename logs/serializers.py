from rest_framework import serializers
from .models import Log
from usuarios.models import Usuario

class LogSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(
                 queryset=Usuario.objects.all(), source='usuario', 
                 write_only=True)

    class Meta:
        model = Log
        fields = ['id', 'usuario_id', 'acao', 'descricao', 'data_hora']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['usuario'] = instance.usuario.username
        return data
