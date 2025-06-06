from django.db import models

class Suprimento(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0)
    ultima_reposicao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome