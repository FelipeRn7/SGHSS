from django.db import models
from usuarios.models import Usuario

class LogSistema(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    acao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.usuario.username if self.usuario else 'Sistema'} - {self.data_hora}"
