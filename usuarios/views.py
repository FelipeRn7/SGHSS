from rest_framework import generics, permissions
from .models import Usuario
from .serializers import UsuarioSerializer
from .permissions import IsAdminUserType

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUserType]
    