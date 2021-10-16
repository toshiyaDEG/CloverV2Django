from django.urls import path
from . import views

urlpatterns = [
    path('', views.materias, name="materias"),
]
