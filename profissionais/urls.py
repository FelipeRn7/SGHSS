from django.urls import path
from .views import ProfissionalListCreateView, ProfissionalDetailView

# Rotas para gerenciar profissionais da saúde
urlpatterns = [
    path('profissionais/', ProfissionalListCreateView.as_view(), name='profissional-list-create'),
    path('profissionais/<int:pk>/', ProfissionalDetailView.as_view(), name='profissional-detail'),
]


