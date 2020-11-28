from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Paciente

# Create your views here.

def turnos(request):
    return render(request, 'turnos.html')


def pacientes(request):
    # pacientes = Paciente.objects.all()
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']

        pacientes = Paciente.objects.filter(nombre=nombre)

    return render(request, 'pacientes.html', {
        'pacientes': pacientes
    })