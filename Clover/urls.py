"""Clover URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', include("home.urls")),
    #path('login/', include("login.urls")),
    #path('registro_alumnos/', include("registro_alumnos.urls")),
    path('lista_alumnos/', include("lista_alumnos.urls")),
    path('materias/', include("materias.urls")),
    path('subir_tarea/', include("subir_tarea.urls")),
    path('subir_respuesta/', include("subir_respuesta.urls")),
    path('cuentas/', include("cuentas.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]