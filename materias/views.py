from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def materias(request):
    """Atiende la petición GET /"""
    return render(request, "materias/materias.html")