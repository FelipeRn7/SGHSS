from rest_framework import generics
from .models import Log
from .serializers import LogSerializer
from usuarios.permissions import IsAdminUserType

class LogListView(generics.ListAPIView):
    queryset = Log.objects.all().order_by('-data_hora')
    serializer_class = LogSerializer
    permission_classes = [IsAdminUserType]

