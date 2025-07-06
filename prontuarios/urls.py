from django.urls import path
from .views import ProntuarioListCreateView, ProntuarioDetailView

# Endpoints de prontuário
urlpatterns = [
    path('prontuarios/', ProntuarioListCreateView.as_view(), name='prontuario-list-create'),
    path('prontuarios/<int:pk>/', ProntuarioDetailView.as_view(), name='prontuario-detail'),
]