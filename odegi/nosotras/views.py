from django.shortcuts import render
from .models import Nosotras


def equipoodegi(request):
    equipo = Nosotras.objects.filter(voluntaria=False).order_by('-nombre')
    voluntarias = Nosotras.objects.filter(voluntaria=True).order_by('-nombre')
    context = {
        'equipo': equipo,
        'voluntarias': voluntarias,
    }
    return render(request, "nosotras.html", context)
