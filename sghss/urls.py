from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),
    path('api/', include('pacientes.urls')),
    path('api/', include('consultas.urls')),
    path('api/', include('prontuarios.urls')),
    path('api/', include('receitas.urls')),
    path('api/', include('leitos.urls')),
    path('api/', include('suprimentos.urls')),
    path('api/logs/', include('logs.urls')),
    path('api/', include('profissionais.urls')),
]
