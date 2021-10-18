from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from subir_tarea.models import Tarea


@login_required()
def materias(request):
    """Atiende la petición GET /"""
    return render(request, "materias/materias.html")


@login_required()
def lengua_materna(request):
    """Atiende la petición GET /"""
    #t_lenmaterna = Tarea.objects.filter()
    return render(request, "materias/lengua_materna.html")