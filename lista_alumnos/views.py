from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def lista_alumnos(request):
    """Atiende la petición GET /"""
    return render(request, "lista_alumnos/lista_alumnos.html")