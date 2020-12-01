from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=64,null=False)
    apellido = models.CharField(max_length=64,null=False)
    dni = models.IntegerField(null=False,unique=True)
    edad = models.IntegerField(null=False)
    nacimiento = models.DateField(null=False)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class EstadoTurno(models.Model):
    descripcion = models.CharField(max_length=64,null=False,unique=True)

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

class Observacion(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=150)
    medico = models.ForeignKey(User, on_delete=models.PROTECT, related_name="medicoObservacion")
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name="pacienteObservacion")
    

class EstadoPedido(models.Model):
    descripcion = models.CharField(max_length=64)

class LadoLente(models.Model):
    descripcion = models.CharField(max_length=64)

class Clasificacion(models.Model):
    descripcion = models.CharField(max_length=64)

class TipoLente(models.Model):
    descripcion = models.CharField(max_length=64)

class TipoPago(models.Model):
    descripcion = models.CharField(max_length=64)

class Producto(models.Model):
    precio = models.FloatField()
    nombre = models.CharField(max_length=64)
    detalle = models.CharField(max_length=152)
    clasificacion = models.ForeignKey(LadoLente,on_delete=models.PROTECT, related_name="productoClasificacion")
    lado_lente = models.ForeignKey(LadoLente,on_delete=models.PROTECT,null=True, related_name="productoLenteLado")
    tipo_lente = models.ForeignKey(TipoLente,on_delete=models.PROTECT, null=True,related_name="productoLenteTipo")
    armazon = models.BooleanField()

class Pedido(models.Model):
    productos = models.ManyToManyField(Producto, blank=True, related_name="productosPedidos")
    estado = models.ForeignKey(EstadoPedido,on_delete=models.PROTECT,null=True, related_name="pedidoEstado")
    tipo_pago = models.ForeignKey(TipoPago,on_delete=models.PROTECT,null=True, related_name="pedidoTipoPago")
    subtotal = models.FloatField()
