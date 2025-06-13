from django.urls import path
from .views import ReceitaDigitalListCreateView, ReceitaDigitalDetailView

urlpatterns = [
    path('receitas/', ReceitaDigitalListCreateView.as_view(), name='receita-list-create'),
    path('receitas/<int:pk>/', ReceitaDigitalDetailView.as_view(), name='receita-detail'),
]