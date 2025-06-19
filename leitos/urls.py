from django.urls import path
from .views import LeitoListCreateView, LeitoDetailView

urlpatterns = [
    path('leitos/', LeitoListCreateView.as_view(), name='leito-list-create'),
    path('leitos/<int:pk>/', LeitoDetailView.as_view(), name='leito-detail'),
]
