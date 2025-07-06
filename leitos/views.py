from rest_framework import generics
from .models import LeitoHospitalar
from .serializers import LeitoSerializer
from usuarios.permissions import IsAdminUserType  

# View para listar todos os leitos e permitir criação de novos
class LeitoListCreateView(generics.ListCreateAPIView):
    queryset = LeitoHospitalar.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAdminUserType]  # Apenas administradores têm permissão

# View para obter, atualizar ou deletar um leito específico
class LeitoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeitoHospitalar.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAdminUserType]

