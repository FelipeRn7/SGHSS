from rest_framework import generics
from .models import Leito
from .serializers import LeitoSerializer
from usuarios.permissions import IsAdminUserType  

class LeitoListCreateView(generics.ListCreateAPIView):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAdminUserType]

class LeitoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAdminUserType]

