from django.urls import path, include
from django.conf.urls import url

from subir_tarea.models import Tarea
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('subir_tarea/', include("subir_tarea.urls"))
    path('', views.subir_tarea, name="subir_tarea"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
