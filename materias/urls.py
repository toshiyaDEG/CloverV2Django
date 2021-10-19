from django.urls import path
from . import views

urlpatterns = [
    path('', views.materias, name="materias"),
    path('lengua_materna/', views.lengua_materna, name="lengua_materna"),
    path('desafios_matematicos/', views.desafios_matematicos, name="desafios_matematicos"),
    path('ciencias_naturales/', views.ciencias_naturales, name="ciencias_naturales"),
    path('educacion_civica/', views.educacion_civica, name="educacion_civica"),
    path('jalisco/', views.jalisco, name="jalisco"),
    path('educacion_fisica/', views.educacion_fisica, name="educacion_fisica")
]
