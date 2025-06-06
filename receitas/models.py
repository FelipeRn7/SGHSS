from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

class ReceitaDigital(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)
    medicamentos = models.TextField()

    def __str__(self):
        return f"Receita de {self.paciente.usuario.username} por {self.profissional.usuario.username}" 
    