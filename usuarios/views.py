from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('usuarios:log_in'))
    return HttpResponseRedirect(reverse('usuarios:log_in'))


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('usuarios:index'))
        else:
            return render(request, 'usuarios/login.html', {
                'mensaje': 'Credenciales no validas.'
            })
    return render(request, 'usuarios/login.html')


def log_out(request):
    logout(request)
    return render(request, 'usuarios/login.html', {
        'mensaje': 'Probando el template'
    })
