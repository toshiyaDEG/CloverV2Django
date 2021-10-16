from django.urls import path
from . import views

urlpatterns = [
    path('avisos/', views.avisos, name="avisos"),
]
