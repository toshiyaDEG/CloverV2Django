from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def subir_respuesta(request, pk):
    """Atiende la petición GET /"""
    return render(request, "subir_respuesta/subir_respuesta.html", {id:pk})