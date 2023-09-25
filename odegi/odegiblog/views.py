from django.shortcuts import render
from .models import Publicacion


def homepage(request):
    destacado = Publicacion.objects.filter(estatus=1).filter(destacado=True).order_by('-fecha_publicacion')[:1]
    publicaciones = Publicacion.objects.filter(estatus=1).order_by('-fecha_publicacion')[:6]
    colores = ['#ECA0ED', '#B5D2EA', '#FFDBBC', '#FF895A']
    context = {
        'destacado': destacado,
        'publicaciones': publicaciones,
        'colores': colores,
    }

    return render(request, "pages/home.html", context)
