from django.db import models
from usuarios.models import Usuario

# Modelo de dados que representa um paciente no sistema
class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE) # Ligação direta com a tabela de usuários
    cpf = models.CharField(max_length=14, unique=True) # CPF único do paciente
    data_nascimento = models.DateField() # Data de nascimento
    endereco = models.TextField() # Endereço completo

    def __str__(self):
        return self.usuario.username
