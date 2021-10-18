from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    """Atiende la petición GET /"""
    return render(request, "home/index.html")


# @login_required
# def avisos(request):
#     """Atiende la petición GET /"""
#     return render(request, "avisos/avisos.html")