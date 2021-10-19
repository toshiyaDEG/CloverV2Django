from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.subir_respuesta, name="subir_respuesta"),
]
