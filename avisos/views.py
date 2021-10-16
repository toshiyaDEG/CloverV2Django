from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def avisos(request):
    """Atiende la petición GET /"""
    return render(request, "avisos/avisos.html")
