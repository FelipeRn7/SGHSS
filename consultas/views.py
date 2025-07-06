from rest_framework import generics, permissions
from .models import Consulta
from .serializers import ConsultaSerializer
from usuarios.permissions import IsAdminUserType

# Views para o aplicativo de consultas
class ConsultaListCreateView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAdminUserType] # Acesso permitido apenas para administradores

# View para recuperar, atualizar ou excluir uma consulta específica
class ConsultaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAdminUserType]

    