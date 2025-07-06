from django.urls import path
from .views import PacienteListCreateView, PacienteDetailView

# Rotas da API para gerenciamento de pacientes
urlpatterns = [
    path('pacientes/', PacienteListCreateView.as_view(), name='paciente-list-create'),
    path('pacientes/<int:pk>/', PacienteDetailView.as_view(), name='paciente-detail'),
]