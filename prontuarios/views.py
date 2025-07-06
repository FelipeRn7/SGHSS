from rest_framework import generics, permissions
from .models import Prontuario
from .serializers import ProntuarioSerializer
from usuarios.permissions import IsProfissionalUserType

# Apenas profissionais podem criar e visualizar prontuários
class ProntuarioListCreateView(generics.ListCreateAPIView):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = [IsProfissionalUserType]

class ProntuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
    permission_classes = [IsProfissionalUserType]

    