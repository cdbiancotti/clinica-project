from . import views
from django.urls import path

app_name = 'usuarios'

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.log_in, name="log_in"),
    path('logout', views.log_in, name="log_out")
]
