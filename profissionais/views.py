from rest_framework import generics, permissions
from .models import ProfissionalSaude
from .serializers import ProfissionalSaudeSerializer
from usuarios.permissions import IsAdminUserType

# View para criação e listagem de profissionais (apenas para admins autenticados)
class ProfissionalListCreateView(generics.ListCreateAPIView):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserType]

# View para operações com instância específica do profissional
class ProfissionalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserType]
