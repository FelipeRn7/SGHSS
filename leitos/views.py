from rest_framework import generics
from .models import LeitoHospitalar
from .serializers import LeitoSerializer
from usuarios.permissions import IsAdminUserType  

class LeitoListCreateView(generics.ListCreateAPIView):
    queryset = LeitoHospitalar.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAdminUserType]

class LeitoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeitoHospitalar.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAdminUserType]

