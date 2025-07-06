from rest_framework import generics, permissions
from .models import Paciente
from .serializers import PacienteSerializer
from usuarios.permissions import IsAdminUserType

# View para listar e criar pacientes, apenas para administradores
class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAdminUserType]

# View para detalhar, atualizar ou remover um paciente
class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAdminUserType]
