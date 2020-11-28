from django.contrib import admin
from .models import Paciente, EstadoTurno, Turno # EstadoPedido,Observacion,
# Register your models here.


admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(EstadoTurno)
# admin.site.register(EstadoPedido)
# admin.site.register(Observacion)