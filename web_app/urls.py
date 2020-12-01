from django.urls import path
from . import views

app_name = 'web_app'

urlpatterns = [
    path('turnos', views.turnos, name="turnos"),
    path('turnos/<int:turno_id>', views.turno, name="turno"),
    path('turnos/<int:turno_id>/edicion', views.crear_turno, name="crear_turno"),
    path('turnos/<int:turno_id>/eliminar', views.eliminar_turno, name="eliminar_turno"),
    path('pedidos', views.pedidos, name="pedidos"),
    path('pedidos/<int:pedido_id>', views.pedido, name="pedido"),
    path('pedidos/<int:pedido_id>/edicion', views.crear_pedido, name="crear_pedido"),
    path('pedidos/<int:pedido_id>/eliminar', views.eliminar_pedido, name="eliminar_pedido"),
    path('pacientes', views.pacientes, name="pacientes"),
    path('pacientes/<int:paciente_id>', views.paciente, name="paciente"),
    path('pacientes/<int:paciente_id>/edicion', views.crear_paciente, name="crear_paciente"),
    path('pacientes/<int:paciente_id>/edicion/nueva_observacion', views.nueva_observacion, name="nueva_observacion"),
]
