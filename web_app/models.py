from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    edad = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class EstadoTurno(models.Model):
    descripcion = models.CharField(max_length=64)

    def __str__(self):
        return f'Id: {self.id} - Descripcion: {self.descripcion}'

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.ForeignKey(EstadoTurno, on_delete=models.PROTECT, related_name="estadoTurno")
    medico = models.ForeignKey(User, on_delete=models.PROTECT, related_name="medicoTurno")
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name="pacienteTurno")

    def __str__(self):
        return f'Fecha: {self.fecha} - Hora: {self.hora} - Paciente: {self.paciente} - Medico: {self.medico}'
    

# class EstadoPedido(models.Model):
#     descripcion: models.CharField(max_length=64)


# class Observacion(models.Model):
#     fecha = models.DateField()
#     descripcion = models.CharField()
#     medico = models.ForeignKey(User, on_delete=models.PROTECT, related_name="medicoObservacion")
#     paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name="pacienteObservacion")