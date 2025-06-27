from rest_framework import generics, permissions
from .models import LogSistema
from .serializers import LogSerializer
from usuarios.permissions import IsAdminUserType

class LogListCreateView(generics.ListCreateAPIView):
    queryset = LogSistema.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserType]

