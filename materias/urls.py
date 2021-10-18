from django.urls import path
from . import views

urlpatterns = [
    path('', views.materias, name="materias"),
    path('lengua_materna/', views.lengua_materna, name="lengua_materna")
]
