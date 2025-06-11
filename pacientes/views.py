from rest_framework import generics, permissions
from .models import Paciente
from .serializers import PacienteSerializer
from usuarios.permissions import IsAdminUserType

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAdminUserType]

class PacienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permissions_classes = [IsAdminUserType]
