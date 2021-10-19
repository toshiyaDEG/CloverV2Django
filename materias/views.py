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


@login_required()
def ciencias_naturales(request):
    """Atiende la petición GET /"""
    tarea_cn = Tarea.objects.filter(materia_tarea__materia = "CN")

    return render(request, "materias/ciencias_naturales.html",{"tarea_cn":tarea_cn})


@login_required()
def desafios_matematicos(request):
    """Atiende la petición GET /"""
    
    return render(request, "materias/desafios_matematicos.html")


@login_required()
def educacion_civica(request):
    """Atiende la petición GET /"""
    
    return render(request, "materias/educacion_civica.html")


@login_required()
def educacion_fisica (request):
    """Atiende la petición GET /"""
    
    return render(request, "materias/educacion_fisica.html")


@login_required()
def jalisco(request):
    """Atiende la petición GET /"""
    
    return render(request, "materias/jalisco.html")