from django.urls import path
from .views import ConsultaListCreateView, ConsultaDetailView

# URLs para o aplicativo de consultas
urlpatterns = [
    path('consultas/', ConsultaListCreateView.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', ConsultaDetailView.as_view(), name='consulta-detail'),
]