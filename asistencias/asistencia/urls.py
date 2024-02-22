from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_asistencia, name='asistencia'),
    path('personas', views.listar_personas, name='personas'),
]