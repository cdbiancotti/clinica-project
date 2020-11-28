from django.urls import path
from . import views

app_name = 'web_app'

urlpatterns = [
    path('turnos', views.turnos, name="turnos"),
    path('pacientes', views.pacientes, name="pacientes"),
]
