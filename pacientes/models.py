from django.db import models
from usuarios.models import Usuario

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimente = models.DateField()
    endereco = models.TextField()

    def __str__(self):
        return self.usuario.username
