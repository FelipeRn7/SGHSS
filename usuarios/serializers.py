from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.password_validation import validate_password

class UsuarioSerializer(serializers.ModelSerializer):
    password: serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'tipo']

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            tipo=validated_data['tipo']
        )
        return user