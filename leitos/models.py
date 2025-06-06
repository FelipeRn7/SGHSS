from django.db import models
from pacientes.models import Paciente

class LeitoHospitalar(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    ocupado = models.BooleanField(default=False)
    paciente = models.OneToOneField(Paciente, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Leito {self.codigo} - {'Ocupado' if self.ocupado else 'Disponível'}"