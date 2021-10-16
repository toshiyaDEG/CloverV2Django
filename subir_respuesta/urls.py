from django.urls import path
from . import views

urlpatterns = [
    path('', views.subir_respuesta, name="subir_respuesta"),
]
