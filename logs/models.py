from django.db import models
from usuarios.models import Usuario

# Modelo que representa um log de atividade no sistema
class LogSistema(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True) # Usuário que realizou a ação
    acao = models.TextField() # Descrição da ação realizada
    data_hora = models.DateTimeField(auto_now_add=True) # Data e hora do registro
    ip = models.GenericIPAddressField() # Endereço IP de onde partiu a ação

    def __str__(self):
        return f"{self.usuario.username if self.usuario else 'Sistema'} - {self.data_hora}"
