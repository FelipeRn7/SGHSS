from django.urls import path
from .views import ConsultaListCreateView, ConsultaDetailView

urlpatterns = [
    path('consultas/', ConsultaListCreateView.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', ConsultaDetailView.as_view(), name='consulta-detail'),
]