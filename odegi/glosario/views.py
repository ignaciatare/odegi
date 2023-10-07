from django.shortcuts import render
from .models import Glosario

def glosario(request):
    terminos = Glosario.objects.filter(estatus=1).order_by('-termino')
    context = {
        'terminos': terminos,
        'definicion': Glosario.definicion,
    }
    return render(request, "nuestro_trabajo.html", context)
