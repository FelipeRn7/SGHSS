from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

# Modelo principal representando uma consulta médica
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE) # Ligação com o paciente
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE) # Ligação com o profissional de saúde
    data = models.DateField() # Data da consulta
    horario = models.TimeField() # Horário da consulta
    status = models.CharField(max_length=20, default='Agendada') # Estado da consulta
    criado_em = models.DateTimeField(auto_now_add=True) # Data de criação do registro

    def __str__(self):
        return f"{self.data} - {self.profissional.usuario.username} com {self.paciente.usuario.username}"

# Modelo para associar suprimentos a uma consulta    
class ConsultaSuprimento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    suprimento = models.ForeignKey('suprimentos.Suprimento', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade} X {self.suprimento.nome} na consulta {self.consulta.id}"