from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.index, name="index"),
    path('perfil', views.perfil, name="perfil"),
    path('login', views.log_in, name="log_in"),
    path('logout', views.log_out, name="log_out")
]
