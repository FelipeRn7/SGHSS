from rest_framework import generics, permissions
from .models import Consulta
from .serializers import ConsultaSerializer
from usuarios.permissions import IsAdminUserType

class ConsultaListCreateView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAdminUserType]

class ConsultaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAdminUserType]

    