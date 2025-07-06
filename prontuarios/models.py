from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

# Modelo que representa o prontuário clínico de um paciente
class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField() # Detalhes clínicos

    def __str__(self):
        return f"Prontuário de {self.paciente.usuario.username} em {self.data_registro.date()}"