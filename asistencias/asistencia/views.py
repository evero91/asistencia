from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.http import require_GET, require_POST

from .models import Persona

def serialize_queryset(queryset):
    return serializers.serialize('json', queryset)

def pagina_asistencia(request):
    personas = Persona.objects.all()
    return render(request, 'asistencia/asistencia.html', {'personas': personas})

@require_GET
def listar_personas(request):
    personas = Persona.objects.all()
    return JsonResponse(serialize_queryset(personas), safe=False)
