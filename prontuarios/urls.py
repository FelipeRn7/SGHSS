from django.urls import path
from .views import ProntuarioListCreateView, ProntuarioDetailView

urlpatterns = [
    path('prontuarios/', ProntuarioListCreateView.as_view(), name='prontuario-list-create'),
    path('prontuarios/<int:pk>/', ProntuarioDetailView.as_view(), name='prontuario-detail'),
]