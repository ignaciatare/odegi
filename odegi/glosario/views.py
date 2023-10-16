from django.shortcuts import render
from .models import Glosario
from odegi.odegiblog.models import Publicacion

def glosario(request):
    terminos = Glosario.objects.filter(estatus=1).order_by('-termino')
    definiciones = {termino.termino: termino.definicion for termino in terminos}
    nuestros_proyectos = Publicacion.objects.filter(estatus=1).filter(seccion=3).order_by('-fecha_publicacion')[:3]
    herramientas = Publicacion.objects.filter(estatus=1).filter(seccion=2).order_by('-fecha_publicacion')
    colores = ['#ECA0ED', '#B5D2EA', '#FFDBBC', '#FF895A']
    context = {
        'terminos': terminos,
        'definiciones': definiciones,
        'proyectos': nuestros_proyectos,
        'herramientas': herramientas,
        'colores': colores,
    }
    return render(request, "nuestro_trabajo.html", context)

