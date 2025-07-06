from django.urls import path
from .views import SuprimentoListCreateView, SuprimentoDetailView

# Endpoints de suprimentos
urlpatterns = [
    path('suprimentos/', SuprimentoListCreateView.as_view(), name='suprimento-list-create'),
    path('suprimentos/<int:pk>/', SuprimentoDetailView.as_view(), name='suprimento-detail'),
]
