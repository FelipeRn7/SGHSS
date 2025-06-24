from rest_framework import generics, permissions
from .models import ProfissionalSaude
from .serializers import ProfissionalSaudeSerializer
from usuarios.permissions import IsAdminUserType

class ProfissionalListCreateView(generics.ListCreateAPIView):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserType]

class ProfissionalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSaudeSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserType]
