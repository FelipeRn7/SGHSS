from rest_framework import generics
from .models import ReceitaDigital
from .serializers import ReceitaDigitalSerializer
from usuarios.permissions import IsProfissionalUserType

class ReceitaDigitalListCreateView(generics.ListCreateAPIView):
    queryset = ReceitaDigital.objects.all()
    serializer_class = ReceitaDigitalSerializer
    permission_classes = [IsProfissionalUserType]

class ReceitaDigitalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReceitaDigital.objects.all()
    serializer_class = ReceitaDigitalSerializer
    permission_classes = [IsProfissionalUserType]