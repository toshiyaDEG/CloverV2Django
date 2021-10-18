from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarea


@login_required()
def subir_tarea(request):
    if request.method == "POST":
        archivo2 = request.FILES["archivo"]
        #document =
        # FilesUpload.objects.create(file=file2)
        #document.save()

        Tarea.objects.create(
            archivo=archivo2,
            tema = request.POST["tema"],
            comentario = request.POST["comentario"],
            fechaLimite = request.POST["fechaLimite"],
            materia_tarea= request.POST.get("materia_tarea")
        )
        return HttpResponse("Tu archivo se ha subido correctamente")
    return render(request, "subir_tarea/subir_tarea.html")

