from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Paciente, Turno, EstadoTurno, Observacion
from django.contrib.auth.models import User
from datetime import date

# Create your views here.

def turnos(request):
    grupos = request.user.groups.all()
    if len(grupos) > 0:
        grupo = grupos[0].name
    busqueda_realizada = False
    turnos = []
    pacientes = Paciente.objects.all()
    medicos = User.objects.filter(groups=2)
    estados = EstadoTurno.objects.all()
    if request.method == 'POST':
        filtros = {}
        for key in request.POST.keys():
            campos = ['medico', 'paciente', 'estado', 'fecha']
            if key in campos:
                dato = request.POST[key]
                if bool(dato):
                    filtros[key] = dato

        turnos = Turno.objects.filter(**filtros)
        busqueda_realizada = True

    return render(request, 'turnos.html', {
        'turnos': turnos,
        'pacientes': pacientes,
        'medicos': medicos,
        'estados': estados,
        'busqueda_realizada': busqueda_realizada,
    })

def turno(request, turno_id):
    turno = None
    fecha_nacimiento = None
    fecha_turno = None
    hora_turno = None
    pacientes = Paciente.objects.all()
    medicos = User.objects.filter(groups=2)
    estados = EstadoTurno.objects.all()
    if turno_id != 0:
        turno = Turno.objects.get(pk=turno_id)
        fecha_turno = turno.fecha.strftime('%Y-%m-%d')
        hora_turno = turno.hora.strftime('%H:%M')
    return render(request, 'turno.html', {
        'turno': turno,
        'turno_id': turno_id,
        'fecha_turno': fecha_turno,
        'hora_turno': hora_turno,
        'pacientes': pacientes,
        'medicos': medicos,
        'estados': estados,
    })

def crear_turno(request, turno_id):
    if request.method == 'POST':        
        datos_actualizados = {}
        for key in request.POST.keys():
            campos = ['medico', 'paciente', 'estado', 'fecha', 'hora']
            if key in campos:
                dato = request.POST[key]
                if bool(dato):
                    if key == 'medico':
                        datos_actualizados[key] = User.objects.get(id=dato)
                    elif key == 'paciente':
                        datos_actualizados[key] = Paciente.objects.get(id=dato)
                    elif key == 'estado':
                        datos_actualizados[key] = EstadoTurno.objects.get(id=dato)
                    else:
                        datos_actualizados[key] = dato

        if turno_id != 0:
            turno = Turno.objects.get(pk=turno_id)
            turno = {**turno, **datos_actualizados}
            turno.save()
        else:
            Turno.objects.create(**datos_actualizados)
        return redirect('web_app:turnos')

def eliminar_turno(request, turno_id):
    turno = Turno.objects.get(id=turno_id)
    turno.delete()
    return redirect('web_app:turnos')

def pacientes(request):
    grupos = request.user.groups.all()
    grupo = ''
    if len(grupos) > 0:
        grupo = grupos[0].name
    busqueda_realizada = False
    pacientes = []
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        filtros = {}
        if bool(nombre):
            filtros['nombre__contains'] = nombre
        if bool(apellido):
            filtros['apellido__contains'] = apellido
        pacientes = Paciente.objects.filter(**filtros)
        if grupo == 'medico':
            filtros_fecha = {}
            dia = request.POST['dia']
            mes = request.POST['mes']
            ano = request.POST['ano']
            if bool(dia):
                filtros_fecha['fecha__day'] = dia
            if bool(mes):
                filtros_fecha['fecha__month'] = mes
            if bool(ano):
                filtros_fecha['fecha__year'] = ano
            turnos = Turno.objects.filter(medico=request.user.id,**filtros_fecha)
            pacientes_turnos = turnos.values_list('paciente', flat=True)
            pacientes = pacientes.filter(id__in=pacientes_turnos)
        busqueda_realizada = True

    return render(request, 'pacientes.html', {
        'pacientes': pacientes,
        'busqueda_realizada': busqueda_realizada
    })

def paciente(request, paciente_id):
    paciente = None
    fecha_nacimiento = None
    historia_medica = None
    if paciente_id != 0:
        paciente = Paciente.objects.get(pk=paciente_id)
        fecha_nacimiento = paciente.nacimiento.strftime('%Y-%m-%d')
        historia_medica = Observacion.objects.filter(paciente=paciente).reverse()
    return render(request, 'paciente.html', {
        'paciente': paciente,
        'paciente_id': paciente_id,
        'fecha_nacimiento': fecha_nacimiento,
        'historia_medica': historia_medica,
    })

def crear_paciente(request, paciente_id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        nacimiento = request.POST['nacimiento']
        dni = request.POST['dni']
        if paciente_id != 0:
            paciente = Paciente.objects.get(pk=paciente_id)
            paciente.nombre = nombre
            paciente.apellido = apellido
            paciente.edad = edad
            paciente.dni = dni
            paciente.nacimiento = nacimiento
            paciente.save()
        else:
            Paciente.objects.create(nombre=nombre, apellido=apellido, edad=edad, dni=dni,nacimiento=nacimiento)
        return redirect('web_app:pacientes')
        
def nueva_observacion(request, paciente_id):
    grupos = request.user.groups.all()
    grupo = ''
    if len(grupos) > 0:
        grupo = grupos[0].name
    if grupo == 'medico' and request.method == 'POST':
        paciente = Paciente.objects.get(id=paciente_id)
        observacion = request.POST['observacion']
        if bool(observacion):
            Observacion.objects.create(descripcion=observacion,fecha=date.today(),medico=request.user,paciente=paciente)
    return redirect('web_app:paciente', paciente_id)