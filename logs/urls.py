from django.urls import path
from .views import LogListCreateView

# URLs do módulo de logs
urlpatterns = [
    path('', LogListCreateView.as_view(), name='log-list'),
]
