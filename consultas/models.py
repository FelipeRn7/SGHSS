from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=20, default='Agendada')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.data} - {self.profissional.usuario.username} com {self.paciente.usuario.username}"
    
class ConsultaSuprimento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    suprimento = models.ForeignKey('suprimentos.Suprimento', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade} X {self.suprimento.nome} na consulta {self.consulta.id}"