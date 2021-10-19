from django.contrib import admin

# Register your models here.
from .models import Tarea

# class TareaAdmin(admin.ModelAdmin):
#     #Se sobre escribe lo que hace __str__
#     list_display = ("materia_tarea", "tema",)

admin.site.register(Tarea)