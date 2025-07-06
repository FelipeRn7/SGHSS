from django.db import models

# Representa materiais médicos com data de entrada, saída e quantidade
class Suprimento(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0)
    ultima_reposicao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome