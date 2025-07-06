from django.db import models
from usuarios.models import Usuario

# Modelo que representa um profissional da saúde
class ProfissionalSaude(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario.username