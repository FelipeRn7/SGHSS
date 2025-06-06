from django.db import models
from usuarios.models import Usuario

class ProfissionalSaude(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100)
    conselho = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario.username