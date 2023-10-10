from django.shortcuts import render
from .models import Nosotras


def equipoodegi(request):
    equipo = Nosotras.objects.filter(voluntaria=False)
    voluntarias = Nosotras.objects.filter(voluntaria=True)
    context = {
        'equipo': equipo,
        'voluntarias': voluntarias,
    }
    return render(request, "nosotras.html", context)
