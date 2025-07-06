from django.db import models
from pacientes.models import Paciente

# Modelo que representa um leito hospitalar
class LeitoHospitalar(models.Model):
    codigo = models.CharField(max_length=20, unique=True) # Código identificador do leito
    ocupado = models.BooleanField(default=False) # Indica se o leito está ocupado
    paciente = models.OneToOneField(Paciente, null=True, blank=True, 
                                    on_delete=models.SET_NULL) # Relaciona o leito a um paciente, se estiver ocupado

    def __str__(self):
        return f"Leito {self.codigo} - {'Ocupado' if self.ocupado else 'Disponível'}"