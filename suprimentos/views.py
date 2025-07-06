from rest_framework import generics
from .models import Suprimento
from .serializers import SuprimentoSerializer
from usuarios.permissions import IsAdminUserType

# Gerenciado apenas por usuários administradores
class SuprimentoListCreateView(generics.ListCreateAPIView):
    queryset = Suprimento.objects.all()
    serializer_class = SuprimentoSerializer
    permission_classes = [IsAdminUserType]

class SuprimentoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Suprimento.objects.all()
    serializer_class = SuprimentoSerializer
    permission_classes = [IsAdminUserType]

